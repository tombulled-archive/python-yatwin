from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_aging (an instance of <ParamMethod>)

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

ENDPOINT = 'get_aging.cgi'
DESCRIPTION = 'get related aging parameters. aging mode'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.AGING_ENABLE,
    parameters.PTZSPEED,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_aging = method_types.ParamMethod \
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
