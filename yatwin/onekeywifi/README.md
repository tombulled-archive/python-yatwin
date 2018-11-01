# python-yatwin: /yatwin/onekeywifi/

## Contents:
* [OneKeyWifi.OneKeyWifi](#example-onekeywifionekeywifi)

### Example: OneKeyWifi.OneKeyWifi
```python
>>> from yatwin.onekeywifi import OneKeyWifi
>>> from pprint import pprint
>>> 
>>> # Create a OneKeyWifi instance
>>> onekeywifi = OneKeyWifi()
>>> onekeywifi
<OneKeyWifi()>
>>> 
>>> # Get the current interface
>>> interface = onekeywifi.get_interface()
>>> pprint(interface)
{'Authentication': 'WPA2-Personal',
 'Bssid': 'AB:CD:EF:AB:CD:EF',
 'Channel': '4',
 'Cipher': 'CCMP',
 'ConnectionMode': 'Auto Connect',
 'Description': 'Marvell AVASTAR Wireless-AC Network Controller',
 'Guid': 'e418db5f-5301-4b99-81f0-e0c213dc360a',
 'Name': 'WiFi',
 'NetworkType': 'Infrastructure',
 'PhysicalAddress': 'AB:CD:EF:AB:CD:EF',
 'Profile': 'SomeSSID',
 'RadioType': '802.11n',
 'ReceiveRate': '151',
 'Signal': '99%',
 'Ssid': 'SomeSSID',
 'State': 'connected',
 'TransmitRate': '151'}
>>> 
>>> # Get the BSSID of the network this device is connected to
>>> bssid = interface['Bssid'].upper()
>>> bssid
'AB:CD:EF:AB:CD:EF'
>>> 
>>> # Encode some data
>>> encoded = onekeywifi.encode(bssid, 'Ybrb')
>>> encoded
[8300, 6500, 6900, 9100, 9300, 9500, 9700, 9100, 7900, 6900, 8900, 8700, 9300, 8900, 7300, 9300, 9700, 8500, 10100, 8300]
>>> 
>>> # Play that data
>>> onekeywifi.play(encoded, play_count = 1)
>>> 
>>> # Decode that data
>>> decoded_bssid, decoded_psk = onekeywifi.decode(encoded, [bssid])
>>> decoded_bssid
'AB:CD:EF:AB:CD:EF'
>>> decoded_psk
'Ybrb'
>>> 
```
