# python-yatwin: /yatwin/interfaces/onvif/wsdl/xsd/

## Contents:
* [Xsd.Xsd](#example-xsdxsd)
* [XsdCompiler.XsdCompiler](#example-xsdcompilerxsdcompiler)
* [XsdParser.XsdParser](#example-xsdparserxsdparser)
* [XsdSource.XsdSource](#example-xsdsourcexsdsource)

### Example: Xsd.Xsd
```python
>>> from yatwin.interfaces.onvif.wsdl import Xsd
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> 
>>> # Pick an XSD
>>> XSD_ONVIF = assets.XSD_ONVIF
>>> XSD_ONVIF
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd'
>>> 
>>> # Create an Xsd instance
>>> onvif = Xsd(XSD_ONVIF)
>>> onvif
<Xsd(onvif.xsd)>
>>> 
>>> # Some class attributes
>>> onvif.XsdSource
<XsdSource(onvif.xsd)>
>>> onvif.XsdParser
<XsdParser(onvif.xsd)>
>>> onvif.XsdCompiler
<XsdCompiler(onvif.xsd)>
>>> 
```

### Example: XsdCompiler.XsdCompiler
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import xsd
>>> 
>>> # Pick an XSD
>>> XSD_ONVIF = assets.XSD_ONVIF
>>> XSD_ONVIF
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd'
>>> 
>>> # Create an XsdSource instance
>>> onvif_source = xsd.XsdSource(XSD_ONVIF)
>>> onvif_source
<XsdSource(onvif.xsd)>
>>> 
>>> # Create an XsdParser instance
>>> onvif_parser = xsd.XsdParser(onvif_source)
>>> onvif_parser
<XsdParser(onvif.xsd)>
>>>
>>> # Create an XsdCompiler instance
>>> onvif_compiler = xsd.XsdCompiler(onvif_parser)
>>> onvif_compiler
<XsdCompiler(onvif.xsd)>
>>> 
>>> # Compile the xsd
>>> compiled = onvif_compiler.compile()
>>> 
```

### Example: XsdParser.XsdParser
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import xsd
>>> 
>>> # Pick an XSD
>>> XSD_ONVIF = assets.XSD_ONVIF
>>> XSD_ONVIF
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd'
>>> 
>>> # Create an XsdSource instance
>>> onvif_source = xsd.XsdSource(XSD_ONVIF)
>>> onvif_source
<XsdSource(onvif.xsd)>
>>> 
>>> # Create an XsdParser instance
>>> onvif_parser = xsd.XsdParser(onvif_source)
>>> onvif_parser
<XsdParser(onvif.xsd)>
>>> 
>>> # Parse the xsd
>>> parsed = onvif_parser.parse()
>>> 
```

### Example: XsdSource.XsdSource
```python
>>> from yatwin.interfaces.onvif.wsdl import assets
>>> from yatwin.interfaces.onvif.wsdl import xsd
>>> 
>>> # Pick an XSD
>>> XSD_ONVIF = assets.XSD_ONVIF
>>> XSD_ONVIF
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\yatwin\\interfaces\\onvif\\wsdl\\assets\\onvif.xsd'
>>> 
>>> # Create an XsdSource instance
>>> onvif_source = xsd.XsdSource(XSD_ONVIF)
>>> onvif_source
<XsdSource(onvif.xsd)>
>>> 
>>> # Get the filename
>>> onvif_source._file_name
'onvif.xsd'
>>> 
```

