import requests

"""
Imports:
    requests

Contains:
    get_external_ip
    _get_external_ip_httpbin
"""

def get_external_ip():
    return _get_external_ip_httpbin()

def _get_external_ip_httpbin():
    resp = requests.get('https://httpbin.org/ip')

    data = resp.json()

    return data.get('origin', None)
