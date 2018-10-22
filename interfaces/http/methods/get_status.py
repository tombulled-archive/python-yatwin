from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_status (an instance of <ParamMethod>)

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

ENDPOINT = 'get_status.cgi'
DESCRIPTION = 'Get device status'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.ALARM_STATUS,
    parameters.ALIAS,
    parameters.APP_VERSION,
    parameters.CAMERA_TYPE,
    parameters.CUSTOMER_CODE,
    parameters.DEVICEID,
    parameters.DEVICE_SUB_TYPE,
    parameters.DEVICETYPE,
    parameters.DNS_STATUS,
    parameters.DNS_ENABLE,
    parameters.ENCRYPT,
    parameters.EXTERN_WIFI,
    parameters.INTERNET,
    parameters.MAC,
    parameters.TIME_NOW,
    parameters.OEM_ID,
    parameters.OSDENABLE,
    parameters.P2P_STATUS,
    parameters.PARAMS_MD5,
    parameters.PASSWORD_CHANGE_REALTIME,
    parameters.RECORD_SD_STATUS,
    parameters.SD_FREE,
    parameters.SD_LEVEL,
    parameters.SD_STATUS,
    parameters.SD_TOTAL,
    parameters.SYS_VER,
    parameters.SYSTEM_WIFI_MODE,
    parameters.TIMEPLAN_VERSION,
    parameters.UNDER,
    parameters.UPNP_STATUS,
    parameters.WIFIMAC,
)
PERMISSION = permissions.MANAGER
METHOD = methods.GET
FILES = ()

get_status = method_types.ParamMethod \
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
