# python-yatwin: /yatwin/interfaces/ftp/

## Contents:
* [constants](#example-constants)
* [decorators.keep_alive](#example-decoratorskeep_alive)
* [decorators.callback_store](#example-decoratorscallback_store)
* [errors](#example-errors)
* [ftp.Ftp](#example-ftpftp)

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

### Example: errors
```python
>>> from yatwin.interfaces.ftp import errors
>>> from pprint import pprint
>>>
>>> # See what error classes are available
>>> pprint([attr for attr in dir(errors) if not attr.startswith('_')])
['ConnectionRefusedError', 'LoginFailed', 'TimeoutError']
>>>
>>> # raise an error
>>> raise errors.LoginFailed('This is my error message')
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    raise errors.LoginFailed('This is my error message')
yatwin.interfaces.ftp.errors.LoginFailed: This is my error message
>>> 
```

### Example: ftp.Ftp
```python
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
>>> # Call some ftp methods
>>> print(ftp.pwd())
/
>>> print(ftp.ls())
drwxrwxr-x    2 1003     1003          1573 Apr 18  2017 bin
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 boot
drwxrwxrwt    5 vstarcam root          3400 Sep 14 06:27 dev
drwxrwxr-x    5 1003     1003           238 Apr 18  2017 etc
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 home
lrwxrwxrwx    1 1003     1003             9 Mar 13  2017 init -> sbin/init
drwxrwxr-x    3 1003     1003          1432 Apr 18  2017 lib
lrwxrwxrwx    1 1003     1003            11 Mar 13  2017 linuxrc -> bin/busybox
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 lost+found
-rwxrwxr-x    1 1003     1003          1341 Mar 13  2017 mkimg.rootfs
-rwxrwxr-x    1 1003     1003           431 Mar 13  2017 mknod_console
drwxrwxr-x    6 1003     1003            63 Mar 13  2017 mnt
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 nfsroot
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 opt
dr-xr-xr-x   62 vstarcam root             0 Jan  1  1970 proc
drwxrwxr-x    2 1003     1003            31 Apr 18  2017 root
drwxrwxr-x    2 1003     1003           893 Apr 18  2017 sbin
drwxrwxr-x    2 1003     1003             3 Mar 13  2017 share
dr-xr-xr-x   12 vstarcam root             0 Jan  1  1970 sys
drwxr-xr-x    7 vstarcam root             0 Jan  1  1970 system
drwxrwxrwt    2 vstarcam root           460 Sep 14 07:46 tmp
drwxrwxr-x    6 1003     1003            62 Mar 13  2017 usr
drwxrwxr-x    4 1003     1003            37 Mar 13  2017 var
>>> 
```
