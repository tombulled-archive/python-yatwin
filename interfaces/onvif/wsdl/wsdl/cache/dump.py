from ...assets import WSDLS
from .. import Wsdl
import os.path
import pickle

"""
Imports:
    ...assets.WSDLS
    ..Wsdl
    os.path
    pickle

Contains:
    dump_all
"""

def dump_all():
    """
    Dumps a cached pickle of each wsdl from ...assets.WSDLS
    ... into assets/cache/

    These files have extensions:
        .parsed.pickle - The parsed wsdl
        .compiled.pickle - The compiled wsdl
    """

    for WSDL in WSDLS:
        wsdl = Wsdl(WSDL)

        parsed = wsdl.WsdlCompiler.parsed
        compiled = wsdl.compiled

        directory = os.path.dirname(WSDL)
        filename = os.path.basename(WSDL)

        with open(directory + '\\cache\\' + filename + '.parsed.pickle', 'wb') as file_parsed:
            pickle.dump(parsed, file_parsed, pickle.HIGHEST_PROTOCOL)

        with open(directory + '\\cache\\' + filename + '.compiled.pickle', 'wb') as file_compiled:
            pickle.dump(compiled, file_compiled, pickle.HIGHEST_PROTOCOL)
