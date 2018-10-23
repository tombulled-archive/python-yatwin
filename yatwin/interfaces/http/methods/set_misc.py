from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_misc (an instance of <ParamMethod>)

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

ENDPOINT = 'set_misc.cgi'
DESCRIPTION = 'setup camera PTZ parameters'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.LED_MODE,
    parameters.PTRUNTIMES,
    parameters.PTZ_PATROL_RATE,
    parameters.PTZ_PATROL_UP_RATE,
    parameters.PTZ_PATROL_DOWN_RATE,
    parameters.PTZ_PATROL_LEFT_RATE,
    parameters.PTZ_PATROL_RIGHT_RATE,
    parameters.PTZ_DISPPRESET,
    parameters.PTZ_CENTER_ONSTART,
    parameters.PRESET_ONSTART,
    parameters.PTZ_SOFT_LIMIT_MAX_VERT,
    parameters.PTZ_SOFT_LIMIT_MAX_LEVEL,
    parameters.PTZ_SOFT_LIMIT_STOP_PERCENT_VERT,
    parameters.PTZ_SOFT_LIMIT_STOP_PERCENT_LEVEL,
    parameters.OSDENABLE,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_misc = method_types.ParamMethod \
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
