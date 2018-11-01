# python-yatwin: /yatwin/interfaces/onvif/wsdl/assets/

## Contents:
* [files](#example-files)

### Example: files
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from pprint import pprint
>>> 
>>> # See what WSDL assets are available
>>> # Note: Results are limited to first 10
>>> pprint(assets.WSDLS[:10])
('C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\analytics.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\analyticsdevice.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\deviceio.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\devicemgmt.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\display.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\event.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\imaging.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\media.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\ptz.wsdl',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\remotediscovery.wsdl')
>>> 
>>> # See what XSD assets are available
>>> pprint(assets.XSDS)
('C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd',
 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\common.xsd')
>>> 
>>> # Indirectly import an asset
>>> from yatwin.interfaces.onvif.wsdl.assets import WSDL_ANALYTICS
>>> WSDL_ANALYTICS
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\analytics.wsdl'
>>> 
>>> # Directly import an asset
>>> from yatwin.interfaces.onvif.wsdl.assets.files import WSDL_DEVICE_IO
>>> WSDL_DEVICE_IO
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\deviceio.wsdl'
>>> 
```
