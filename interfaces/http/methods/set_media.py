from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_media (an instance of <ParamMethod>)

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

ENDPOINT = 'set_media.cgi'
DESCRIPTION = 'setup media'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.MAINRATE,
    parameters.ENC_SIZE,
    parameters.ENC_BITRATE,
    parameters.ENC_RATEMODE,
    parameters.ENC_KEYFRAME,
    parameters.ENC_QUANT,
    parameters.ENC_FRAMERATE,
    parameters.SUB_ENC_SIZE,
    parameters.SUB_ENC_BITRATE,
    parameters.SUB_ENC_RATEMODE,
    parameters.SUB_ENC_KEYFRAME,
    parameters.SUB_ENC_QUANT,
    parameters.SUB_ENC_FRAMERATE,
    parameters.MAINMODE,
    parameters.SUBMODE,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_media = method_types.ParamMethod \
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
