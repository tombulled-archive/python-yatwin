# python-yatwin: /yatwin/interfaces/http/parameters/

## Contents:
* [parameters](#example-parameters)

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
