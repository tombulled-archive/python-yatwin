# python-yatwin: /yatwin/interfaces/telnet

## Contents:
* [constants](#example-constants)
* [decorators.keep_alive](#example-decoratorskeep_alive)
* [errors](#example-errors)
* [telnet.Telnet](#example-telnettelnet)

### Example: constants
```python
>>> from yatwin.interfaces.telnet import constants
>>> from pprint import pprint
>>> 
>>> # See the constants available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_')])
['COMMAND_CD',
 'COMMAND_EXIT',
 'COMMAND_LS',
 'COMMAND_PS',
 'COMMAND_PWD',
 'COMMAND_TOP',
 'COMMAND_WHOAMI',
 'CONTROL_C',
 'CRLF',
 'DEFAULT_PASSWORD',
 'DEFAULT_PORT',
 'DEFAULT_USERNAME',
 'EXECUTION_MODE',
 'EXECUTION_MODE_BASIC',
 'EXECUTION_MODE_HASH',
 'FILE_FTP_TEST',
 'FILE_STARTUP',
 'FLAG_LOGIN',
 'FLAG_LOGIN_FAILED',
 'FLAG_PASSWORD',
 'FLAG_PROMPT',
 'HASH_BITS',
 'KNOWN_LOGINS',
 'LF',
 'TIMEOUT_GENERAL',
 'TIMEOUT_LOGIN']
>>> 
>>> # Get a constants value
>>> constants.DEFAULT_USERNAME
'vstarcam2017'
>>> 
>>> # Change a constants value
>>> constants.DEFAULT_USERNAME = 'vstarcam2015'
>>> 
>>> # Prove it changed
>>> constants.DEFAULT_USERNAME
'vstarcam2015'
>>> 
```

### Example: decorators.keep_alive
```python
>>> from yatwin.interfaces.telnet import decorators
>>> from yatwin.interfaces import Telnet
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> TELNET_USERNAME = 'vstarcam2017'
>>> TELNET_PASSWORD = '20170912'
>>> TELNET_PORT = 23
>>> 
>>> # Create a Telnet instance
>>> telnet = Telnet \
(
	HOST,
	username = TELNET_USERNAME,
	password = TELNET_PASSWORD,
	port = TELNET_PORT,
)
>>> telnet
<Telnet(vstarcam2017:20170912@192.168.1.227:23)>
>>>
>>> # Create a method with @decorators.keep_alive
>>> @decorators.keep_alive
def ls(cls, *args, **kwargs):
	cls.Telnet.write(b'ls\n')
	raw_resp = cls.Telnet.read_until(b'\r\n# ')
	return raw_resp.decode()
  
>>>
>>> # Check it works
>>> print(ls(telnet))
ls
[1;34mbin[0m            [1;36minit[0m           [1;32mmknod_console[0m  [1;34mroot[0m           [1;34mtmp[0m
[1;34mboot[0m           [1;34mlib[0m            [1;34mmnt[0m            [1;34msbin[0m           [1;34musr[0m
[1;34mdev[0m            [1;36mlinuxrc[0m        [1;34mnfsroot[0m        [1;34mshare[0m          [1;34mvar[0m
[1;34metc[0m            [1;34mlost+found[0m     [1;34mopt[0m            [1;34msys[0m
[1;34mhome[0m           [1;32mmkimg.rootfs[0m   [1;34mproc[0m           [1;34msystem[0m
# 
>>> 
```

### Example: errors
```python
>>> from yatwin.interfaces.telnet import errors
>>> from pprint import pprint
>>> 
>>> # See the error classes that are available
>>> pprint([attr for attr in dir(errors) if not attr.startswith('_')])
['ConnectionRefusedError',
 'InvalidExecutionMode',
 'LoginFailed',
 'TimeoutError']
>>> 
>>> # Raise an error
>>> raise errors.LoginFailed('My error message')
Traceback (most recent call last):
  File "<pyshell#317>", line 1, in <module>
    raise errors.LoginFailed('My error message')
yatwin.interfaces.telnet.errors.LoginFailed: My error message
>>> 
```

### Example: telnet.Telnet
```python
>>> from yatwin.interfaces import Telnet
>>> 
>>> # Camera information
>>> HOST = '192.168.1.227'
>>> TELNET_USERNAME = 'vstarcam2017'
>>> TELNET_PASSWORD = '20170912'
>>> TELNET_PORT = 23
>>> 
>>> # Create a Telnet instance
>>> telnet = Telnet \
(
	HOST,
	username = TELNET_USERNAME,
	password = TELNET_PASSWORD,
	port = TELNET_PORT,
)
>>> telnet
<Telnet(vstarcam2017:20170912@192.168.1.227:23)>
>>>
>>> # Use some built-in telnet methods:
>>> print(telnet.ls())
bin            init           mknod_console  root           tmp
boot           lib            mnt            sbin           usr
dev            linuxrc        nfsroot        share          var
etc            lost+found     opt            sys
home           mkimg.rootfs   proc           system
>>> print(telnet.top())
Mem: 30500K used, 6680K free, 0K shrd, 584K buff, 7028K cached
CPU: 23.0% usr  7.6% sys  0.0% nic 69.2% idle  0.0% io  0.0% irq  0.0% sirq
Load average: 9.87 10.53 10.41 2/149 16418
  PID  PPID USER     STAT   VSZ %MEM CPU %CPU COMMAND
  612     1 vstarcam S     353m971.5   0 24.6 /system/system/bin/encoder
16418 14773 vstarcam R     1708  4.5   0  6.1 top -n 1
  562     1 vstarcam S     7700 20.6   0  0.0 /system/system/bin/wifidaemon
  548     1 vstarcam S     1716  4.6   0  0.0 telnetd
 5635   548 vstarcam S     1716  4.6   0  0.0 -sh
14773   548 vstarcam S     1716  4.6   0  0.0 -sh
 5692  5635 vstarcam S     1716  4.6   0  0.0 tcpsvd -vE 0.0.0.0 21 ftpd /
14636   548 vstarcam S     1712  4.6   0  0.0 -sh
14671   548 vstarcam S     1712  4.6   0  0.0 -sh
  565     1 vstarcam S     1708  4.5   0  0.0 /sbin/getty -L ttyS000 115200 vt10
    1     0 vstarcam S     1704  4.5   0  0.0 init
  531     1 vstarcam S <    868  2.3   0  0.0 udevd --daemon
 1001     2 vstarcam SW       0  0.0   0  0.0 [RtmpMlmeTask]
 1000     2 vstarcam SW       0  0.0   0  0.0 [RtmpTimerTask]
    3     2 vstarcam SW       0  0.0   0  0.0 [ksoftirqd/0]
  263     2 vstarcam SW       0  0.0   0  0.0 [kworker/0:1]
  535     2 vstarcam SW       0  0.0   0  0.0 [mmcqd/1]
  424     2 vstarcam SW       0  0.0   0  0.0 [mtdblock2]
  545     2 vstarcam SWN      0  0.0   0  0.0 [jffs2_gcd_mtd3]
  561     2 vstarcam SW       0  0.0   0  0.0 [flush-179:0]#
>>> 
>>> # Execute custom commands
>>> print(telnet.execute('echo "I hear an echo"'))
I hear an echo
>>> print(telnet.execute('echo "some data" > /tmp/_'))

>>> print(telnet.execute('cat /tmp/_'))
some data
>>> 
```
