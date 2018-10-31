# python-yatwin: /yatwin/interfaces/http/methods/method_types/

## Contents:
* [Audiostream]
* [BaseMethod]
* [DictMethod]
* [Livestream]
* [ParamMethod]
* [Snapshot]
* [Videostream]
* [decorators]

### Example: Audiostream
```python
>>> from yatwin.interfaces.http.methods.method_types import Audiostream
>>> 
>>> # Method information
>>> ENDPOINT = 'audiostream.cgi'
>>> DESCRIPTION = 'request video communication'
>>> #...
>>> 
>>> # Create an Audiostream instance
>>> audio_stream = Audiostream \
(
	endpoint = ENDPOINT,
	description = DESCRIPTION,
	#...
)
>>> audio_stream
<Audiostream(audiostream.cgi)>
>>> 
>>> # If you have a <Http> instance, for example 'http', you could do:
>>> # audio_stream(http = http).play_stream()
>>> 
```

### Example: BaseMethod
```python
```

### Example: DictMethod
```python
```

### Example: Livestream
```python
```

### Example: ParamMethod
```python
```

### Example: Snapshot
```python
```

### Example: Videostream
```python
```

### Example: decorators
```python
```
