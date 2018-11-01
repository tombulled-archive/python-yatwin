# python-yatwin: /yatwin/interfaces/http/files/file_types/

## Contents:
* [BaseFile](#example-basefile)
* [File](#example-file)
* [FirmwareFile](#example-firmwarefile)

### Example: BaseFile
```python
>>> from yatwin.interfaces.http.files.file_types import BaseFile
>>> 
>>> # File information
>>> IDENTIFIER = 'file'
>>> DESCRIPTION = 'File to upload to server'
>>> 
>>> # Create the BaseFile instance
>>> file = BaseFile(identifier = IDENTIFIER, description = DESCRIPTION)
>>> file
<BaseFile(file)>
>>> 
```

### Example: File
```python
>>> from yatwin.interfaces.http.files.file_types import File
>>> 
>>> # File information
>>> IDENTIFIER = 'file'
>>> DESCRIPTION = 'File to upload to server'
>>> 
>>> # Create the BaseFile instance
>>> file = File(identifier = IDENTIFIER, description = DESCRIPTION)
>>> file
<File(file)>
>>> 
```

### Example: FirmwareFile
```python
>>> from yatwin.interfaces.http.files.file_types import FirmwareFile
>>> 
>>> # File information
>>> IDENTIFIER = 'file'
>>> DESCRIPTION = 'File to upload to server'
>>> 
>>> # Create the BaseFile instance
>>> file = FirmwareFile(identifier = IDENTIFIER, description = DESCRIPTION)
>>> file
<FirmwareFile(file)>
>>> 
```
