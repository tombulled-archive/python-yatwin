# python-yatwin: /yatwin/interfaces/rtsp/

## Contents:
* [constants](#example-constants)
* [ffmpeg.download_audio](#example-ffmpegdownload_audio)
* [ffmpeg.download_snapshot](#example-ffmpegdownload_snapshot)
* [ffmpeg.download_video](#example-ffmpegdownload_video)
* [rtsp.Rtsp](#example-rtsprtsp)
* [utils.embed_image](#example-utilsembed_image)
* [vlc.download_audio](#example-vlcdownload_audio)
* [vlc.download_snapshot](#example-vlcdownload_snapshot)
* [vlc.download_video](#example-vlcdownload_video)
* [vlc.play_audio](#example-vlcplay_audio)
* [vlc.view_snapshot](#example-vlcview_snapshot)
* [vlc.view_video](#example-vlcview_video)
* [vlc.embed_video](#example-vlcembed_video)

### Example: constants
```python
>>> from yatwin.interfaces.rtsp import constants
>>> from pprint import pprint
>>> 
>>> # See what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()])
['DEFAULT_ENDPOINT',
 'DEFAULT_PASSWORD',
 'DEFAULT_PORT',
 'DEFAULT_USERNAME',
 'VLC_SNAPSHOT_WAIT']
>>> 
>>> # Get a constants value
>>> constants.DEFAULT_ENDPOINT
'udp/av1_0'
>>> 
>>> # Change a constants value
>>> constants.DEFAULT_ENDPOINT = 'udp/av2_1'
>>> constants.DEFAULT_ENDPOINT
'udp/av2_1'
>>> 
>>> # Create a new constant
>>> constants.FOO_BAR = 'Value'
>>> constants.FOO_BAR
'Value'
>>> 
```

### Example: ffmpeg.download_audio
```python
>>> from yatwin.interfaces.rtsp import ffmpeg
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download audio
>>> ffmpeg.download_audio(URL, file_out = 'audio.mp3', duration = 5)
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\audio.mp3'
>>> 
```

### Example: ffmpeg.download_snapshot
```python
>>> from yatwin.interfaces.rtsp import ffmpeg
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download snapshot
>>> ffmpeg.download_snapshot(URL, file_out = 'snapshot.jpg')
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.jpg'
>>> 
```

### Example: ffmpeg.download_video
```python
>>> from yatwin.interfaces.rtsp import ffmpeg
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download video
>>> ffmpeg.download_video(URL, file_out = 'video.mp4', audio = True, duration = 5)
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\video.mp4'
>>> 
```

### Example: rtsp.Rtsp
```python
>>> from yatwin.interfaces import Rtsp
>>> 
>>> # Camera (RTSP) information
>>> HOST = '192.168.1.227'
>>> USERNAME = 'admin'
>>> PASSWORD = '888888'
>>> # PORT = ...
>>> # ENDPOINT = ...
>>> 
>>> # Create an Rtsp instance
>>> rtsp = Rtsp \
(
	HOST,
	username = USERNAME,
	password = PASSWORD,
	# port = ...,
	# endpoint = ...,
)
>>> rtsp
<Rtsp(admin:888888@192.168.1.227:10554)[udp/av1_0]>
>>> 
>>> # Call some methods
>>> rtsp._make_url()
'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> rtsp.download_snapshot()
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.jpg'
>>> 
```

### Example: utils.embed_image
```python
>>> from yatwin.interfaces.rtsp import utils
>>> import tkinter as tk
>>> from pprint import pprint
>>> 
>>> # Information
>>> IMAGE_PATH = 'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.jpg'
>>> 
>>> # Create a tkinter window and frame
>>> root = tk.Tk()
>>> frame = tk.Frame(root)
>>> frame.grid(row=1, column=1, sticky='nsew')
>>>
>>> # Embed the image
>>> embedded = utils.embed_image(frame, IMAGE_PATH)
>>> pprint(embedded)
{'Image': <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=1280x720 at 0x234A0CB97B8>,
 'Label': <tkinter.Label object .!frame.!label2>,
 'PhotoImage': <PIL.ImageTk.PhotoImage object at 0x0000023496B50780>}
>>> 
>>> # Finally, place root into a mainloop
>>> try:
	root.mainloop()
except KeyboardInterrupt:
	pass

>>>
```

### Example: vlc.download_audio
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download audio
>>> vlc.download_audio(URL)
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\audio.flac'
>>> 
```

### Example: vlc.download_snapshot
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download snapshot
>>> vlc.download_snapshot(URL)
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\snapshot.png'
>>> 
```

### Example: vlc.download_video
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Download video
>>> vlc.download_video(URL)
'C:\\Users\\Admin\\Documents\\GitHub\\python-yatwin\\video.mp4'
>>> 
```

### Example: vlc.play_audio
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Play audio
>>> player = vlc.play_audio(URL, duration = None)
>>> 
>>> # Listen for a bit...
>>> 
>>> # Stop playing audio
>>> player.stop()
>>> 
```

### Example: vlc.view_snapshot
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # View snapshot
>>> player = vlc.view_snapshot(URL)
>>> player
<vlc.MediaPlayer object at 0x00000234A0CB9E10>
>>> 
>>> # View snapshot for a bit...
>>> 
>>> # Destroy window
>>> player.stop()
>>> 
```

### Example: vlc.view_video
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # View video
>>> player = vlc.view_video(URL, duration = None)
>>> player
<vlc.MediaPlayer object at 0x000002349ECF6240>
>>> 
>>> # View video for a bit...
>>> 
>>> # Destroy window
>>> player.stop()
>>> 
```

### Example: vlc.embed_video
```python
>>> from yatwin.interfaces.rtsp import vlc
>>> import tkinter as tk
>>> 
>>> # RTSP information
>>> URL = 'rtsp://admin:888888@192.168.1.227:10554/udp/av1_0'
>>> 
>>> # Create a window
>>> root = tk.Tk()
>>> 
>>> # Create a frame
>>> frame = tk.Frame(root)
>>> frame.grid(row=1, column=1, sticky='nsew')
>>> 
>>> # Make frame expand to root
>>> root.grid_columnconfigure(1, weight=1)
>>> root.grid_rowconfigure(1, weight=1)
>>> 
>>> # Setup root
>>> root.grid_propagate(False)
>>> root.geometry('1080x720')
''
>>> 
>>> # Embed the video
>>> player = vlc.embed_video(URL, frame)
>>> player
<vlc.MediaPlayer object at 0x00000234A0CB9EB8>
>>> 
>>> # Play the video
>>> player.play()
0
>>> 
>>> # Finally, place root into a mainloop
>>> try:
	root.mainloop()
except KeyboardInterrupt:
	player.stop()
	root.destroy()

	
>>> 
```
