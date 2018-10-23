"""
Library containing <BaseParam>
"""

class BaseParam(object):
    """
    Base Parameter object. Designed to be inherited from.
    """

    def __init__ \
        (
            self,
            identifier = None,
            description = None,
            values = None,
            constant = None,
            constant_assumed = None,
            getter = None,
            setter = None,
            getter_identifier = None,
            setter_identifier = None,
            identifiers = {},
        ):
        """
        Initialises self
        """

        self._init_attrs()

        self.identifier = identifier
        self.description = description
        self.values = values
        self.constant = constant
        self.constant_assumed = constant_assumed
        self.getter = getter
        self.setter = setter
        self.getter_identifier = getter_identifier
        self.setter_identifier = setter_identifier
        self.identifiers = identifiers

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(identifier)>
        Where:
        ... class_name = self.__class__.__name__
        ... identifier = self.identifier
        """

        return f'<{self.__class__.__name__}({self.identifier})>'

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value (usually None)
        """

        self.identifier = None
        self.description = None
        self.values = None
        self.constant = None
        self.constant_assumed = None
        self.getter = None
        self.setter = None
        self.getter_identifier = None
        self.setter_identifier = None
        self.indentifiers = {}
