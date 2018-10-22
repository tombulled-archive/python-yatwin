from . import PARAMETERS

"""
Library containing utility functions for 'parameters'

Contains:
    get_parameter

Imports:
    .PARAMETERS
"""

def get_parameter \
        (
            set_identifier=None,
            get_identifier=None,
            identifier=None,
            endpoint=None,
        ):
    """
    Attempt to get the parameter from .PARAMETERS where:
        parameter.setter_identifier == set_identifier OR
        parameter.getter_identifier == get_identifier OR
        parameter.identifier == identifier
    """

    for parameter in PARAMETERS:
        if endpoint is not None \
                and parameter.identifiers:
            for method_name, method_identifier in parameter.identifiers.items():
                if method_name == endpoint and \
                        (
                            method_identifier == identifier or \
                            method_identifier == get_identifier or \
                            method_identifier == set_identifier
                        ):
                    return parameter
            else:
                continue

        if set_identifier is not None \
                and parameter.setter_identifier != set_identifier:
            continue

        if get_identifier is not None \
                and parameter.getter_identifier != get_identifier:
            continue

        if identifier is not None \
                and parameter.identifier != identifier:
            continue

        return parameter
