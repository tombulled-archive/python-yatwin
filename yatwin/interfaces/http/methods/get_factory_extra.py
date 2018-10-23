from . import method_types
from .. import parameters
from .constants import permissions
from .constants import methods

"""
Library containing get_factory_extra (an instance of <ParamMethod>)

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

ENDPOINT = 'get_factory_extra.cgi'
DESCRIPTION = 'get ADC related parameters'
GET_PARAMETERS = \
(
    parameters.LOGINUSE,
    parameters.LOGINPAS,
)
POST_PARAMETERS = ()
RETURNS = \
(
    parameters.ADC_MAX,
    parameters.ADC_MIN,
    parameters.ADC_USE,
    parameters.ADC_V,
    parameters.EXP_ADC,
    parameters.EXP_AVELUM,
    parameters.EXP_GAIN,
    parameters.GET_ADC,
    parameters.GET_AVELUM,
    parameters.GET_GAIN,
    parameters.IR_ATTR,
    parameters.IR_OFF_VAL,
    parameters.IR_OFF_COM,
    parameters.IR_ON_COM,
    parameters.IR_ON_VAL,
)
PERMISSION = permissions.ADMINISTRATOR
METHOD = methods.GET
FILES = ()

get_factory_extra = method_types.ParamMethod \
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
