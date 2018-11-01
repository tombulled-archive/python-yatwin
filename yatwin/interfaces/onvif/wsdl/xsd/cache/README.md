# python-yatwin: /yatwin/interfaces/onvif/wsdl/xsd/cache/

## Contents:
* [dump.dump_all](#example-dumpdump_all)
* [load.load](#example-loadload)

### Example: dump.dump_all
```python
>>> from yatwin.interfaces.onvif.wsdl.xsd.cache import dump_all
>>> from pprint import pprint
>>> 
>>> # Dump all XSD assets into cached forms
>>> pprint(dump_all())
{'compiled': {'common.xsd': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\common.xsd.compiled.pickle',
              'onvif.xsd': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\onvif.xsd.compiled.pickle'},
 'parsed': {'common.xsd': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\common.xsd.parsed.pickle',
            'onvif.xsd': 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\cache\\onvif.xsd.parsed.pickle'}}
>>> 
```

### Example: load.load
```python
>>> from yatwin.interfaces.onvif.wsdl.xsd.cache import load
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> 
>>> # Pick a XSD to load
>>> XSD_ONVIF = assets.XSD_ONVIF
>>> XSD_ONVIF
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd'
>>> 
>>> # Load it into a <Xsd> instance
>>> xsd_onvif = load(XSD_ONVIF)
>>> xsd_onvif
<Xsd(onvif.xsd)>
>>> 
```
