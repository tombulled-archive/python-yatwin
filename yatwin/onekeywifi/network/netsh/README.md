# python-yatwin: /yatwin/onekeywifi/network/netsh/

## Contents:
* [constants](#example-constants)
* [Netsh.Netsh](#example-netshnetsh)
* [utils.cmd_exec_subprocess](#example-utilscmd_exec_subprocess)

### Example: constants
```python
>>> from yatwin.onekeywifi.network.netsh import constants
>>> from pprint import pprint
>>> 
>>> # See what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_')])
['CREATE_NO_WINDOW']
>>> 
>>> # Pick a constant
>>> CREATE_NO_WINDOW = constants.CREATE_NO_WINDOW
>>> CREATE_NO_WINDOW
134217728
>>> 
>>> # Import a constant
>>> from yatwin.onekeywifi.network.netsh.constants import CREATE_NO_WINDOW
>>> 
>>> # Change a constants value
>>> constants.CREATE_NO_WINDOW = 'New Value'
>>> constants.CREATE_NO_WINDOW
'New Value'
>>> 
>>> # Create a new constant
>>> constants.FOO_BAR = 'Value'
>>> constants.FOO_BAR
'Value'
>>> 
```


### Example: Netsh.Netsh
```python
>>> from yatwin.onekeywifi.network.netsh import Netsh
>>> from pprint import pprint
>>> 
>>> # Create a Netsh instance
>>> netsh = Netsh()
>>> 
>>> # Get networks
>>> pprint(netsh.get_networks())
[{'Authentication': 'WPA2-Personal',
  'BSSIDs': [{'BSSID': '76:ee:f1:eb:be:9c',
              'BasicRates': '1 2 5.5 11',
              'Channel': '4',
              'OtherRates': '6 9 12 18 24 36 48 54',
              'RadioType': '802.11n',
              'Signal': '86%'}],
  'Encryption': 'CCMP',
  'NetworkType': 'Infrastructure',
  'SSID': 'BTHub6-MRH3'}]
>>> 
>>> # Get interfaces
>>> pprint(netsh.get_interfaces())
({'Authentication': 'WPA2-Personal',
  'BSSID': '54:df:d1:be:bf:9b',
  'Channel': '4',
  'Cipher': 'CCMP',
  'Connection mode': 'Auto Connect',
  'Description': 'Marvell AVASTAR Wireless-AC Network Controller',
  'GUID': 'e407da4e-4808-4c96-82e0-e1b204bc450e',
  'Name': 'WiFi',
  'Network type': 'Infrastructure',
  'Physical address': 'be:84:81:e1:86:72',
  'Profile': 'SomeSSID',
  'Radio type': '802.11n',
  'Receive rate (Mbps)': '148',
  'SSID': 'SomeSSID',
  'Signal': '91%',
  'State': 'connected',
  'Transmit rate (Mbps)': '148'},)
>>> 
```


### Example: utils.cmd_exec_subprocess
```python
>>> from yatwin.onekeywifi.network.netsh import utils
>>> 
>>> # Command information
>>> COMMAND = 'netsh wlan show networks mode=bssid'
>>> 
>>> # Execute the command
>>> raw_stdout = utils.cmd_exec_subprocess(COMMAND)
>>> 
>>> # View the commands stdout
>>> print(raw_stdout)

Interface name : WiFi 
There are 1 networks currently visible. 

SSID 1 : SomeSSID
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP 
    BSSID 1                 : 84:fd:e1:df:cd:1b
         Signal             : 88%  
         Radio type         : 802.11n
         Channel            : 4 
         Basic rates (Mbps) : 1 2 5.5 11
         Other rates (Mbps) : 6 9 12 18 24 36 48 54


>>> 
```
