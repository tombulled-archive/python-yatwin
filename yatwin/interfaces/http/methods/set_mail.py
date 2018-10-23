from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_mail (an instance of <ParamMethod>)

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
    .parameters
    .constants.permissions
    .constants.methods
"""

ENDPOINT = 'set_mail.cgi'
DESCRIPTION = 'setup mail service'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.MAIL_SENDER,
    parameters.MAIL_RECEIVER1,
    parameters.MAIL_RECEIVER2,
    parameters.MAIL_RECEIVER3,
    parameters.MAIL_RECEIVER4,
    parameters.MAILSSL,
    parameters.MAIL_SVR,
    parameters.MAIL_PORT,
    parameters.MAIL_USER,
    parameters.MAIL_PWD,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_mail = method_types.ParamMethod \
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
