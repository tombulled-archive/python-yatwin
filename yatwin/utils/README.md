# python-yatwin: /yatwin/utils/

### Example: disect_url
```python
>>> from yatwin.utils import disect_url
>>> from pprint import pprint
>>>
>>> # Pick a URL
>>> url = 'https://github.com/tombulled/python-yatwin'
>>>
>>> # Disect it
>>> disected_url = disect_url(url)
>>>
>>> # View the disected URL
>>> pprint(disected_url)
{'Endpoint': 'tombulled/python-yatwin',
 'IP': 'github.com',
 'Password': None,
 'Port': None,
 'Protocol': 'https',
 'Raw URL': 'https://github.com/tombulled/python-yatwin',
 'Username': None}
>>>
>>> # Pick a more interesting URL
>>> url = 'http://admin:888888@192.168.1.227:80/index.htm?loginuse=admin&loginpas=888888'
>>>
>>> # Disect it
>>> disected_url = disect_url(url)
>>>
>>> # View the disected URL
>>> pprint(disected_url)
{'Endpoint': 'index.htm?loginuse=admin&loginpas=888888',
 'IP': '192.168.1.227',
 'Password': '888888',
 'Port': '80',
 'Protocol': 'http',
 'Raw URL': 'http://admin:888888@192.168.1.227:80/index.htm?loginuse=admin&loginpas=888888',
 'Username': 'admin'}
>>> 
```

### Example: scan_port
```python
>>> from yatwin.utils import scan_port
>>>
>>> # Camera information
>>> HOST = '192.168.1.227'
>>>
>>> # Check to see if a port is open, e.g. port 80
>>> scan_port(HOST, 80)
True
>>>
>>> # Check to see if a different port is open, e.g. port 1612
>>> scan_port(HOST, 1612)
False
>>> 
```
