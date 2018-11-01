# python-yatwin: /yatwin/interfaces/onvif/wsdl/wsdl/cache/

## Contents:
* [dump.dump_all](#example-dumpdump_all)
* [load.load](#example-loadload)

### Example: dump.dump_all
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl.cache import dump_all
>>> from pprint import pprint
>>> 
>>> # Dump all WSDL assets into cached forms
>>> pprint(dump_all())
{'compiled': {'analytics.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\analytics.wsdl.compiled.pickle',
              'analyticsdevice.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\analyticsdevice.wsdl.compiled.pickle',
              'deviceio.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\deviceio.wsdl.compiled.pickle',
              'devicemgmt.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\devicemgmt.wsdl.compiled.pickle',
              'display.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\display.wsdl.compiled.pickle',
              'event.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\event.wsdl.compiled.pickle',
              'events.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\events.wsdl.compiled.pickle',
              'imaging.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\imaging.wsdl.compiled.pickle',
              'media.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\media.wsdl.compiled.pickle',
              'ptz.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\ptz.wsdl.compiled.pickle',
              'receiver.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\receiver.wsdl.compiled.pickle',
              'recording.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\recording.wsdl.compiled.pickle',
              'remotediscovery.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\remotediscovery.wsdl.compiled.pickle',
              'replay.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\replay.wsdl.compiled.pickle',
              'search.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\search.wsdl.compiled.pickle'},
 'parsed': {'analytics.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\analytics.wsdl.parsed.pickle',
            'analyticsdevice.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\analyticsdevice.wsdl.parsed.pickle',
            'deviceio.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\deviceio.wsdl.parsed.pickle',
            'devicemgmt.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\devicemgmt.wsdl.parsed.pickle',
            'display.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\display.wsdl.parsed.pickle',
            'event.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\event.wsdl.parsed.pickle',
            'events.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\events.wsdl.parsed.pickle',
            'imaging.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\imaging.wsdl.parsed.pickle',
            'media.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\media.wsdl.parsed.pickle',
            'ptz.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\ptz.wsdl.parsed.pickle',
            'receiver.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\receiver.wsdl.parsed.pickle',
            'recording.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\recording.wsdl.parsed.pickle',
            'remotediscovery.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\remotediscovery.wsdl.parsed.pickle',
            'replay.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\replay.wsdl.parsed.pickle',
            'search.wsdl': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\search.wsdl.parsed.pickle'}}
>>> 
```

### Example: load.load
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl.cache import load
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> 
>>> # Pick a WSDL to load
>>> WSDL_ANALYTICS = assets.WSDL_ANALYTICS
>>> WSDL_ANALYTICS
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\analytics.wsdl'
>>> 
>>> # Load it into a <Wsdl> instance
>>> wsdl_analytics = load(WSDL_ANALYTICS)
>>> wsdl_analytics
<Wsdl(analytics.wsdl)>
>>> 
```
