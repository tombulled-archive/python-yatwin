from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_camera_params (an instance of <ParamMethod>)

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

ENDPOINT = 'get_camera_params.cgi'
DESCRIPTION = 'get device video related parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.MAINSTREAMHEIGHT,
    parameters.MAINSTREAMWIDTH,
    parameters.OSDENABLE,
    parameters.CAMERA_TYPE,
    parameters.ENC_BITRATE,
    parameters.ENC_FRAMERATE,
    parameters.ENC_KEYFRAME,
    parameters.ENC_MAIN_MODE,
    parameters.ENC_QUANT,
    parameters.ENC_RATEMODE,
    parameters.ENC_SIZE,
    parameters.IRCUT,
    parameters.RESOLUTION,
    parameters.RESOLUTIONSUB,
    parameters.RESOLUTIONSUBSUB,
    parameters.PTZ_PATROL_RATE,
    parameters.SUB_ENC_BITRATE,
    parameters.SUB_ENC_FRAMERATE,
    parameters.SUB_ENC_KEYFRAME,
    parameters.SUB_ENC_QUANT,
    parameters.SUB_ENC_RATEMODE,
    parameters.SUB_ENC_SIZE,
    parameters.SUB_SUB_ENC_BITRATE,
    parameters.SUB_SUB_ENC_FRAMERATE,
    parameters.SUB_SUB_ENC_KEYFRAME,
    parameters.SUB_SUB_ENC_QUANT,
    parameters.SUB_SUB_ENC_RATEMODE,
    parameters.SUB_SUB_ENC_SIZE,
    parameters.VBRIGHT,
    parameters.VCONTRAST,
    parameters.VHUE,
    parameters.VSATURATION,
    parameters.FLIP, # (camera_control.cgi) param=5 (flipe and mirror)
    parameters.MODE, # (camera_control.cgi) param=3 (mode): means camera operating voltage (Hz)
    parameters.OUTVOLUME, # (camera_control.cgi) param=25 (output volume)
    parameters.INVOLUME, # (camera_control.cgi) param=24 (Input volume)
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_camera_params = method_types.ParamMethod \
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
