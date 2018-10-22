from .BaseParam import BaseParam

"""
Library containing <SystemParam>

Imports:
    .BaseParam.BaseParam
"""

class SystemParam(BaseParam):
    """
    Inherits from <BaseParam>
    System Parameter object.

    These parameters are both sent and retrieved (potentially under different names)
    ... therefore they need a reference to both a setter and a getter
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        super().__init__(*args, **kwargs)
