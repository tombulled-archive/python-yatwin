# python-yatwin: /yatwin/interfaces/icmp/

## Contents:
* [decorators.kwarg_or_attr](#example-decoratorskwarg_or_attr)
* [icmp.Icmp](#example-icmpicmp)
* [wincmdping.ping](#example-wincmdpingping)

### Example: decorators.kwarg_or_attr
```python
>>> from yatwin.interfaces.icmp import decorators
>>> 
>>> # Create a class with a method decorated by @decorators.kwarg_or_attr
>>> class MyClass(object):
	def __init__(self, x = 1):
		self.x = x
		
	@decorators.kwarg_or_attr('x', not_in=(None,))
	def some_method(self, x = None):
		return x

>>> # Create a class instance
>>> my_class = MyClass()
>>>
>>> # Check the value of the class attribute 'x'
>>> my_class.x
1
>>> 
>>> # Call the method with no kwargs (it will use the class attribute for 'x')
>>> my_class.some_method()
1
>>> # Delete the class attribute
>>> del my_class.x
>>>
>>> # Try to call the method with no kwargs again (this time no class attribute exists, so an exception is raised)
>>> my_class.some_method()
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    my_class.some_method()
  File "C:\Users\Admin\Documents\GitHub\python-yatwin\yatwin\interfaces\icmp\decorators.py", line 39, in wrapper
    raise TypeError(f'Missing kwarg/attr: \'{key}\'')
TypeError: Missing kwarg/attr: 'x'
>>> 
>>> # Call the method with 'x' as a kwarg
>>> my_class.some_method(x = 3)
3
>>> 
```

### Example: icmp.Icmp
```python
>>> from yatwin.interfaces import Icmp
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> 
>>> # Create an Icmp instance
>>> icmp = Icmp(HOST)
>>> 
>>> # Ping the host to see if it's up (Boolean response)
>>> icmp.ping()
True
>>> 
>>> # Raw ping the host (see the commands stdout)
>>> print(icmp.ping_raw())
Pinging 192.168.1.227 with 32 bytes of data:
Reply from 192.168.1.227: bytes=32 time=3ms TTL=64

Ping statistics for 192.168.1.227:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 3ms, Maximum = 3ms, Average = 3ms
>>> 
```

### Example: wincmdping.ping
```python
>>> from yatwin.interfaces.icmp.wincmdping import ping
>>> from pprint import pprint
>>> 
>>> # Pick an IP
>>> HOST = '192.168.1.227'
>>> 
>>> # Ping the IP and parse the commands stdout
>>> pinged = ping(HOST, raw = False)
>>> pprint(pinged)
{'Pinging': {'Bytes': '32', 'IP': '192.168.1.227'},
 'Raw': 'Pinging 192.168.1.227 with 32 bytes of data:\r\n'
        'Reply from 192.168.1.227: bytes=32 time=6ms TTL=64\r\n'
        '\r\n'
        'Ping statistics for 192.168.1.227:\r\n'
        '    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),\r\n'
        'Approximate round trip times in milli-seconds:\r\n'
        '    Minimum = 6ms, Maximum = 6ms, Average = 6ms',
 'Replies': [{'Bytes': '32',
              'From': '192.168.1.227',
              'TTL': '64',
              'Time': '6'}],
 'Statistics': {'Packets': {'Loss': '0',
                            'Lost': '0',
                            'Received': '1',
                            'Sent': '1'}},
 'Times': {'Average': '6', 'Maximum': '6', 'Minimum': '6'}}
>>> 
>>> # Ping the IP and **don't** parse the commands stdout
>>> pinged = ping(HOST, raw = True)
>>> print(pinged)

Pinging 192.168.1.227 with 32 bytes of data:
Reply from 192.168.1.227: bytes=32 time=3ms TTL=64

Ping statistics for 192.168.1.227:
    Packets: Sent = 1, Received = 1, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
    Minimum = 3ms, Maximum = 3ms, Average = 3ms

>>> 
```
