from .methods.utils import *

"""
Library containing utility functions for 'http'

Imports:
    .methods.utils.*

Contains:
    jstopy
    sprintf_cgi_overview
"""

def jstopy(http_resp):
    """
    Function to parse the JavaScript variables in 'http_resp'
    ... then return them as a dictionary
    """

    x = http_resp

    data = {}

    for line in x.split(';'):
        line = line.strip()

        if line.lower().startswith('var'):
            line = line[3:].strip()

        if not line:
            continue

        eq_index = line.index('=')

        key, val = line[:eq_index], line[eq_index+1:]

        key = key.strip()
        val = val.strip()

        plus = False

        if key.endswith('+'):
            plus = True
            key = key[:-1].strip()

        sub_keys = []

        if val.startswith('"') or val.startswith('\''):
            val = val[1:]

            if val.endswith('"') or val.endswith('\''):
                val = val[:-1]
        elif 'array' not in str(val).lower():
            val = int(val)

        if str(val).lower() in ('array()', 'new array()',):
            val = {}

        if '[' in key:
            key, *sub_keys = key.split('[')
            key = key.strip()
            
            sub_keys = [sk.strip().rstrip(']').strip() for sk in sub_keys]

        if sub_keys:
            if len(sub_keys) == 1:
                data[key][sub_keys[0]] = val

                continue
            #else...

        if not plus:
            data[key] = val
        else:
            data[key] += val

    return data

def sprintf_cgi_overview(cgi):
    """
    Returns a pretty printable version of the cgi in the form:
        endpoint: ...
        description: ...
        permission: ...
        method: ...
    """

    data = \
    (
        f'\tendpoint: {cgi.endpoint}\n'
        f'\tdescription: {cgi.description}\n'
        f'\tpermission: {cgi.permission}\n'
        #f'\tgrammar: {cgi.grammar}\n'
        #f'explained: {cgi.explained}\n'
        f'\tmethod: {cgi.method}\n'
    )

    data += '\tget_parameters:\n'

    for param in cgi.get_parameters:
        data += f'\t\t{param.identifier}: {param.description}\n'

    data += '\treturn parameters:\n'

    for param in cgi.returns:
        data += f'\t\t{param.identifier}: {param.description}\n'

    return data
