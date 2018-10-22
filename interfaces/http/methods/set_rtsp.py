from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_rtsp (an instance of <ParamMethod>)

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

ENDPOINT = 'set_rtsp.cgi'
DESCRIPTION = \
(
    'Setup rtsp certificate service. '
    'rtspuser, rtsppwd and rtspenable are not implemented. '
    'RTSP uses HTTP auth. The port can be changed.'
)
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.RTSP_AUTH_ENABLE,
    parameters.RTSPPORT,
    parameters.RTSPUSER,
    parameters.RTSPPWD,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_rtsp = method_types.ParamMethod \
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
