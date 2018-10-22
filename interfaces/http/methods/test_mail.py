from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing test_mail (an instance of <ParamMethod>)

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

ENDPOINT = 'test_mail.cgi'
DESCRIPTION = 'Get Email test results'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

test_mail = method_types.ParamMethod \
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
