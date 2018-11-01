# python-yatwin: /yatwin/interfaces/http/parameters/parameter_types/

## Contents:
* [BaseParam](#example-baseparam)
* [ControllerParam](#example-controllerparam)
* [Param](#example-param)
* [SystemParam](#example-systemparam)

### Example: BaseParam
```python
>>> from yatwin.interfaces.http.parameters.parameter_types import BaseParam
>>> 
>>> # Parameter information
>>> IDENTIFIER = 'enc_main_mode'
>>> DESCRIPTION = 'Main encryption mode'
>>> # ...
>>> 
>>> # Create a BaseParam instance
>>> enc_main_mode = BaseParam \
(
	identifier = IDENTIFIER,
	description = DESCRIPTION,
	# ...
)
>>> enc_main_mode
<BaseParam(enc_main_mode)>
>>> 
```


### Example: ControllerParam
```python
>>> from yatwin.interfaces.http.parameters.parameter_types import ControllerParam
>>> 
>>> # Parameter information
>>> IDENTIFIER = 'enc_main_mode'
>>> DESCRIPTION = 'Main encryption mode'
>>> # ...
>>> 
>>> # Create a ControllerParam instance
>>> enc_main_mode = ControllerParam \
(
	identifier = IDENTIFIER,
	description = DESCRIPTION,
	# ...
)
>>> enc_main_mode
<ControllerParam(enc_main_mode)>
>>> 
```


### Example: Param
```python
>>> from yatwin.interfaces.http.parameters.parameter_types import Param
>>> 
>>> # Parameter information
>>> IDENTIFIER = 'enc_main_mode'
>>> DESCRIPTION = 'Main encryption mode'
>>> # ...
>>> 
>>> # Create a Param instance
>>> enc_main_mode = Param \
(
	identifier = IDENTIFIER,
	description = DESCRIPTION,
	# ...
)
>>> enc_main_mode
<Param(enc_main_mode)>
>>> 
```


### Example: SystemParam
```python
>>> from yatwin.interfaces.http.parameters.parameter_types import SystemParam
>>> 
>>> # Parameter information
>>> IDENTIFIER = 'enc_main_mode'
>>> DESCRIPTION = 'Main encryption mode'
>>> # ...
>>> 
>>> # Create a SystemParam instance
>>> enc_main_mode = SystemParam \
(
	identifier = IDENTIFIER,
	description = DESCRIPTION,
	# ...
)
>>> enc_main_mode
<SystemParam(enc_main_mode)>
>>> 
```
