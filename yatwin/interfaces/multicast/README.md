# python-yatwin: /yatwin/interfaces/multicast/

## Contents:
* [multicast.Multicast](#example-multicastmulticast)

### Example: multicast.Multicast
```python
>>> from yatwin.interfaces import Multicast
>>> from pprint import pprint
>>> 
>>> # Create a Multicast instance
>>> multicast = Multicast()
>>> multicast
<Multicast()>
>>> 
>>> # WSDD Discover using ws_discovery
>>> discovered = multicast.ws_discover()
>>> pprint(discovered)
[{'EPR': 'urn:uuid:813b12f7-45a0-11b6-8404-c156e3a2e429',
  'InstanceID': 0,
  'MetadataVersion': 1,
  'Scopes': [onvif://www.onvif.org/type/Network_Transmitter,
             onvif://www.onvif.org/type/video_encoder,
             onvif://www.onvif.org/type/ptz,
             onvif://www.onvif.org/type/audio_encoder,
             onvif://www.onvif.org/type/video_analytics,
             onvif://www.onvif.org/hardware/Vstarcam,
             onvif://www.onvif.org/name/Vstarcam,
             onvif://www.onvif.org/location/country/China,
             onvif://www.onvif.org/Profile/Streaming],
  'Types': [http://www.onvif.org/ver10/network/wsdl:NetworkVideoTransmitter],
  'XAddrs': ['http://192.168.1.236:10080/onvif/device_service'],
  '_Service': <yatwin.interfaces.multicast.ws_discovery.Service object at 0x0000024BA7763780>},
 {'EPR': 'urn:uuid:813b12f5-49a5-11b5-8414-28ad3b083022',
  'InstanceID': 0,
  'MetadataVersion': 1,
  'Scopes': [onvif://www.onvif.org/type/Network_Transmitter,
             onvif://www.onvif.org/type/video_encoder,
             onvif://www.onvif.org/type/ptz,
             onvif://www.onvif.org/type/audio_encoder,
             onvif://www.onvif.org/type/video_analytics,
             onvif://www.onvif.org/hardware/Vstarcam,
             onvif://www.onvif.org/name/Vstarcam,
             onvif://www.onvif.org/location/country/China,
             onvif://www.onvif.org/Profile/Streaming],
  'Types': [http://www.onvif.org/ver10/network/wsdl:NetworkVideoTransmitter],
  'XAddrs': ['http://192.168.1.227:10080/onvif/device_service'],
  '_Service': <yatwin.interfaces.multicast.ws_discovery.Service object at 0x0000024BA7747780>},
 {'EPR': 'urn:uuid:822b12e7-45a9-14b5-8404-27ad3e1e4a5c',
  'InstanceID': 0,
  'MetadataVersion': 1,
  'Scopes': [onvif://www.onvif.org/type/Network_Transmitter,
             onvif://www.onvif.org/type/video_encoder,
             onvif://www.onvif.org/type/ptz,
             onvif://www.onvif.org/type/audio_encoder,
             onvif://www.onvif.org/type/video_analytics,
             onvif://www.onvif.org/hardware/IP-camera,
             onvif://www.onvif.org/name/IP-camera,
             onvif://www.onvif.org/location/country/China,
             onvif://www.onvif.org/Profile/Streaming],
  'Types': [http://www.onvif.org/ver10/network/wsdl:NetworkVideoTransmitter],
  'XAddrs': ['http://192.168.1.235:10080/onvif/device_service'],
  '_Service': <yatwin.interfaces.multicast.ws_discovery.Service object at 0x0000024BA77587B8>}]
>>> 
>>> # WSDD Discover using nmap (--script=broadcast-wsdd-discover)
>>> discovered = multicast.broadcast_wsdd_discover_nmap()
>>> pprint(discovered)
{'Devices': [{'239.255.255.250': {'Address': 'http://192.168.1.236:10080/onvif/device_service',
                                  'Message id': '4abb38f0183696a-499e71d1-6f9cb671-580f223-6756e0bb22cb901d2fcbd09b',
                                  'Type': 'n:NetworkVideoTransmitter'}},
             {'239.255.255.250': {'Address': 'http://192.168.1.227:10080/onvif/device_service',
                                  'Message id': '124a675cd0794ae-58be84ff-49a58e1c-39c9e9-520c207618175cc216a67586',
                                  'Type': 'n:NetworkVideoTransmitter'}}],
 'WCF Services': [{'239.255.255.250': {'Address': 'http://192.168.1.235:10080/onvif/device_service',
                                       'Message id': '38b133d63698d25a-305d5175-18ac4770-7d506b7f-2a10c8b1116cc0b15dc9156',
                                       'Type': 'n:NetworkVideoTransmitter'}},
                  {'239.255.255.250': {'Address': 'http://192.168.1.227:10080/onvif/device_service',
                                       'Message id': '7f895c4f417c163d-7f085db2-71dd321f-3741ff63-6dcbdcb3456bbd8d18c24d40',
                                       'Type': 'n:NetworkVideoTransmitter'}}]}
>>> 
```
