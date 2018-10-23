from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_alarm (an instance of <ParamMethod>)

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

ENDPOINT = 'set_alarm.cgi'
DESCRIPTION = \
(
    'setup device alarm option (motion detection, sound alarm, '
    'GPIO alarm, temperature and humidity alarm)'
)
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.ALARM_MOTION_ARMED,
    parameters.ALARM_MOTION_SENSITIVITY,
    parameters.ALARM_MAIL,
    parameters.ALARM_RECORD,
    parameters.ALARM_AUDIO,
    parameters.ALARM_PRESETSIT,
    parameters.ALARM_UPLOAD_INTERVAL,
    parameters.ALARM_SCHEDULE_ENABLE,
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
    #enable_alarm_audio | In CGI SDK, cannot locate on camera
    parameters.ALARM_SNAPSHOT,
    parameters.ALARM_HTTP,
    parameters.ALARM_HTTP_URL,
    parameters.ALARM_SERVER,
    parameters.ALARM_USER,
    parameters.ALARM_PWD,
    #alarmdeviceid | In CGI SDK, cannot locate on camera
    parameters.MOTION_PLAN_1,
    parameters.MOTION_PLAN_2,
    parameters.MOTION_PLAN_3,
    parameters.MOTION_PLAN_4,
    parameters.MOTION_PLAN_5,
    parameters.MOTION_PLAN_6,
    parameters.MOTION_PLAN_7,
    parameters.MOTION_PLAN_8,
    parameters.MOTION_PLAN_9,
    parameters.MOTION_PLAN_10,
    parameters.MOTION_PLAN_11,
    parameters.MOTION_PLAN_12,
    parameters.MOTION_PLAN_13,
    parameters.MOTION_PLAN_14,
    parameters.MOTION_PLAN_15,
    parameters.MOTION_PLAN_16,
    parameters.MOTION_PLAN_17,
    parameters.MOTION_PLAN_18,
    parameters.MOTION_PLAN_19,
    parameters.MOTION_PLAN_20,
    parameters.MOTION_PLAN_21,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_alarm = method_types.ParamMethod \
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
