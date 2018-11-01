from ..util import Util
from . import utils

"""
Lots of this code was (pain-stakingly) converted
... from Java to Python from the Java APK Source Code

Contains:
    <DataDecoder>

Imports:
    ..util.Util
    .utils
"""

class DataDecoder(object):
    """
    Class for decoding frequencies into a bssid and a wifi psk
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises self
        """

        pass

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name()>
        """

        return f'<{self.__class__.__name__}()>'

    def decode(self, frequencies, available_frequencies, bssids):
        """
        Decodes 'frequencies' into (bssid, psk) using 'available_frequencies'
        ... and 'bssids'

        :param frequencies - Frequencies to decode
        :param available_frequencies - Which frequencies were used to encode the data
        :param bssids - A list of bssids in which the encoded bssid's endpoint
        ... falls into
        """

        enc_hex = self._hex_from_frequencies(frequencies, available_frequencies)
        mac, psk_hex = self._mac_psk_hex_from_hex(enc_hex)
        bssid = self._bssid_from_mac(mac, bssids)
        psk = self._psk_from_psk_hex(psk_hex)

        return bssid, psk

    def _hex_from_frequencies(self, frequencies, available_frequencies):
        """
        Converts 'frequencies' into a hex string using 'available_frequencies'
        """

        codes = [available_frequencies.index(frequency) for frequency in frequencies]
        hex_chars = '0123456789abcdef'
        codes = codes[2:-6]
        hex_string = ''.join([hex_chars[code - 1] for code in codes])

        return hex_string

    def _mac_psk_hex_from_hex(self, enc_hex):
        """
        Converts the encoded hex into (mac, psk_hex)
        """

        hexc = '0123456789abcdef'
        mac_len, *rest = enc_hex
        mac_len = (hexc.index(mac_len) + 1) * 2
        mac = enc_hex[1:mac_len + 1]
        psk_hex = enc_hex[mac_len + 1:]

        return mac, psk_hex

    def _bssid_from_mac(self, mac, bssids):
        """
        Converts 'mac' into a full BSSID using 'bssids'
        """

        mac = mac.strip().upper()

        bssid_endpoint = ':'.join(utils.chunks(mac, 2))

        for bssid in bssids:
            bssid = bssid.upper()
            if bssid.endswith(bssid_endpoint):
                return bssid

    def _psk_from_psk_hex(self, psk_hex):
        """
        Decodes 'psk_hex' into a plain-text psk
        """

        return self.decodeString(0, psk_hex.encode())

    def decodeString(self, _result, _data):
        """
        Taken From Java APK Source Code
        """

        Bytes = [b'' for _ in range(len(_data))]
        costHexsAdd = [0]
        dataLen, Bytes = self.decodeData(_data, 0, len(_data), costHexsAdd, Bytes, 0, -1)

        return self.bytes2String(Bytes, 0, dataLen)

    def decodeData(self, _hexs, _hexsOff, _hexsLen, _hexsCostLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        aPartLen = [_resultLen]
        costHexsAdd = [0]
        dataLen = 0
        Type = [0]

        _hexsCostLen[0] = 0
        _, Type, _hexsCostLen, aPartLen = self.hex2Type(_hexs, _hexsOff, _hexsLen, _hexsCostLen, Type, aPartLen)

        if Type[0] == 1:
            resultIdx, _result, costHexsAdd = self.hex2Lower(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, aPartLen[0])
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
            resultIdx, _result, costHexsAdd = self.hex2Digit(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff + dataLen, _resultLen if _resultLen < 0 else _resultLen - dataLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 2:
            resultIdx, _result, costHexsAdd = self.hex2Char64(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, aPartLen[0])
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
            resultIdx, _result, costHexsAdd = self.hex2Digit(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff + dataLen, _resultLen if _resultLen < 0 else _resultLen - dataLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 4:
            resultIdx, _result, costHexsAdd = self.hex2Digit(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, aPartLen[0])
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
            resultIdx, _result, costHexsAdd = self.hex2Char64(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff + dataLen, _resultLen if _resultLen < 0 else _resultLen - dataLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 0:
            resultIdx, _result, costHexsAdd = self.hex2Digit(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, _resultLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 3:
            resultIdx, _result, costHexsAdd = self.hex2Char256(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, _resultLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 5:
            resultIdx, _result, costHexsAdd = self.hex2Lower(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, _resultLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 6:
            resultIdx, _result, costHexsAdd = self.hex2Char64(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, _resultLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]
        elif Type[0] == 7:
            resultIdx, _result, costHexsAdd = self.hex2Upper(_hexs, _hexsOff + _hexsCostLen[0], _hexsLen - _hexsCostLen[0], costHexsAdd, _result, _resultOff, _resultLen)
            dataLen += resultIdx
            _hexsCostLen[0] += costHexsAdd[0]

        return (dataLen, _result)

    def hex2Type(self, _hexs, _hexsOff, _hexsLen, _hexsCostLen, _type, _aPartLen):
        """
        Taken From Java APK Source Code
        """

        r = 1

        _type[0] = Util.hexChar2Int(_hexs[_hexsOff + 0]) >> 1
        _hexsCostLen[0] = 1

        if _type[0] == 1 or _type[0] == 2 or _type[0] == 4:
            _aPartLen[0] = (Util.hexChar2Int(_hexs[_hexsOff + 0]) & 0x1) << 4 | Util.hexChar2Int(_hexs[_hexsOff + 1])
            _aPartLen[0] += 1
            r = 2
            _hexsCostLen[0] = 2

        return (r, _type, _hexsCostLen, _aPartLen)

    def hex2Lower(self, _hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        tempChars = [b'' for _ in range(_hexsLen // 2 + 4)] #was +1

        costBits = 0

        _, _result, _costHexsLen = self.hex2Chars(_hexs, _hexsOff, _hexsLen, _costHexsLen, tempChars, 0, _resultLen * 5 if _resultLen > 0 else _resultLen)

        resultIdx = 0

        while _resultLen < 0 or resultIdx < _resultLen:
            costBits = (resultIdx + 1) * 5

            if costBits > _hexsLen * 4:
                break

            _result[_resultOff + resultIdx] = 97 + self.bitsGet(tempChars, 0, resultIdx * 5, costBits)
            _costHexsLen[0] = (costBits + 3) // 4

            resultIdx += 1

        tempChars = None

        return (resultIdx, _result, _costHexsLen)

    def hex2Digit(self, _hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        i = 0

        while i < _hexsLen and (_resultLen < 0 or i < _resultLen):
            _result[_resultOff + i] = _hexs[_hexsOff + i]

            i += 1

        _costHexsLen[0] = i

        return (i, _result, _costHexsLen)

    def hex2Char64(self, _hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        tempChars = [0 for _ in range(_hexsLen // 2 + 1)] #b'' for...?

        costBits = 0

        self.hex2Chars(_hexs, _hexsOff, _hexsLen, _costHexsLen, tempChars, 0, _resultLen * 6 if _resultLen > 0 else _resultLen)

        resultIdx = 0

        while _resultLen < 0 or resultIdx < _resultLen:
            costBits = (resultIdx + 1) * 6

            if costBits > _hexsLen * 4:
                break

            _result[_resultOff + resultIdx] = Util.int2Char64(self.bitsGet(tempChars, 0, resultIdx * 6, costBits))
            _costHexsLen[0] = (costBits + 3) // 4

            resultIdx += 1

        tempChars = None

        return (resultIdx, _result, _costHexsLen)

    def hex2Char256(self, _hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        return self.hex2Chars(_hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen * 8 if _resultLen > 0 else _resultLen)

    def hex2Upper(self, _hexs, _hexsOff, _hexsLen, _costHexsLen, _result, _resultOff, _resultLen):
        """
        Taken From Java APK Source Code
        """

        tempChars = [b'' for _ in range(_hexsLen // 2 + 1)]

        costBits = 0

        _, _result, _costHexsLen = self.hex2Chars(_hexs, _hexsOff, _hexsLen, _costHexsLen, tempChars, 0, _resultLen * 5 if _resultLen > 0 else _resultLen)

        resultIdx = 0

        while _resultLen < 0 or resultIdx < _resultLen:
            costBits = (resultIdx + 1) * 5

            if costBits > _hexsLen * 4:
                break

            _result[_resultOff + resultIdx] = 65 + self.bitsGet(tempChars, 0, resultIdx * 5, costBits)
            _costHexsLen[0] = (costBits + 3) // 4

            resultIdx += 1

        tempChars = None

        return (resultIdx, _result, _costHexsLen)

    def hex2Chars(self, _hexs, _hexsOff, _hexsCount, _costHexsCount, _result, _resultOff, _maxBitsCount):
        """
        Taken From Java APK Source Code
        """

        hexsCount = _hexsCount if _maxBitsCount < 0 else (_maxBitsCount + 3) // 4
        hexsCount = _hexsCount if hexsCount > _hexsCount else hexsCount

        for i in range(hexsCount // 2):
            _result[_resultOff+ i] = Util.hexChar2Int(_hexs[_hexsOff + 2 * i]) << 4 | Util.hexChar2Int(_hexs[_hexsOff + 2 * i + 1])

        _costHexsCount[0] = 2 * i

        if hexsCount % 2 > 0:
            _costHexsCount[0] = 2 * i + 1
            _result[_resultOff + i] = Util.hexChar2Int(_hexs[_hexsOff + 2 * i]) << 4

            i += 1

        return (i, _result, _costHexsCount)

    def bitsGet(self, _bits, _bitsOff, _bitsStart, _bitsEnd):
        """
        Taken From Java APK Source Code
        """

        #_bits = [b for b in _bits if b != b''] #hackish fix

        byteStart = _bitsStart // 8
        byteEnd = _bitsEnd // 8

        if byteStart == byteEnd:
            return self.bitGet(_bits[_bitsOff + byteStart], _bitsStart % 8, _bitsEnd % 8)

        assert byteEnd == byteStart + 1

        startPos = _bitsStart % 8
        endPos = _bitsEnd % 8
        startSource = self.bitGet(_bits[_bitsOff + byteStart], startPos, 8)
        endSource = self.bitGet(_bits[_bitsOff + byteEnd], 0, endPos)

        return startSource << endPos | endSource

    def bitGet(self, _sourceBits, _start, _end):
        """
        Taken From Java APK Source Code
        """

        return (_sourceBits >> 8 - _end if _end < 8 else _sourceBits) & 255 >> 8 - (_end - _start)

    def bytes2String(self, _bytes, _off, _len):
        """
        Taken From Java APK Source Code
        """

        #_bytes = b''.join(_bytes)
        _bytes = b''.join([chr(b).encode()  if b != b'' else b'' for b in _bytes]) #fix

        s = None
        try:
            s = _bytes.decode('gbk')
        except:
            s = _bytes.decode()

        return s
