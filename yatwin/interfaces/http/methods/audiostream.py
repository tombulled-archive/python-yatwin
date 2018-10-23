from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing audiostream (an instance of <Audiostream>)

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

ENDPOINT = 'audiostream.cgi'
DESCRIPTION = 'request video communication'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.STREAM_ID,
)
POST_PARAMETERS = ()
RETURNS = ()
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

audiostream = method_types.Audiostream \
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
