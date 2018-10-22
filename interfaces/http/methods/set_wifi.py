from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_wifi (an instance of <ParamMethod>)

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

ENDPOINT = 'set_wifi.cgi'
DESCRIPTION = 'setup device wifi parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.WIFI_ENABLE,
    parameters.WIFI_SSID,
    parameters.WIFI_CHANNEL,
    parameters.WIFI_MODE,
    parameters.WIFI_AUTHTYPE,
    parameters.WIFI_ENCRYPT,
    parameters.WIFI_KEYFORMAT,
    parameters.WIFI_DEFKEY,
    parameters.WIFI_KEY1,
    parameters.WIFI_KEY1_BITS,
    parameters.WIFI_KEY2,
    parameters.WIFI_KEY2_BITS,
    parameters.WIFI_KEY3,
    parameters.WIFI_KEY3_BITS,
    parameters.WIFI_KEY4,
    parameters.WIFI_KEY4_BITS,
    parameters.WIFI_WPA_PSK,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_wifi = method_types.ParamMethod \
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
