from ... import xsd
import os.path
import pickle

"""
Imports:
    ...xsd
    os.path
    pickle

Contains:
    load
    _load
"""

def load(xsd_path):
    """
    Loads the cached form of the xsd located
    ... in xsd_path

    This will check that the following files exist:
        xsd_path
        *the parsed cache file*
        *the compiled cache file*
    """

    directory = os.path.dirname(xsd_path)
    filename = os.path.basename(xsd_path)

    ext_parsed = '.parsed.pickle'
    ext_compiled = '.compiled.pickle'
    ext_directory = '\\cache\\'

    if not os.path.isfile(xsd_path):
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

    return _load(xsd_path, data_parsed, data_compiled)

def _load(xsd_path, parsed, compiled):
    """
    Given that paths of:
        The .xsd file
        The .parsed.pickle file
        The .compiled.pickle file
    Create an <Xsd> object from the cached data
    ... which it then returns
    """

    XsdSource = xsd.XsdSource(xsd_path) # bs4 will still parse it
    XsdParser = xsd.XsdParser(XsdSource)
    XsdCompiler = xsd.XsdCompiler(XsdParser, _parsed=parsed)
    Xsd = xsd.Xsd \
    (
        xsd_path,
        _compiled = compiled,
        _XsdSource = XsdSource,
        _XsdParser = XsdParser,
        _XsdCompiler = XsdCompiler
    )

    return Xsd
