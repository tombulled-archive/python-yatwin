from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_recordsch (an instance of <ParamMethod>)

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

ENDPOINT = 'set_recordsch.cgi'
DESCRIPTION = 'setup record settings'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.RECORD_COVER_ENABLE,
    #record_time | In CGI SDK, cannot locate on camera
    parameters.RECORD_AUDIO,
    parameters.RECORD_TIME_ENABLE,
    parameters.ALARM_SCHEDULE_MON_0,
    parameters.ALARM_SCHEDULE_MON_1,
    parameters.ALARM_SCHEDULE_MON_2,
    parameters.ALARM_SCHEDULE_TUE_0,
    parameters.ALARM_SCHEDULE_TUE_1,
    parameters.ALARM_SCHEDULE_TUE_2,
    parameters.ALARM_SCHEDULE_WED_0,
    parameters.ALARM_SCHEDULE_WED_1,
    parameters.ALARM_SCHEDULE_WED_2,
    parameters.ALARM_SCHEDULE_THU_0,
    parameters.ALARM_SCHEDULE_THU_1,
    parameters.ALARM_SCHEDULE_THU_2,
    parameters.ALARM_SCHEDULE_FRI_0,
    parameters.ALARM_SCHEDULE_FRI_1,
    parameters.ALARM_SCHEDULE_FRI_2,
    parameters.ALARM_SCHEDULE_SAT_0,
    parameters.ALARM_SCHEDULE_SAT_1,
    parameters.ALARM_SCHEDULE_SAT_2,
    parameters.ALARM_SCHEDULE_SUN_0,
    parameters.ALARM_SCHEDULE_SUN_1,
    parameters.ALARM_SCHEDULE_SUN_2,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_recordsch = method_types.ParamMethod \
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
