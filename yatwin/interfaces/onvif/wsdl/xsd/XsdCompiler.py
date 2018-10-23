"""
Contains:
    <XsdCompiler>
"""

class XsdCompiler(object):
    """
    Class allowing a parsed xsd to be compiled.
    In this case, compilation means combining data from
    ... all available sources to produce a singualar
    ... compiled data-structure.
    """

    def __init__(self, xsd_parser, _parsed=None):
        """
        Initialises self.

        :param xsd_parser - An <xsd.XsdParser> instance to be compiled.
        """

        self._init_attrs()

        self.XsdParser = xsd_parser

        self.parsed = self.XsdParser.parse() if _parsed is None else _parsed

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.XsdParser.XsdSource._file_name})>'

    def compile(self):
        """
        Compiles a parsed form of self.WsdlParser into a singualar
        ... compiled data-structure.
        At the moment, this is essentially just a wrapper for xsd.XsdParser.parse
        """

        return self.parsed # Doesn't need to compile it

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.XsdParser = None

        self.parsed = None
