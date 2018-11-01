# python-yatwin: /yatwin/onekeywifi/encoder/

## Contents:
* [Encoder.Encoder](#example-encoderencoder)

### Example: Encoder.Encoder
```python
>>> from yatwin.onekeywifi import Encoder
>>> 
>>> # Network information
>>> BSSID = 'ab:cd:ef:ab:cd:ef'
>>> PSK = 'test'
>>> 
>>> # Create an Encoder instance
>>> encoder = Encoder()
>>> 
>>> # Encode the network information
>>> frequencies = encoder.encode(BSSID, PSK)
>>> 
>>> # View the encoded frequencies
>>> frequencies
[8300, 6500, 6900, 9100, 9300, 9500, 9700, 8700, 8500, 9900, 7100, 7700, 7300, 9300, 9900, 6700, 9100, 10100, 8300]
>>> 
```
