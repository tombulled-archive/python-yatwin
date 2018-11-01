# python-yatwin: /yatwin/interfaces/http/methods/constants/

## Contents:
* [constants](#example-constants)

### Example: constants
```python
>>> from yatwin.interfaces.http.methods import constants
>>> from pprint import pprint
>>> 
>>> # See what constants are available
>>> # Note: Results limited to the first 10
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()][:10]+['...'])
['ADMINISTRATOR',
 'CENTER',
 'GET',
 'HPATROL',
 'HPATROL_STOP',
 'IO_OFF',
 'IO_ON',
 'MANAGER',
 'OPERATOR',
 'PARAM_BRIGHTNESS',
 '...']
>>> 
>>> # Get a constants value
>>> constants.HPATROL
28
>>> 
>>> # Change a constants value
>>> constants.MANAGER = 'New Value'
>>> constants.MANAGER
'New Value'
>>> 
>>> # Create a new constant
>>> constants.NEW_CONSTANT = 1
>>> 
>>> # Indirectly import a constant
>>> from yatwin.interfaces.http.methods.constants import ADMINISTRATOR
>>> ADMINISTRATOR
'ADMINISTRATOR'
>>> 
>>> # Directly import a constant
>>> from yatwin.interfaces.http.methods.constants.permissions import VISITOR
>>> VISITOR
'VISITOR'
>>> 
```
