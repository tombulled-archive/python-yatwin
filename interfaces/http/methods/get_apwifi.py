from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_apwifi (an instance of <ParamMethod>)

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

ENDPOINT = 'get_apwifi.cgi'
DESCRIPTION = 'get AP related parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.APWIFI_ENCRYPT,
    parameters.APSWIFI_PORT,
    parameters.APWIFI_KEY,
    parameters.APWIFI_SSID,
    parameters.APWIFI_IPADDR,
    parameters.APWIFI_MASK,
    parameters.APWIFI_STARTIP,
    parameters.APWIFI_ENDIP,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_apwifi = method_types.ParamMethod \
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
