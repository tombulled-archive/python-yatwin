# python-yatwin: /yatwin/interfaces/onvif/wsdl/wsdl/

## Contents:
* [errors](#example-errors)
* [methods.print_compiled_operation](#example-methodsprint_compiled_operation)
* [methods.sprintf_compiled_operation](#example-methodssprintf_compiled_operation)
* [methods.identify_operations](#example-methodsidentify_operations)
* [Wsdl.Wsdl](#example-wsdlwsdl)
* [WsdlCompiler.WsdlCompiler](#example-wsdlcompilerwsdlcompiler)
* [WsdlParser.WsdlParser](#example-wsdlparserwsdlparser)
* [WsdlSource.WsdlSource](#example-wsdlsourcewsdlsource)

### Example: errors
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl import errors
>>> from pprint import pprint
>>> 
>>> # See what error classes are available
>>> pprint([attr for attr in dir(errors) if not attr.startswith('_')])
['FileDoesNotExist', 'InvalidArgument', 'ParseError']
>>> 
>>> # Pick an error
>>> FileDoesNotExist = errors.FileDoesNotExist
>>> FileDoesNotExist
<class 'yatwin.interfaces.onvif.wsdl.wsdl.errors.FileDoesNotExist'>
>>> 
>>> # Import an error
>>> from yatwin.interfaces.onvif.wsdl.wsdl.errors import InvalidArgument
>>> InvalidArgument
<class 'yatwin.interfaces.onvif.wsdl.wsdl.errors.InvalidArgument'>
>>> 
>>> # Raise an error
>>> raise FileDoesNotExist('My error message')
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    raise FileDoesNotExist('My error message')
yatwin.interfaces.onvif.wsdl.wsdl.errors.FileDoesNotExist: My error message
>>> 
```

### Example: methods.print_compiled_operation
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl import methods
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif import wsdl
>>> 
>>> # Create a <Wsdl> instance
>>> device_io = wsdl.Wsdl(assets.WSDL_DEVICE_IO)
>>> device_io
<Wsdl(deviceio.wsdl)>
>>> 
>>> # Get its compiled data
>>> compiled = device_io.compiled
>>>
>>> # Get the WSDL's operations
>>> operations = device_io.find_all()
>>>
>>> # Pick an operation
>>> operation = operations[0]
>>> operation['Name']
'GetServiceCapabilities'
>>> 
>>> # Print a representation of the compiled operation
>>> methods.print_compiled_operation(operation)
1. GetServiceCapabilities
Description:
Returns the capabilities of the device IO service. The result is returned in a typed answer.
SOAP action:
http://www.onvif.org/ver10/deviceio/wsdl/GetServiceCapabilities
Input:
	[GetServiceCapabilities]
Output:
	[GetServiceCapabilitiesResponse]
		* Capabilities [Capabilities]
		  The capabilities for the device IO service is returned in the Capabilities element.
			o VideoSources [int]
			  Number of video sources (defaults to none).
			o VideoOutputs [int]
			  Number of video outputs (defaults to none).
			o AudioSources [int]
			  Number of audio sources (defaults to none).
			o AudioOutputs [int]
			  Number of audio outputs (defaults to none).
			o RelayOutputs [int]
			  Number of relay outputs (defaults to none).
			o SerialPorts [int]
			  Number of serial ports (defaults to none).
			o DigitalInputs [int]
			  Number of digital inputs (defaults to none).
			o DigitalInputOptions [boolean]
			  Indicates support for DigitalInput configuration of the idle state (defaults to false).

>>> 
```

### Example: methods.sprintf_compiled_operation
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl import methods
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif import wsdl
>>> 
>>> # Create a <Wsdl> instance
>>> device_io = wsdl.Wsdl(assets.WSDL_DEVICE_IO)
>>> device_io
<Wsdl(deviceio.wsdl)>
>>> 
>>> # Get its compiled data
>>> compiled = device_io.compiled
>>>
>>> # Get the WSDL's operations
>>> operations = device_io.find_all()
>>>
>>> # Pick an operation
>>> operation = operations[0]
>>> operation['Name']
'GetServiceCapabilities'
>>> 
>>> # Manually print a representation of the compiled operation
>>> print(methods.sprintf_compiled_operation(operation))
1. GetServiceCapabilities
Description:
Returns the capabilities of the device IO service. The result is returned in a typed answer.
SOAP action:
http://www.onvif.org/ver10/deviceio/wsdl/GetServiceCapabilities
Input:
	[GetServiceCapabilities]
Output:
	[GetServiceCapabilitiesResponse]
		* Capabilities [Capabilities]
		  The capabilities for the device IO service is returned in the Capabilities element.
			o VideoSources [int]
			  Number of video sources (defaults to none).
			o VideoOutputs [int]
			  Number of video outputs (defaults to none).
			o AudioSources [int]
			  Number of audio sources (defaults to none).
			o AudioOutputs [int]
			  Number of audio outputs (defaults to none).
			o RelayOutputs [int]
			  Number of relay outputs (defaults to none).
			o SerialPorts [int]
			  Number of serial ports (defaults to none).
			o DigitalInputs [int]
			  Number of digital inputs (defaults to none).
			o DigitalInputOptions [boolean]
			  Indicates support for DigitalInput configuration of the idle state (defaults to false).

>>> 
```

### Example: methods.identify_operations
```python
>>> from yatwin.interfaces.onvif.wsdl.wsdl import methods
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif import wsdl
>>> from yatwin.interfaces import Onvif
>>> from pprint import pprint
>>> 
>>> # Create an Onvif instance, see documentation for <Onvif> for more info
>>> onvif = Onvif('192.168.1.227')
>>> onvif
<Onvif(admin:888888@192.168.1.227:10080)>
>>> 
>>> # See what services are available
>>> pprint(onvif.services)
{'DeviceMgmt': <onvif.client.ONVIFService object at 0x000001D250970940>,
 'Events': <onvif.client.ONVIFService object at 0x000001D25AD12C50>,
 'Imaging': <onvif.client.ONVIFService object at 0x000001D25AD64E48>,
 'Media': <onvif.client.ONVIFService object at 0x000001D25AF9A9B0>,
 'PTZ': <onvif.client.ONVIFService object at 0x000001D25B2F02B0>}
>>> 
>>> # Create a <Wsdl> instance for the DeviceMgmt WSDL
>>> device_mgmt = wsdl.Wsdl(assets.WSDL_DEVICE_MGMT)
>>> device_mgmt
<Wsdl(devicemgmt.wsdl)>
>>> 
>>> # Get its compiled data
>>> compiled = device_io.compiled
>>> 
>>> # Get the Onvif service associated with it
>>> service = onvif.services.get('DeviceMgmt', None)
>>> service
<onvif.client.ONVIFService object at 0x000001D250970940>
>>> 
>>> # Identify operations contained in the wsdl which the service supports
>>> operations = methods.identify_operations(service, device_mgmt)
>>> 
>>> # Pick an operation
>>> operation = operations[0]
>>> operation['Name']
'GetServices'
>>> 
```

### Example: Wsdl.Wsdl
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif import wsdl
>>> 
>>> # Pick a WSDL asset
>>> WSDL_DEVICE_MGMT = assets.WSDL_DEVICE_MGMT
>>> WSDL_DEVICE_MGMT
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\devicemgmt.wsdl'
>>> 
>>> # Create a Wsdl instance
>>> device_mgmt = wsdl.Wsdl(WSDL_DEVICE_MGMT)
>>> device_mgmt
<Wsdl(devicemgmt.wsdl)>
>>> 
>>> # Find an operation
>>> operation = device_mgmt.find(name = 'GetServices')
>>> operation['Name']
'GetServices'
>>> operation['Documentation']
'Returns information about services on the device.'
>>> 
```

### Example: WsdlCompiler.WsdlCompiler
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import wsdl
>>> 
>>> # Pick a WSDL asset
>>> WSDL_DEVICE_MGMT = assets.WSDL_DEVICE_MGMT
>>> WSDL_DEVICE_MGMT
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\devicemgmt.wsdl'
>>> 
>>> # Create a WsdlSource instance
>>> device_mgmt_source = wsdl.WsdlSource(WSDL_DEVICE_MGMT)
>>> device_mgmt_source
<WsdlSource(devicemgmt.wsdl)>
>>> 
>>> # Create a WsdlParser instance
>>> device_mgmt_parser = wsdl.WsdlParser(device_mgmt_source)
>>> device_mgmt_parser
<WsdlParser(devicemgmt.wsdl)>
>>> 
>>> # Create a WsdlCompiler instance
>>> device_mgmt_compiler = wsdl.WsdlCompiler(device_mgmt_parser)
>>> device_mgmt_compiler
<WsdlCompiler(devicemgmt.wsdl)>
>>> 
>>> # Compile the wsdl
>>> compiled = device_mgmt_compiler.compile()
>>> 
>>> # Compile the wsdl minimally
>>> compiled_min = device_mgmt_compiler.compile_min()
>>>
```

### Example: WsdlParser.WsdlParser
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import wsdl
>>> 
>>> # Pick a WSDL asset
>>> WSDL_DEVICE_MGMT = assets.WSDL_DEVICE_MGMT
>>> WSDL_DEVICE_MGMT
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\devicemgmt.wsdl'
>>> 
>>> # Create a WsdlSource instance
>>> device_mgmt_source = wsdl.WsdlSource(WSDL_DEVICE_MGMT)
>>> device_mgmt_source
<WsdlSource(devicemgmt.wsdl)>
>>> 
>>> # Create a WsdlParser instance
>>> device_mgmt_parser = wsdl.WsdlParser(device_mgmt_source)
>>> device_mgmt_parser
<WsdlParser(devicemgmt.wsdl)>
>>>
>>> # Parse the wsdl
>>> parsed = device_mgmt_parser.parse()
>>> 
```

### Example: WsdlSource.WsdlSource
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import wsdl
>>> 
>>> # Pick a WSDL asset
>>> WSDL_DEVICE_MGMT = assets.WSDL_DEVICE_MGMT
>>> WSDL_DEVICE_MGMT
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\devicemgmt.wsdl'
>>> 
>>> # Create a WsdlSource instance
>>> device_mgmt_source = wsdl.WsdlSource(WSDL_DEVICE_MGMT)
>>> device_mgmt_source
<WsdlSource(devicemgmt.wsdl)>
>>> 
>>> # Get the WSDL filename
>>> device_mgmt_source._file_name
'devicemgmt.wsdl'
>>> 
```

