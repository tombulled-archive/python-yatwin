from .BaseParam import BaseParam

"""
Library containing <Param>

Imports:
    .BaseParam.BaseParam
"""

class Param(BaseParam):
    """
    Inherits from <BaseParam>
    Parameter object.

    These parameters are likely either only sent (e.g. url?param=val)
    ... or only receieved (e.g. tf_status=1)
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises self
        Initialises super

        Auto-assigns:
            self.getter_identifier (if None)
            self.setter_identifier (if None)
            self.identifiers (if None):
                [self.getter]: self.getter_identifier,
                [self.setter]: self.setter_identifier,
        """
        
        super().__init__(*args, **kwargs)

        self.getter_identifier = self.identifier if self.getter_identifier is None else self.getter_identifier
        self.setter_identifier = self.identifier if self.setter_identifier is None else self.setter_identifier

        if not self.identifiers:
            self.identifiers = {}

            if self.getter and self.getter_identifier:
                self.identifiers[self.getter] = self.getter_identifier
            if self.setter and self.setter_identifier:
                self.identifiers[self.setter] = self.setter_identifier
