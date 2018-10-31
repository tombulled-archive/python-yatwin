# python-yatwin: /yatwin/interfaces/http/methods/utils

## Contents:
* [utils](#example-utils)
* [controllers](#example-controllers)

### Example: utils
```python
>>> from yatwin.interfaces.http.methods import utils
>>> from pprint import pprint
>>> 
>>> # See what utils are available
>>> pprint([attr for attr in dir(utils) if not attr.startswith('_')])
['constants',
 'controllers',
 'generate_preset',
 'scale_brightness',
 'scale_contrast',
 'scale_hue',
 'scale_ptz_patrol_rate']
>>> 
>>> # Indirectly import a util
>>> from yatwin.interfaces.http.methods.utils import scale_hue
>>> 
>>> # Directly import a util
>>> from yatwin.interfaces.http.methods.utils.controllers import scale_hue
>>>  
```

### Example: controllers
```python
>>> from yatwin.interfaces.http.methods import utils
>>>
>>> # scale_ptz_patrol_rate
>>> utils.scale_ptz_patrol_rate(5)
10
>>> 
>>> # scale_brightness
>>> utils.scale_brightness(6)
42
>>> 
>>> # scale_contrast
>>> utils.scale_contrast(4)
28
>>> 
>>> # scale_hue
>>> utils.scale_hue(7)
49
>>> 
>>> # generate_preset
>>> utils.generate_preset(4, set = False)
37
>>> 
```
