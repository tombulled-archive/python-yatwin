from .WsdlCompiler import WsdlCompiler
from .WsdlParser import WsdlParser
from .WsdlSource import WsdlSource

"""
Library containing <Wsdl>

Imports:
    .WsdlCompiler.WsdlCompiler
    .WsdlParser.WsdlParser
    .WsdlSource.WsdlSource
"""

class Wsdl(object):
    """
    Class that provides basic bs4.BeautifulSoup
    ... interaction to WsdlCompiler
    """

    def __init__(self, path, xsd_scope=None, _compiled=None, _WsdlSource=None, _WsdlParser=None, _WsdlCompiler=None):
        """
        Initialises self.
        Turns 'path' into a WsdlSource
        Parses it and then compiles it.
        """

        self._init_attrs()

        self.WsdlSource = WsdlSource(path) if _WsdlSource is None else _WsdlSource
        self.WsdlParser = WsdlParser(self.WsdlSource) if _WsdlParser is None else _WsdlParser
        self.WsdlCompiler = WsdlCompiler(self.WsdlParser, xsd_scope=xsd_scope) if _WsdlCompiler is None else _WsdlCompiler

        self.compiled = self.WsdlCompiler.compile() if _compiled is None else _compiled

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(file_name)>
        """

        return f'<{self.__class__.__name__}({self.WsdlSource._file_name})>'

    def find(self, name=None, index=None, soap_action=None):
        """
        Find the first operation where:
            operation['Name'] = name AND/OR
            operation['Index'] = index AND/OR
            operation['SOAPAction'] = soap_action
        """

        match = {}

        if name is not None:
            match['Name'] = name
        if index is not None:
            match['Index'] = index
        if soap_action is not None:
            match['SOAPAction'] = soap_action

        for operation in self.compiled:
            if not match:
                return operation
            for key, val in match.items():
                if operation[key] == val:
                    return operation

    def find_all(self, name=None, index=None, soap_action=None):
        """
        Find all operations where:
            operation['Name'] = name AND/OR
            operation['Index'] = index AND/OR
            operation['SOAPAction'] = soap_action
        """

        match = {}
        data = []

        if name is not None:
            match['Name'] = name
        if index is not None:
            match['Index'] = index
        if soap_action is not None:
            match['SOAPAction'] = soap_action

        for operation in self.compiled:
            if not match:
                data.append(operation)
                continue

            for key, val in match.items():
                if operation[key] == val:
                    data.append(operation)

                    break

        return data

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usually None)
        """

        self.WsdlSource = None
        self.WsdlParser = None
        self.WsdlCompiler = None

        self.compiled = None
