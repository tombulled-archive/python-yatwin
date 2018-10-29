# python-yatwin: /yatwin/interfaces/ftp/

## Contents:
* [constants](#example-constants)
* [decorators.keep_alive](#example-decoratorskeep_alive)
* [decorators.callback_store](#example-decoratorscallback_store)

### Example: constants
```python
>>> from yatwin.interfaces.ftp import constants
>>> from pprint import pprint
>>> 
>>> # Have a look at what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()])
['COMMAND_HELP',
 'COMMAND_LIST',
 'COMMAND_RETR',
 'COMMAND_STOR',
 'DEFAULT_PASSWORD',
 'DEFAULT_PORT',
 'DEFAULT_USERNAME',
 'STATUS_CODE_OPERATION_SUCCESSFUL',
 'TIMEOUT']
>>> 
>>> # Get a constants value
>>> constants.DEFAULT_PORT
21
>>> 
>>> # Change a constants value
>>> constants.TIMEOUT = 4
>>> 
```

### Example: @decorators.keep_alive
```python
>>> from yatwin.interfaces.ftp import decorators
>>> from yatwin.interfaces import Ftp
>>> from time import sleep
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> FTP_USERNAME = ''
>>> FTP_PASSWORD = ''
>>> FTP_PORT = 21
>>> 
>>> # Create an Ftp instance
>>> ftp = Ftp(HOST, username = FTP_USERNAME, password = FTP_PASSWORD, port = FTP_PORT)
>>> ftp
<Ftp(:@192.168.1.227:21)>
>>>
>>> # Create a non-decorated method (*not* kept alive)
>>> def PWD_not_kept_alive(cls, *args, **kwargs):
	return cls.FTP.pwd(*args, **kwargs)

>>> # Create a decorated method (kept alive)
>>> @decorators.keep_alive
def PWD_kept_alive(cls, *args, **kwargs):
	return cls.FTP.pwd(*args, **kwargs)

>>> # Make the Ftp session timeout
>>> # Note: 3 minutes feels like forever if you're sitting waiting for it to timeout
>>> sleep(180)
>>>
>>> # Attempt to execute PWD without using @decorators.keep_alive
>>> print(PWD_not_kept_alive(ftp))
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    print(ftp.PWD_not_kept_alive(ftp))
  File "<pyshell#80>", line 2, in PWD_not_kept_alive
    return cls.FTP.pwd(*args, **kwargs)
  File "C:\Program Files\Python36\lib\ftplib.py", line 656, in pwd
    resp = self.voidcmd('PWD')
  File "C:\Program Files\Python36\lib\ftplib.py", line 278, in voidcmd
    return self.voidresp()
  File "C:\Program Files\Python36\lib\ftplib.py", line 251, in voidresp
    resp = self.getresp()
  File "C:\Program Files\Python36\lib\ftplib.py", line 244, in getresp
    raise error_temp(resp)
ftplib.error_temp: 421 Timeout
>>>
>>> # Attempt to execute PWD ***with*** using @decorators.keep_alive
>>> print(ftp.PWD_kept_alive(ftp))
/
>>> 
```

### Example: @decorators.callback_store
```python
>>> from yatwin.interfaces.ftp import decorators
>>> from yatwin.interfaces.ftp import constants
>>> from yatwin.interfaces import Ftp
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> FTP_USERNAME = ''
>>> FTP_PASSWORD = ''
>>> FTP_PORT = 21
>>> 
>>> # Create an Ftp instance
>>> ftp = Ftp(HOST, username = FTP_USERNAME, password = FTP_PASSWORD, port = FTP_PORT)
>>> ftp
<Ftp(:@192.168.1.227:21)>
>>>
>>> # Create a decorated method
>>> @decorators.callback_store
def LIST(cls, *args, **kwargs):
	return cls.FTP.retrlines('LIST /', *args, **kwargs)
  
>>> # Call the decorated method
>>> print(LIST(ftp))
>>>
```
