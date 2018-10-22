from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_apwifi (an instance of <ParamMethod>)

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

ENDPOINT = 'set_apwifi.cgi'
DESCRIPTION = 'setup AP related parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.APWIFI_ENCRYPT,
    #mode | In CGI SDK, cannot locate on camera
    parameters.APWIFI_KEY,
    parameters.APWIFI_SSID,
    parameters.APWIFI_IPADDR,
    parameters.APWIFI_MASK,
    parameters.APWIFI_STARTIP,
    parameters.APWIFI_ENDIP,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_apwifi = method_types.ParamMethod \
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
