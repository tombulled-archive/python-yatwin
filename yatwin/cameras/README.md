# python-yatwin: /yatwin/cameras/

### Example: BaseCamera

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

### Example: BaseHackedYatwin

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
