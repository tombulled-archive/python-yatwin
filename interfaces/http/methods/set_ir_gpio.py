from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing set_ir_gpio (an instance of <ParamMethod>)

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

ENDPOINT = 'set_ir_gpio.cgi'
DESCRIPTION = 'control infrared light'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
    parameters.NEXT_URL,
    parameters.VAL,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.RESULT,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

set_ir_gpio = method_types.ParamMethod \
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
