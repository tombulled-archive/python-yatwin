from .XsdCompiler import XsdCompiler
from .XsdParser import XsdParser
from .XsdSource import XsdSource

"""
Contains:
    <Xsd>

Imports:
    .XsdCompiler.XsdCompiler
    .XsdParser.XsdParser
    .XsdSource.XsdSource
"""

class Xsd(object):
    """
    Class to pull together instances of:
        <XsdCompiler>
        <XsdParser>
        <XsdSource>
    """

    def __init__(self, path, _compiled=None, _XsdSource=None, _XsdParser=None, _XsdCompiler=None):
        """
        Initialises self.
        Turns 'path' into an <xsd.XsdSource>
        Parses it and then compiles it.
        """

        self._init_attrs()

        self.XsdSource = XsdSource(path) if _XsdSource is None else _XsdSource
        self.XsdParser = XsdParser(self.XsdSource) if _XsdParser is None else _XsdParser
        self.XsdCompiler = XsdCompiler(self.XsdParser) if _XsdCompiler is None else _XsdCompiler

        self.compiled = self.XsdCompiler.compile() if _compiled is None else _compiled

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.XsdSource._file_name})>'

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.XsdSource = None
        self.XsdParser = None
        self.XsdCompiler = None

        self.compiled = None
