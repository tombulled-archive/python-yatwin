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

    dumped_parsed = {}
    dumped_compiled = {}

    for WSDL in WSDLS:
        wsdl = Wsdl(WSDL)

        wsdl_name = wsdl.WsdlSource._file_name

        parsed = wsdl.WsdlCompiler.parsed
        compiled = wsdl.compiled

        directory = os.path.dirname(WSDL)
        filename = os.path.basename(WSDL)

        path_parsed = directory + '\\cache\\' + filename + '.parsed.pickle'
        path_compiled = directory + '\\cache\\' + filename + '.compiled.pickle'

        with open(path_parsed, 'wb') as file_parsed:
            pickle.dump(parsed, file_parsed, pickle.HIGHEST_PROTOCOL)

        with open(path_compiled, 'wb') as file_compiled:
            pickle.dump(compiled, file_compiled, pickle.HIGHEST_PROTOCOL)

        dumped_parsed[wsdl_name] = path_parsed
        dumped_compiled[wsdl_name] = path_compiled

    data = \
    {
        'parsed': dumped_parsed,
        'compiled': dumped_compiled,
    }

    return data
