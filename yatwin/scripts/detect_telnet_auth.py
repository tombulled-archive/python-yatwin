from ..interfaces.telnet import Telnet
from ..interfaces.telnet import constants
from ..interfaces.telnet import errors
from .. import decorators
import logging

"""
Imports:
    ..interfaces.telnet.Telnet
    ..interfaces.telnet.constants
    ..interfaces.telnet.errors
    ..decorators
    logging

Contains:
    detect_telnet_auth

This may soon be deprecated
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def detect_telnet_auth(host):
    """
    Essentially a small brute-force attack to
    ... determine the login credentials for
    ... telnet
    Attempts each username, password from
    ... ..interfaces.telnet.constants.KNOWN_LOGINS

    Returns:
        {
            'username': username,
            'password': password,
        }
    """

    telnet = None

    for username, password in constants.KNOWN_LOGINS:
        data = \
        {
            'username': username,
            'password': password,
        }

        try:
            if telnet is None:
                telnet = Telnet(host, username=username, password=password)
            else:
                telnet.username = username
                telnet.password = password
                telnet._initialise() # After 3 login attempts, the connection will get dropped

            data['_telnet'] = telnet

            return data
        except errors.LoginFailed as error_login_failed:
            logger.debug('Login failed:', error_login_failed)

            continue
        except Exception as error: # [WinError 10061] No connection could be made because the target machine actively refused it
            logger.debug('Login failed:', error)
            break

        logger.debug('Failed to detect telnet auth')
