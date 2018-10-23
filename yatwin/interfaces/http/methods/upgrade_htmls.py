from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods
from ..files import firmware_files

"""
Library containing upgrade_htmls (an instance of <ParamMethod>)

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

ENDPOINT = 'upgrade_htmls.cgi'
DESCRIPTION = \
(
    'upgrade device web interface. Note: this cgi compress files '
    'which need upgrade and send to IP camera through post. '
    'Post a .bin firmware file using the filename \'file\''
)
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,  # Not always the case, returns nothing if no file was uploaded
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.POST
FILES = \
(
    firmware_files.FILE,
)

upgrade_htmls = method_types.ParamMethod \
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
