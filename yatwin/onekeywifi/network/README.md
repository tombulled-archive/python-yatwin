# python-yatwin: /yatwin/onekeywifi/network/

## Contents:
* [NetworkScanner.NetworkScanner](#example-networkscannernetworkscanner)

### Example: NetworkScanner.NetworkScanner
```python
>>> from yatwin.onekeywifi import NetworkScanner
>>> from pprint import pprint
>>> 
>>> # Create a NetworkScanner instance
>>> network_scanner = NetworkScanner()
>>> 
>>> # Get networks
>>> networks = network_scanner.get_networks()
>>> pprint(networks)
{'SomeSSID': ['91:4E:4B:01:FF:A4']}
>>> 
>>> # Pick a bssid
>>> bssid = networks['SomeSSID'][0]
>>> bssid
'91:4E:4B:01:FF:A4'
>>> 
>>> # Get the current interface
>>> interface = network_scanner.get_interface()
>>> pprint(interface)
{'Authentication': 'WPA2-Personal',
 'Bssid': '91:4e:4b:01:ff:a4',
 'Channel': '5',
 'Cipher': 'CCMP',
 'ConnectionMode': 'Auto Connect',
 'Description': 'Marvell AVASTAR Wireless-AC Network Controller',
 'Guid': 'f418db6f-5901-4b94-92f1-e0f204bc470d',
 'Name': 'WiFi',
 'NetworkType': 'Infrastructure',
 'PhysicalAddress': 'ec:85:91:f2:83:64',
 'Profile': 'SomeSSID',
 'RadioType': '802.11n',
 'ReceiveRate': '146',
 'Signal': '88%',
 'Ssid': 'SomeSSID',
 'State': 'connected',
 'TransmitRate': '146'}
>>> 
>>> # Get the current bssid
>>> current_bssid = interface['Bssid']
>>> current_bssid
'91:4e:4b:01:ff:a4'
```
