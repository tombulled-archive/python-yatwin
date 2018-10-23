# python-yatwin: /yatwin/decorators/

### Example: @debug_call
```python
>>> import yatwin
>>> from yatwin import decorators
>>> import logging
>>>
>>> # Enable logging, and set it to 'debug' level
>>> yatwin.logger.setLevel(logging.DEBUG)
>>> yatwin._enable_logging()
INFO:yatwin:Logging has been enabled
>>>
>>> # Create a function decorated with debug_call
>>> @decorators.debug_call(yatwin.logger)
def my_func(param, key = 1):
  pass
  
>>> 
>>> # Call the function
>>> my_func('some_val', key = 3)
DEBUG:yatwin:my_func('some_val', key=3)
>>> 
```

### Example: @debug_resp
```python
>>> import yatwin
>>> from yatwin import decorators
>>> import logging
>>>
>>> # Enable logging, and set it to 'debug' level
>>> yatwin.logger.setLevel(logging.DEBUG)
>>> yatwin._enable_logging()
INFO:yatwin:Logging has been enabled
>>>
>>> # Create a function decorated with debug_resp
>>> @decorators.debug_resp(yatwin.logger)
def my_func(param, key = 1):
  return 'some data'
  
>>> 
>>> # Call the function
>>> my_func('some_val', key = 3)
DEBUG:yatwin:my_func(...) -> 'some data'
>>>
```

### Example: @debug
```python
>>> import yatwin
>>> from yatwin import decorators
>>> import logging
>>>
>>> # Enable logging, and set it to 'debug' level
>>> yatwin.logger.setLevel(logging.DEBUG)
>>> yatwin._enable_logging()
INFO:yatwin:Logging has been enabled
>>>
>>> # Create a function decorated with debug
>>> @decorators.debug()
def my_func(param, key = 1):
  return 'some data'
  
>>> 
>>> # Call the function
>>> my_func('some_val', key = 3)
DEBUG:yatwin:my_func('some_val', key=3)
DEBUG:yatwin:my_func(...) -> 'some data'
>>>
```
