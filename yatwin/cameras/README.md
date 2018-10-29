# python-yatwin: /yatwin/cameras/

## Contents:
* [BaseCamera.BaseCamera](#example-basecamerabasecamera)
* [BaseHackedYatwin.BaseHackedYatwin](#example-basehackedyatwinbasehackedyatwin)
* [decorators.try_except](#example-decoratorstry_except)
* [utils.create_service](#example-utilscreate_service)

### Example: BaseCamera.BaseCamera

```python
>>> from yatwin.cameras import BaseCamera
>>>
>>> # Cameras IP Address
>>> HOST = '192.168.1.223'
>>>
>>> # Create the BaseCamera instance
>>> cam = BaseCamera(HOST)
>>>
>>> # Some services are auto-built
>>> cam.multicast
<Multicast()>
>>> cam.icmp
<Icmp(192.168.1.223)>
>>>
>>> # Other services need to be created manually
>>> cam.http = cam.create_http_service(HOST, username='admin', password='888888', port=80)
>>> cam.http
<Http(admin:888888@192.168.1.223:80)>
>>> 
```

### Example: BaseHackedYatwin.BaseHackedYatwin

```python
>>> from yatwin.cameras import BaseHackedYatwin
>>> 
>>> # Camera details
>>> HOST = '192.168.1.223'
>>> ONVIF_PORT = 10080 # Default Onvif port
>>> 
>>> # Create the BaseHackedYatwin instance
>>> # It will auto-hack as many interfaces as it can
>>> cam = BaseHackedYatwin(HOST, onvif_port = ONVIF_PORT)
>>> cam
<BaseHackedYatwin
(
	http:      <Http(admin:888888@192.168.1.223:80)>
	icmp:      <Icmp(192.168.1.223)>
	onvif:     <Onvif(admin:888888@192.168.1.223:10080)>
	telnet:    <Telnet(vstarcam2017:20170912@192.168.1.223:23)>
	ftp:       None
	multicast: <Multicast()>
	imap:      None
	rtsp:      <Rtsp(admin:888888@192.168.1.223:10554)[udp/av1_0]>
)>
>>> 
>>> # Access some interfaces
>>> cam.telnet
<Telnet(vstarcam2017:20170912@192.168.1.223:23)>
>>> print(cam.telnet.execute('echo "Telnet was auto-hacked"')
Telnet was auto-hacked
>>> 
```

### Example: decorators.try_except
```python
>>> from yatwin.cameras import decorators
>>> 
>>> # Create a decorated function
>>> @decorators.try_except('Some value')
def some_func(param = 1):
	return param / 0 # This will raise ZeroDivisionError('division by zero')

>>> some_func()
'Some value'
>>>
>>> # Prove it would have raised an exception
>>> 1 / 0
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    1 / 0
ZeroDivisionError: division by zero
>>> 
```

### Example: utils.create_service
```python
>>> from yatwin.interfaces import Http
>>> from yatwin.cameras import utils
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> USERNAME = 'admin'
>>> PASSWORD = '888888'
>>> PORT = 80
>>> 
>>> # Create a service creator for Http
>>> some_service_creator = utils.create_service(Http)
>>> 
>>> # Create a Http service instance using the service creator
>>> http = some_service_creator(HOST, username = USERNAME, password = PASSWORD, port = PORT)
>>> http
<Http(admin:888888@192.168.1.227:80)>
>>>
```
