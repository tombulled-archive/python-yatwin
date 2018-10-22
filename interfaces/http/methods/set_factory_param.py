from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_factory_param (an instance of <ParamMethod>)

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

ENDPOINT = 'set_factory_param.cgi'
DESCRIPTION = 'setup factory default parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.WIFIMAC,
    parameters.MAC,
    parameters.FACTORY_SERVER,
    parameters.FACTORY_USER,
    parameters.FACTORY_PASSWD,
    parameters.FACTORY_DOMAIN_PORT,
    parameters.FACTORY_ALARM_SERVER,
    parameters.FACTORY_HEARTBEAT, # Referenced as 'heatbeat' in the SDK
    #serviceindex | In CGI SDK, cannot locate on camera
    parameters.FACTORY_INDEX,
    parameters.DEVICEID,
    parameters.PNPSERVER,
    parameters.PNPPORT,
    #mode | In CGI SDK, cannot locate on camera

)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_factory_param = method_types.ParamMethod \
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
