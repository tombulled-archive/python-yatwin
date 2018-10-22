from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
"""

ENDPOINT = 'livestream.cgi'
DESCRIPTION = 'ask video communication'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.STREAM_ID,
    parameters.AUDIO,
    parameters.RES,
    parameters.SUB_STREAM,
    parameters.FILE_NAME,
    parameters.OFFSET,
)
POST_PARAMETERS = ()
RETURNS = ()
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

livestream = method_types.Livestream \
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
