from .BaseParam import BaseParam

"""
Library containing <ControllerParam>

Imports:
    .BaseParam.BaseParam
"""

class ControllerParam(BaseParam):
    """
    Inherits from <BaseParam>
    Controller Parameter object.

    These parameters are only retrieved via these identifiers,
    ... however are able to be edited by a *_controller method
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        super().__init__(*args, **kwargs)
