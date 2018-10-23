from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_wifi_scan_result (an instance of <ParamMethod>)

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

ENDPOINT = 'get_wifi_scan_result.cgi'
DESCRIPTION = 'get device seach WiFi list result'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.AP_CHANNEL,
    parameters.AP_DBM_0,
    parameters.AP_DBM_1,
    parameters.AP_MAC,
    parameters.AP_MODE,
    parameters.AP_NUMBER,
    parameters.AP_SECURITY,
    parameters.AP_SSID,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_wifi_scan_result = method_types.ParamMethod \
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
