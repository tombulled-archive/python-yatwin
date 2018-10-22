"""
Imports:
    .system_parameters.*
    .parameters.*
    .controller_parameters.*
    .system_parameters
    .parameters
    .controller_parameters

Constants defined here:
    PARAMETERS - List of all parameters
    parameter_libs - Tuple of parameter libraries
"""

from .system_parameters import *
from .parameters import *
from .controller_parameters import *
from . import system_parameters
from . import parameters
from . import controller_parameters

parameter_libs = \
(
    system_parameters,
    parameters,
    controller_parameters,
)

PARAMETERS = []

for parameter_lib in parameter_libs:
    for attribute in dir(parameter_lib):
        if attribute.startswith('_') or not attribute.isupper():
            continue

        PARAMETERS.append(getattr(parameter_lib, attribute))
