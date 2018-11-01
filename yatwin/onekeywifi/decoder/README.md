# python-yatwin: /yatwin/onekeywifi/decoder/

## Contents:
* [decoder.Decoder](#example-decoderdecoder)

### Example: decoder.Decoder
```python
>>> from yatwin.onekeywifi import Decoder
>>> 
>>> # Encoded data information
>>> FREQUENCIES = [8300, 6500, 6900, 9100, 9300, 9500, 9700, 9100, 7900, 6900, 8900, 8700, 9300, 8900, 7300, 9300, 9700, 8500, 10100, 8300]
>>> BSSIDS = ['ab:cd:ef:ab:cd:ef']
>>> 
>>> # Create a Decoder instance
>>> decoder = Decoder()
>>> 
>>> # Decode the data
>>> bssid, psk = decoder.decode(FREQUENCIES, BSSIDS)
>>> 
>>> # View the decoded data
>>> bssid
'AB:CD:EF:AB:CD:EF'
>>> psk
'Ybrb'
>>> 
```
