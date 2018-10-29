# python-yatwin: /yatwin/interfaces/http/

## Contents:
* [constants](#example-constants)
* [http.Http](#example-httphttp)
* [response.HttpResponse](#example-responsehttpresponse)
* [utils.jstopy](#example-utilsjstopy)
* [utils.sprintf_cgi_overview](#example-utilssprintf_cgi_overview)

### Example: constants
```python
>>> from yatwin.interfaces.http import constants
>>> from pprint import pprint
>>> 
>>> # Have a look at what constants are available
>>> # Note: The results have been limited to the first 10 constants
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()][:10] + ['...'])
['ADMINISTRATOR',
 'AUTO_BUILD',
 'CENTER',
 'DEFAULT_PASSWORD',
 'DEFAULT_PORT',
 'DEFAULT_USERNAME',
 'GET',
 'HPATROL',
 'HPATROL_STOP',
 'IMPLEMENT_GET_AUTH',
 '...']
 >>>
>>> # Get a constants value
>>> constants.DEFAULT_PASSWORD
'888888'
>>> 
>>> # Change a constants value
>>> constants.DEFAULT_PORT = 81
>>> 
```

### Example: http.Http
```python
>>> from yatwin.interfaces import Http
>>> from pprint import pprint
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> USERNAME = 'admin'
>>> PASSWORD = '888888'
>>> PORT = 80
>>> 
>>> # Create a Http instance
>>> http = Http(HOST, username = USERNAME, password = PASSWORD, port = PORT)
>>> http
<Http(admin:888888@192.168.1.227:80)>
>>> 
>>> # Get a raw Http response (html)
>>> index = http.get('index.htm')
>>> index
<HttpResponse(http://admin:888888@192.168.1.227:80/index.htm?loginuse=admin&loginpas=888888)>
>>>
>>> # Call a method
>>> rtsp = http.get_rtsp()
>>> pprint(rtsp)
{<SystemParam(rtspport)>: 10554,
 <SystemParam(rtsppwd)>: '888888',
 <SystemParam(rtspuser)>: 'admin',
 <SystemParam(rtsp_auth_enable)>: 1}
>>>
>>> # Make a url, given an endpoint
>>> http._make_url('some_endpoint.ext')
'http://admin:888888@192.168.1.227:80/some_endpoint.ext?loginuse=admin&loginpas=888888'
>>> 
```

### Example: response.HttpResponse
```python
>>> from yatwin.interfaces import Http
>>> from pprint import pprint
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> USERNAME = 'admin'
>>> PASSWORD = '888888'
>>> PORT = 80
>>> 
>>> # Create a Http instance
>>> http = Http(HOST, username = USERNAME, password = PASSWORD, port = PORT)
>>> http
<Http(admin:888888@192.168.1.227:80)>
>>> 
>>> # Get a raw Http response (html)
>>> index = http.get('index.htm')
>>> index
<HttpResponse(http://admin:888888@192.168.1.227:80/index.htm?loginuse=admin&loginpas=888888)>
>>>
>>> # Parse the response as html
>>> html = index.parse_html()
>>> html
<html>
<head>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type"/>
<meta content="width=320; initial-scale=1.0; maximum-scale=2.0; user-scalable=1;" id="viewport" name="viewport">
<meta content="0" name="date"/>
<meta content="no-cache" http-equiv="pragma"/>
<meta content="no-cache, must-revalidate" http-equiv="Cache-Control"/>
<meta content="0" http-equiv="expires"/>
<title></title>
<script src="public.js"></script>
<script src="get_status.cgi"></script>
<script>
if (alias=='') alias=_anonymous; 
document.title=_device+'('+decodeURIComponent(alias)+')';
</script>
</meta></head>
<body oncontextmenu="return false" style="margin:0px 0px 0px 0px;background-color:#d8d8d8;"><iframe frameborder="0" height="100%" id="idx" marginheight="0" marginwidth="0" name="idx" scrolling="auto" src="login.htm" width="100%"></iframe></body>
<script>
var s=navigator.userAgent.toString();
if(s.indexOf("symbian")!=-1)
	main.src="pda.htm";
else
	main.src="login.htm";
</script>
</html>

>>> 
>>> # Get a javascript http response
>>> login_params = http.get('login.cgi')
>>> login_params
<HttpResponse(http://admin:888888@192.168.1.227:80/login.cgi?loginuse=admin&loginpas=888888)>
>>> 
>>> # Parse the response as javascript
>>> js = login_params.parse_js()
>>> pprint(js)
{'loginpass': '888888', 'loginuser': 'admin', 'pri': 255}
>>> 
```

### Example: utils.jstopy
```python
>>> from yatwin.interfaces.http import utils
>>> from pprint import pprint
>>> 
>>> # Make a list of JavaScript variables
>>> data = 'var some_key_1="some_val_1";var some_key_2=2;'
>>> 
>>> # Parse them into a Python dictionary
>>> parsed = utils.jstopy(data)
>>> pprint(parsed)
{'some_key_1': 'some_val_1', 'some_key_2': 2}
>>> 
```

### Example: utils.sprintf_cgi_overview
```python
>>> from yatwin.interfaces.http import utils
>>> from yatwin.interfaces.http import methods
>>>
>>> # Pick a HTTP method
>>> method = methods.METHODS['get_apwifi']
>>> method
<ParamMethod(get_apwifi.cgi)>
>>> 
>>> # Print the cgi overview
>>> print(utils.sprintf_cgi_overview(method))
	endpoint: get_apwifi.cgi
	description: get AP related parameter
	permission: ADMINISTRATOR
	method: GET
	get_parameters:
		loginuse: Current users username
		loginpas: Current users password
	return parameters:
		apwifi_encrypt: means AP encrypted authentication mode
		apswifi_port: AP port
		apwifi_key: encrypted string
		apwifi_ssid: WiFi AP SSID
		apwifi_ipaddr: WiFi IP address
		apwifi_mask: WiFi MASK
		apwifi_startip: WiFi start IP address
		apwifi_endip: WiFi ends IP address

>>> 
```
