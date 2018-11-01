# python-yatwin: /yatwin/interfaces/http/parameters/

## Contents:
* [parameters](#example-parameters)
* [utils.get_parameter](#example-utilsget_parameter)

### Example: parameters
```python
>>> from yatwin.interfaces.http import parameters
>>> from pprint import pprint
>>> 
>>> # See what parameters are available
>>> # Note: Results are limited to the first 10
>>> pprint(parameters.PARAMETERS[:10]+['...'])
[<SystemParam(adc_max)>,
 <SystemParam(adc_min)>,
 <SystemParam(adc_use)>,
 <SystemParam(aging_enable)>,
 <SystemParam(alarm_audio)>,
 <SystemParam(alarm_http)>,
 <SystemParam(alarm_http_url)>,
 <SystemParam(alarm_input_armed)>,
 <SystemParam(alarm_ioin_level)>,
 <SystemParam(alarm_iolinkage)>,
 '...']
>>> 
>>> # Pick a parameter
>>> adc_min = parameters.PARAMETERS[1]
>>> adc_min
<SystemParam(adc_min)>
>>> 
>>> # Indirectly import a parameter
>>> from yatwin.interfaces.http.parameters import ADC_MIN
>>> ADC_MIN
<SystemParam(adc_min)>
>>> 
>>> # Directly import a parameter
>>> from yatwin.interfaces.http.parameters.system_parameters import ADC_MAX
>>> ADC_MAX
<SystemParam(adc_max)>
>>> 
```

### Example: utils.get_parameter
```python
>>> from yatwin.interfaces.http.parameters import utils
>>> 
>>> # Get a parameter
>>> adc_min = utils.get_parameter(identifier = 'adc_min')
>>> adc_min
<SystemParam(adc_min)>
>>> 
>>> # Get a parameter that doesn't exist
>>> foo_bar = utils.get_parameter(identifier = 'foo_bar')
>>> foo_bar
>>> 
```
