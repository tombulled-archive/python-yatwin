from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing videostream (an instance of <Videostream>)

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

ENDPOINT = 'videostream.cgi'
DESCRIPTION = \
(
    'start firefox and non-IE browser kernel streaming '
    'video request Push. Returns video stream pushed to '
    'non-IE kernel browser'
)
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = ()
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

videostream = method_types.Videostream \
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
