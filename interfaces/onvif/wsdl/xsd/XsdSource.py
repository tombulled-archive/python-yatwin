import bs4
import os.path

"""
Contains:
    <XsdSource>

Imports:
    bs4
    os.path
"""

class XsdSource(bs4.BeautifulSoup):
    """
    Direct wrapper for bs4.BeautifulSoup
    ... using its 'xml' feature
    """

    def __init__(self, path):
        """
        Initialises self and super.
        Opens the file in location 'path'
        ... and closes it afterwards
        """

        self._init_attrs()

        self.path = path

        self._file_name = os.path.basename(self.path)

        with open(path, 'rb') as file:
            super().__init__(file, features='xml')

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self._file_name})>'

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.path = None

        self._file_name = None
