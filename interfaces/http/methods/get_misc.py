from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_misc (an instance of <ParamMethod>)

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

ENDPOINT = 'get_misc.cgi'
DESCRIPTION = 'get device pan tilt related parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.DEVICETYPE,
    parameters.LED_MODE,
    parameters.PRESET_ONSTART,
    parameters.PTRUNTIMES,
    parameters.PTZ_CENTER_ONSTART,
    parameters.PTZ_DISPPRESET,
    parameters.PTZ_PATROL_DOWN_RATE,
    parameters.PTZ_PATROL_LEFT_RATE,
    parameters.PTZ_PATROL_RATE,
    parameters.PTZ_PATROL_RIGHT_RATE,
    parameters.PTZ_PATROL_UP_RATE,
    parameters.PTZ_SOFT_LIMIT_MAX_LEVEL,
    parameters.PTZ_SOFT_LIMIT_MAX_VERT,
    parameters.PTZ_SOFT_LIMIT_STOP_PERCENT_LEVEL,
    parameters.PTZ_SOFT_LIMIT_STOP_PERCENT_VERT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_misc = method_types.ParamMethod \
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
