from ..constants import methods
from .BaseMethod import BaseMethod

"""
Contains:
    <DictMethod>

Imports:
    ..constants.methods
    .BaseMethod.BaseMethod
"""

class DictMethod(BaseMethod):
    """
    Inherits from <BaseMethod>
    Returns data as a parsed dictionary
    For use with requests that return JavaScript variables
    ... E.g. var status=1;
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Shorthand wrapper for self.get
        """

        return self.get(*args, **kwargs)

    def get(self, *args, **kwargs):
        """
        Wrapper for BaseMethod.get
        ... returning it as a parsed dictionary
        For use with requests that return JavaScript variables
        ... E.g. var status=1;
        """

        resp = super().get(*args, **kwargs)

        return resp.parse_js()
