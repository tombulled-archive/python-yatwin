from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_record (an instance of <ParamMethod>)

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

ENDPOINT = 'get_record.cgi'
DESCRIPTION = 'get device video related parameters'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.ENC_BITRATE,
    parameters.ENC_FRAMERATE,
    parameters.ENC_KEYFRAME,
    parameters.ENC_MAIN_MODE,
    parameters.ENC_QUANT,
    parameters.ENC_RATEMODE,
    parameters.ENC_SIZE,
    parameters.ENC_SUB_MODE,
    parameters.RECORD_AUDIO,
    parameters.RECORD_CHANNEL,
    parameters.RECORD_COVER_ENABLE,
    parameters.RECORD_SCHEDULE_FRI_0,
    parameters.RECORD_SCHEDULE_FRI_1,
    parameters.RECORD_SCHEDULE_FRI_2,
    parameters.RECORD_SCHEDULE_MON_0,
    parameters.RECORD_SCHEDULE_MON_1,
    parameters.RECORD_SCHEDULE_MON_2,
    parameters.RECORD_SCHEDULE_TUE_0,
    parameters.RECORD_SCHEDULE_TUE_1,
    parameters.RECORD_SCHEDULE_TUE_2,
    parameters.RECORD_SCHEDULE_WED_0,
    parameters.RECORD_SCHEDULE_WED_1,
    parameters.RECORD_SCHEDULE_WED_2,
    parameters.RECORD_SCHEDULE_THU_0,
    parameters.RECORD_SCHEDULE_THU_1,
    parameters.RECORD_SCHEDULE_THU_2,
    parameters.RECORD_SCHEDULE_SUN_0,
    parameters.RECORD_SCHEDULE_SUN_1,
    parameters.RECORD_SCHEDULE_SUN_2,
    parameters.RECORD_SCHEDULE_SAT_0,
    parameters.RECORD_SCHEDULE_SAT_1,
    parameters.RECORD_SCHEDULE_SAT_2,
    parameters.RECORD_SD_STATUS,
    parameters.RECORD_SIZE,
    parameters.RECORD_TIME_ENABLE,
    parameters.RECORD_TIMER,
    parameters.SD_FREE,
    parameters.SD_TOTAL,
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
    parameters.TF_ENABLE,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_record = method_types.ParamMethod \
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
