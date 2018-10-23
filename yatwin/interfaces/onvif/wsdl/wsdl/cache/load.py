from ... import wsdl
import os.path
import pickle

"""
Imports:
    ...wsdl
    os.path
    pickle

Contains:
    load
    _load
"""

def load(wsdl_path, xsd_scope=()):
    """
    Loads the cached form of the wsdl located
    ... in wsdl_path

    This will check that the following files exist:
        wsdl_path
        *the parsed cache file*
        *the compiled cache file*
    """

    directory = os.path.dirname(wsdl_path)
    filename = os.path.basename(wsdl_path)

    ext_parsed = '.parsed.pickle'
    ext_compiled = '.compiled.pickle'
    ext_directory = '\\cache\\'

    if not os.path.isfile(wsdl_path):
        return

    path_parsed = directory + ext_directory + filename + ext_parsed
    path_compiled = directory + ext_directory + filename + ext_compiled

    if not os.path.isfile(path_parsed):
        return
    if not os.path.isfile(path_compiled):
        return

    with open(path_parsed, 'rb') as file_parsed:
        data_parsed = pickle.load(file_parsed)

    with open(path_compiled, 'rb') as file_compiled:
        data_compiled = pickle.load(file_compiled)

    return _load(wsdl_path, data_parsed, data_compiled, xsd_scope)

def _load(wsdl_path, parsed, compiled, xsd_scope):
    """
    Given that paths of:
        The .wsdl file
        The .parsed.pickle file
        The .compiled.pickle file
    Create the <Wsdl> object from the cache
    ... which it then returns
    """

    WsdlSource = wsdl.WsdlSource(wsdl_path) # bs4 will still parse it
    WsdlParser = wsdl.WsdlParser(WsdlSource)
    WsdlCompiler = wsdl.WsdlCompiler(WsdlParser, _parsed=parsed, xsd_scope=xsd_scope)
    Wsdl = wsdl.Wsdl(wsdl_path, _compiled=compiled, _WsdlSource=WsdlSource, _WsdlParser=WsdlParser, _WsdlCompiler=WsdlCompiler)

    return Wsdl
