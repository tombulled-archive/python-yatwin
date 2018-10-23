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

    for XSD in assets.XSDS:
        xsd = Xsd(XSD)

        parsed = xsd.XsdCompiler.parsed
        compiled = xsd.compiled

        directory = os.path.dirname(XSD)
        filename = os.path.basename(XSD)

        with open(directory + '\\cache\\' + filename + '.parsed.pickle', 'wb') as file_parsed:
            pickle.dump(parsed, file_parsed, pickle.HIGHEST_PROTOCOL)

        with open(directory + '\\cache\\' + filename + '.compiled.pickle', 'wb') as file_compiled:
            pickle.dump(compiled, file_compiled, pickle.HIGHEST_PROTOCOL)
