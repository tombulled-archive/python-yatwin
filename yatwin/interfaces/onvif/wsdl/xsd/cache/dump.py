from ... import assets
from .. import Xsd
import os.path
import pickle

"""
Imports:
    ...assets
    ..Xsd
    os.path
    pickle

Contains:
    dump_all
"""

def dump_all():
    """
    Dumps a cached pickle of each xsd from ...assets.XSDS
    ... into assets/cache/

    These files have extensions:
        .parsed.pickle - The parsed xsd
        .compiled.pickle - The compiled xsd
    """

    dumped_parsed = {}
    dumped_compiled = {}

    for XSD in assets.XSDS:
        xsd = Xsd(XSD)

        xsd_name = xsd.XsdSource._file_name

        parsed = xsd.XsdCompiler.parsed
        compiled = xsd.compiled

        directory = os.path.dirname(XSD)
        filename = os.path.basename(XSD)

        path_parsed = directory + '\\cache\\' + filename + '.parsed.pickle'
        path_compiled = directory + '\\cache\\' + filename + '.compiled.pickle'

        with open(path_parsed, 'wb') as file_parsed:
            pickle.dump(parsed, file_parsed, pickle.HIGHEST_PROTOCOL)

        with open(path_compiled, 'wb') as file_compiled:
            pickle.dump(compiled, file_compiled, pickle.HIGHEST_PROTOCOL)

        dumped_parsed[xsd_name] = path_parsed
        dumped_compiled[xsd_name] = path_compiled

    data = \
    {
        'parsed': dumped_parsed,
        'compiled': dumped_compiled,
    }

    return data
