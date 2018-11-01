# python-yatwin: /yatwin/interfaces/http/files/

## Contents:
* [files](#example-files)

### Example: files
```python
>>> from yatwin.interfaces.http.files import FILES
>>> FILES
[<FirmwareFile(file)>]
>>> 
>>> # Indirectly import a file
>>> from yatwin.interfaces.http.files import FILE
>>> FILE
<FirmwareFile(file)>
>>> 
>>> # Directly import a file
>>> from yatwin.interfaces.http.files.firmware_files import FILE
>>> FILE
<FirmwareFile(file)>
>>> 
```
