# python-yatwin: /yatwin/onekeywifi/player/

## Contains:
* [constants](#example-constants)
* [Player.Player](#example-playerplayer)
* [utils.play_tone](#example-utilsplay_tone)

### Example: constants
```python
>>> from yatwin.onekeywifi.player import constants
>>> from pprint import pprint
>>> 
>>> # See what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_') and attr.isupper()])
['CHANNELS', 'FADE', 'FORMAT', 'FORMAT_NP', 'RATE', 'TONE_DURATION', 'WAIT_GAP']
>>> 
>>> # Pick a constant
>>> constants.CHANNELS
1
>>> 
>>> # Import a constant
>>> from yatwin.onekeywifi.player.constants import RATE
>>> RATE
44100
>>> 
>>> # Change a constants value
>>> RATE = 1200
>>> RATE
1200
>>> 
>>> # Create a new constant
>>> constants.FOO_BAR = 'Value'
>>> constants.FOO_BAR
'Value'
>>> 
```

### Example: Player.Player
```python
>>> from yatwin.onekeywifi import Player
>>> 
>>> # Create a Player instance
>>> player = Player()
>>> 
>>> # Pick some frequencies
>>> FREQUENCIES = [8300, 6500, 6900, 9100, 9300, 9500, 9700, 9100, 7900, 6900, 8900, 8700, 9300, 8900, 7300, 9300, 9700, 8500, 10100, 8300]
>>> 
>>> # Play those frequencies
>>> player.play_frequencies(FREQUENCIES, play_count = 1)
>>> 
```

### Example: utils.play_tone
```python
>>> from yatwin.onekeywifi.player import constants
>>> from yatwin.onekeywifi.player import utils
>>> import pyaudio
>>> 
>>> # Create a pyaudio player and stream
>>> player = pyaudio.PyAudio()
>>> stream = player.open(format=constants.FORMAT, channels=constants.CHANNELS, rate=constants.RATE, output=1)
>>> 
>>> # Pick a frequency
>>> FREQUENCY = 1000
>>> 
>>> # Play that frequency
>>> utils.play_tone(stream, FREQUENCY, 3)
>>> 
```
