from .. import decorators
import logging

"""
Imports:
    ..decorators
    logging

Contains:
    hack_http_auth

May soon be deprecated/improved
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def protect_http_auth(telnet):
    """
    Deletes the system.ini file which is used
    ... to hack http auth

    Note: network-b.ini (and network.ini) can be
    ... used to hack wifi psk
    Note: system-b.ini (and system.ini) can be
    ... used to hack http auth
    Note: Deleting these .ini files can cause
    ... the camera to reset
    """

    resp = telnet.execute('rm /system/www/system.ini')

    flag_failed = \
    (
        'rm: can\'t remove \'/system/www/system.ini\': '
        'No such file or directory'
    )

    success = resp != flag_failed

    if not success:
        logger.debug('Failed to remove system.ini: {resp}')
    else:
        logger.debug('system.ini removed successfuly')

    return success
