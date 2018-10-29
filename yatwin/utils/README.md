# python-yatwin: /yatwin/utils/

## Contents:
* [chunk](#example-chunk)
* [disect_url](#example-disect_url)
* [get_external_ip](#example-get_external_ip)
* [scan_port](#example-scan_port)

### Example: chunk
```python
>>> from yatwin.utils import chunk
>>> from pprint import pprint
>>> 
>>> # Create a list
>>> some_list = list(range(10))
>>> some_list
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>
>>> # Chunk the list into blocks of 2
>>> chunked = chunk(some_list, 2)
>>> list(chunked)
[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
>>> 
```

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

### Example: get_external_ip
```python
>>> from yatwin import utils
>>> 
>>> # Get your LAN's external (public) IP address
>>> # Note: This requires an internet connection
>>> external_ip = utils.get_external_ip()
>>> external_ip
'86.184.83.27'
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
