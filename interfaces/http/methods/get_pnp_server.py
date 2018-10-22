from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_pnp_server (an instance of <ParamMethod>)

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

ENDPOINT = 'get_pnp_server.cgi'
DESCRIPTION = 'get P2P server configuration parameters'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.PNPPORT,
    parameters.PNPPWD,
    parameters.PNPSERVER,
    parameters.PNPUSER,
    parameters.SYSVER,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_pnp_server = method_types.ParamMethod \
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
