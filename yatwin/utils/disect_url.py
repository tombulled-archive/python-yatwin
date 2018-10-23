import re

"""
Contains:
    disect_url

Imports:
    re
"""

def disect_url(url):
    """
    'url' must be in the format:
        {protocol}://[{username}:{password}@]{ip}[:{port}]/[{endpoint}]

    returns:
        {
            'Protocol': protocol,
            'Username': username,
            'Password': password,
            'IP': ip,
            'Port': port,
            'Endpoint': endpoint,
            'RawURL': url,
        }
    """

    raw_url = url.strip()

    if raw_url.count('/') < 3:
        raw_url += '/'

    regexp_url = \
    (
        r'(?P<protocol>.+?)://'
        r'(?:(?P<username>.+?):(?P<password>.+?)@)?'
        r'(?P<ip>.+?)(?::(?P<port>.+?))?/(?P<endpoint>.*)'
    )

    re_match = re.search(regexp_url, raw_url)

    if re_match is None:
        return {'Raw URL': raw_url}

    data = \
    {
        'Protocol': re_match.group('protocol'),
        'Username': re_match.group('username'),
        'Password': re_match.group('password'),
        'IP': re_match.group('ip'), # Make me 'Host'
        'Port': re_match.group('port'), # int() ?
        'Endpoint': re_match.group('endpoint'), # Decode get params?
        'Raw URL': raw_url
    }

    return data
