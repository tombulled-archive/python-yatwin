"""
Library containing:
    <BaseFile>
"""

class BaseFile(object):
    """
    Base File object. Designed to be inherited from.
    """

    def __init__(self, identifier=None, description=None):
        """
        Initialises self.
        """

        self._init_attrs()

        self.identifier = identifier
        self.description = description

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(identifier)>
        """

        return f'<{self.__class__.__name__}({self.identifier})>'

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value (usually None)
        """

        self.identifier = None
        self.description = None
