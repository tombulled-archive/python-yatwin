from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_devices (an instance of <ParamMethod>)

Constants defined here:
    ENDPOINT
    DESCRIPTION
    GET_PARAMETERS
    POST_PARAMETERS
    RETURNS
    METHOD
    FILES

Imports:
    .method_types
    ..parameters
    .constants.permissions
    .constants.methods
"""

ENDPOINT = 'set_devices.cgi'
DESCRIPTION = 'setup multiple device parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.DEV2_ALIAS,
    parameters.DEV2_HOST,
    parameters.DEV2_PORT,
    parameters.DEV2_USER,
    parameters.DEV2_PWD,
    parameters.DEV3_ALIAS,
    parameters.DEV3_HOST,
    parameters.DEV3_PORT,
    parameters.DEV3_USER,
    parameters.DEV3_PWD,
    parameters.DEV4_ALIAS,
    parameters.DEV4_HOST,
    parameters.DEV4_PORT,
    parameters.DEV4_USER,
    parameters.DEV4_PWD,
    parameters.DEV5_ALIAS,
    parameters.DEV5_HOST,
    parameters.DEV5_PORT,
    parameters.DEV5_USER,
    parameters.DEV5_PWD,
    parameters.DEV6_ALIAS,
    parameters.DEV6_HOST,
    parameters.DEV6_PORT,
    parameters.DEV6_USER,
    parameters.DEV6_PWD,
    parameters.DEV7_ALIAS,
    parameters.DEV7_HOST,
    parameters.DEV7_PORT,
    parameters.DEV7_USER,
    parameters.DEV7_PWD,
    parameters.DEV8_ALIAS,
    parameters.DEV8_HOST,
    parameters.DEV8_PORT,
    parameters.DEV8_USER,
    parameters.DEV8_PWD,
    parameters.DEV9_ALIAS,
    parameters.DEV9_HOST,
    parameters.DEV9_PORT,
    parameters.DEV9_USER,
    parameters.DEV9_PWD,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_devices = method_types.ParamMethod \
(
    endpoint = ENDPOINT,
    description = DESCRIPTION,
    get_parameters = GET_PARAMETERS,
    post_parameters = POST_PARAMETERS,
    returns = RETURNS,
    permission = PERMISSION,
    method = METHOD,
    files = FILES,
)
