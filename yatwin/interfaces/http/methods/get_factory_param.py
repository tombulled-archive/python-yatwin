from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_factory_param (an instance of <ParamMethod>)

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

ENDPOINT = 'get_factory_param.cgi'
DESCRIPTION = 'get device factory default setting parameter'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.CUSTOMER_CODE,
    parameters.FACTORY_ALARM_SERVER,
    parameters.FACTORY_HEARTBEAT,
    parameters.FACTORY_INDEX,
    parameters.FACTORY_DDNS_MODE,
    parameters.FACTORY_PASSWD,
    parameters.FACTORY_DOMAIN_PORT,
    parameters.FACTORY_SERVER,
    parameters.FACTORY_DDNS_STATUS,
    parameters.FACTORY_USER,
    parameters.FACTORY_PRODUCTION_ORDER,
    parameters.FACTORY_SHIPMENT_ORDER,
    parameters.SUPPORT_ADPCM_VERSION,
    parameters.SUPPORT_CLOUD_STORAGE,
    parameters.SUPPORT_PIGEON_PUSH,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_factory_param = method_types.ParamMethod \
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
