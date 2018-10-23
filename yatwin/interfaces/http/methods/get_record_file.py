from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_record_file (an instance of <ParamMethod>)

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

ENDPOINT = 'get_record_file.cgi'
DESCRIPTION = 'get record file list'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.PAGE_INDEX,
    parameters.PAGE_SIZE,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.PAGE_COUNT,
    parameters.PAGE_INDEX,
    parameters.PAGE_SIZE,
    parameters.RECORD_COUNT,
    parameters.RECORD_NAME_0,
    parameters.RECORD_NUM_0,
    parameters.RECORD_SIZE_0,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_record_file = method_types.ParamMethod \
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
