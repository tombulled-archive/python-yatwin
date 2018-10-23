from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing snapshot (an instance of <Snapshot>)

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

ENDPOINT = 'snapshot.cgi'
DESCRIPTION = 'snapshot'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.RES,
)
POST_PARAMETERS = ()
RETURNS = ()
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

snapshot = method_types.Snapshot \
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
