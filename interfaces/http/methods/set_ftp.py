from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_ftp (an instance of <ParamMethod>)

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

ENDPOINT = 'set_ftp.cgi'
DESCRIPTION = 'setup device ftp'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.FTP_SVR,
    parameters.FTP_PORT,
    parameters.FTP_USER,
    parameters.FTP_PWD,
    parameters.FTP_DIR,
    parameters.FTP_MODE,
    parameters.FTP_UPLOAD_INTERVAL,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_ftp = method_types.ParamMethod \
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
