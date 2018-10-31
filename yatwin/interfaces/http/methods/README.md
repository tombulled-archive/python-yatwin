# python-yatwin: /yatwin/interfaces/http/methods/

## Contents:
* [methods](#example-methods)

### Example: methods
```python
>>> # Create a Http instance, see Http documentation for more info
>>> from yatwin.interfaces import Http
>>> http = Http('192.168.1.227')
>>> http
<Http(admin:888888@192.168.1.227:80)>
>>> 
>>> from yatwin.interfaces.http import methods
>>> from pprint import pprint
>>> 
>>> # Get a method from METHODS
>>> get_rtsp = methods.METHODS.get('get_rtsp', None)
>>> get_rtsp
<ParamMethod(get_rtsp.cgi)>
>>> 
>>> # Import a method
>>> from yatwin.interfaces.http.methods import get_rtsp
>>> get_rtsp
<ParamMethod(get_rtsp.cgi)>
>>>
>>> # Example use of a method
>>> pprint(get_rtsp(http = http))
{<SystemParam(rtspport)>: 10554,
 <SystemParam(rtsppwd)>: '888888',
 <SystemParam(rtspuser)>: 'admin',
 <SystemParam(rtsp_auth_enable)>: 1}
>>>
>>> # Some methods behave differently
>>> snapshot = methods.snapshot
>>> snapshot
<Snapshot(snapshot.cgi)>
>>>
>>> snapshot() # Not supported, so returns None
>>> snapshot.download_snapshot()
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.jpg'
>>> 
```
