# python-yatwin: /yatwin/interfaces/http/methods/method_types/

## Contents:
* [Audiostream](#example-audiostream)
* [BaseMethod](#example-basemethod)
* [DictMethod](#example-dictmethod)
* [Livestream](#example-livestream)
* [ParamMethod](#example-parammethod)
* [Snapshot](#example-snapshot)
* [Videostream](#example-videostream)
* [@decorators.kwarg_or_attr](#example-decoratorskwarg_or_attr)

### Example: Audiostream
```python
>>> from yatwin.interfaces.http.methods.method_types import Audiostream
>>> 
>>> # Method information
>>> ENDPOINT = 'audiostream.cgi'
>>> DESCRIPTION = 'request video communication'
>>> #...
>>> 
>>> # Create an Audiostream instance
>>> audio_stream = Audiostream \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> audio_stream
<Audiostream(audiostream.cgi)>
>>> 
>>> # If you have a <Http> instance, for example 'http', you could do:
>>> # audio_stream(http = http).play_stream()
>>> 
```

### Example: BaseMethod
```python
>>> from yatwin.interfaces.http.methods.method_types import BaseMethod
>>> 
>>> # Method information
>>> ENDPOINT = 'audiostream.cgi'
>>> DESCRIPTION = 'request video communication'
>>> #...
>>> 
>>> # Create a BaseMethod instance
>>> base_method = BaseMethod \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> base_method
<BaseMethod(audiostream.cgi)>
>>> 
>>> # If you have a <Http> instance, for example 'http', you can do:
>>> # base_method.get(http = http, loginuse='admin', ...)
>>> 
```

### Example: DictMethod
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> 
>>> from yatwin.interfaces.http.methods.method_types import DictMethod
>>> from pprint import pprint
>>> 
>>> # Method information
>>> ENDPOINT = 'login.cgi'
>>> DESCRIPTION = 'get the IE login latest user name, password and privileges'
>>> 
>>> # Create a DictMethod instance
>>> login = DictMethod \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> login
<DictMethod(login.cgi)>
>>>
>>> # Call the method
>>> pprint(login(http = http))
{'loginpass': '888888', 'loginuser': 'admin', 'pri': 255}
>>> 
```

### Example: Livestream
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> 
>>> from yatwin.interfaces.http.methods.method_types import Livestream
>>> 
>>> # Method information
>>> ENDPOINT = 'livestream.cgi'
>>> DESCRIPTION = 'ask video communication'
>>> # ...
>>>
>>> # Create a Livestream instance
>>> livestream = Livestream \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> livestream
<Livestream(livestream.cgi)>
>>> 
>>> livestream.download_video(http = http, file = '20180914074626_010.h264')
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\video.mp4'
>>> 
```

### Example: ParamMethod
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> 
>>> from yatwin.interfaces.http.methods.method_types import ParamMethod
>>> from pprint import pprint
>>> 
>>> # Method information
>>> ENDPOINT = 'get_rtsp.cgi'
>>> DESCRIPTION = 'get RTSP related parameters'
>>> # ...
>>> 
>>> # Create a ParamMethod instance
>>> get_rtsp = ParamMethod \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> get_rtsp
<ParamMethod(get_rtsp.cgi)>
>>> 
>>> pprint(get_rtsp(http = http))
{<SystemParam(rtspport)>: 10554,
 <SystemParam(rtsppwd)>: '888888',
 <SystemParam(rtspuser)>: 'admin',
 <SystemParam(rtsp_auth_enable)>: 1}
>>> 
```

### Example: Snapshot
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> 
>>> from yatwin.interfaces.http.methods.method_types import Snapshot
>>> 
>>> # Method information
>>> ENDPOINT = 'snapshot.cgi'
>>> DESCRIPTION = 'snapshot'
>>> # ...
>>> 
>>> # Create a Snapshot instance
>>> snapshot = Snapshot \
(
	http = http,
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> snapshot
<Snapshot(snapshot.cgi)>
>>> 
>>> # Call some methods
>>> snapshot.download_snapshot()
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.jpg'
>>>
>>> snapshot.view_snapshot()
>>> 
```

### Example: Videostream
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> 
>>> from yatwin.interfaces.http.methods.method_types import Videostream
>>> 
>>> # Method information
>>> ENDPOINT = 'videostream.cgi'
>>> DESCRIPTION = 'start firefox and non-IE browser kernel streaming video request Push'
>>> # ...
>>> 
>>> # Create a Videostream instance
>>> videostream = Videostream \
(
	http = http,
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> videostream
<Videostream(videostream.cgi)>
>>> 
>>> # Call some methods
>>> try:
	videostream.view_video()
except KeyboardInterrupt:
	pass

>>> # ...
>>>
```

### Example: @decorators.kwarg_or_attr
```python
>>> from yatwin.interfaces.http.methods.method_types import decorators
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
>>> 
>>> # Delete the class attribute
>>> del my_class.x
>>> 
>>> # Try to call the method with no kwargs again (this time no class attribute exists, so an exception is raised)
>>> my_class.some_method()
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    my_class.some_method()
  File "C:\Users\Admin\Documents\GitHub\python-yatwin\yatwin\interfaces\http\methods\method_types\decorators.py", line 40, in wrapper
    raise TypeError(f'Missing kwarg/attr: \'{key}\'')
TypeError: Missing kwarg/attr: 'x'
>>> 
>>> # Call the method with 'x' as a kwarg
>>> my_class.some_method(x = 3)
3
>>> 
```
