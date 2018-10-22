from .. import util

"""
Lots of this code was (pain-stakingly) converted
... from Java to Python from the Java APK Source Code

Contains:
    <DataEncoder>

Constants defined here:
    MAX_APART_LEN

Imports:
    ..util
"""

MAX_APART_LEN = 32

class DataEncoder(object):
    """
    Class for encoding a BSSID and PSK into frequencies
    """

    hexChars = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f')

    def __init__(self, *args, **kwargs):
        """
        Initialises self.
        """

        pass

    def encodeMacWifi(self, _mac, _pwd):
        """
        Taken From Java APK Source Code
        """

        mac = _mac
        pwd = self.String2Bytes(_pwd)

        assert len(mac) <= 16 and len(pwd) <= MAX_APART_LEN

        result = [None for _ in range((len(mac) + len(pwd)) * 2 + 7)]
        encodeLen = len(mac) - 1
        result[0] = self.hexChars[(encodeLen & 0xF)].encode()
        resultLen = 1
        _hexCount, _result = self.char256ToHex(mac, 0, len(mac), result, resultLen)
        resultLen += _hexCount
        result = _result
        _hexCount, _result = self.encodeData(pwd, result, resultLen)
        resultLen += _hexCount
        result = _result

        return ''.join(char.decode() for char in result[0:resultLen])

    def String2Bytes(self, _s):
        """
        Taken From Java APK Source Code
        """

        bytes = None
        try:
            bytes = _s.encode('gbk')
        except Exception as error:
            pass

        if bytes is None:
            bytes = _s.encode()

        return bytes

    def char256ToHex(self, _chars, _charsOff, _charsLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        hexCount = self.char256ToHexCount(_chars, _charsOff, _charsLen)
        _result = self.charsToHex(_chars, _charsOff, hexCount, _result, _resultOff)

        return (hexCount, _result)

    def char256ToHexCount(self, _chars, _charsOff, _charsLen):
        """
        Taken From Java APK Source Code
        """

        return _charsLen * 8 // 4

    def charsToHex(self, _chars, _charsOff, _hexCount, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        for i in range(_hexCount):
            if i % 2 == 0:
                _result[i + _resultOff] = self.hexChars[int(_chars[_charsOff + i // 2].decode()) >> 4 & 0xF].encode()
            else:
                _result[i + _resultOff] = self.hexChars[int(_chars[_charsOff + i // 2].decode()) & 0xF].encode()

        return _result

    def encodeData(self, _data, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        aPartLen = [0]
        Type = self.encodeType(_data, len(_data), aPartLen)
        _hexCount, __result = self.type2Hex(Type, aPartLen[0], _result, _resultOff)
        Len = _hexCount
        _result = __result
        if Type == 1:
            _hexCount, __result = self.lower2Hex(_data, 0, aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
            _hexCount, __result = self.digit2Hex(_data, aPartLen[0], len(_data) - aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 4:
            _hexCount, __result = self.char64ToHex(_data, 0, aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
            _hexCount, __result = self.digit2Hex(_data, aPartLen[0], len(_data) - aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 3:
            _hexCount, __result = self.digit2Hex(_data, 0, aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
            _hexCount, __result = self.char64ToHex(_data, aPartLen[0], len(_data) - aPartLen[0], _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 0:
            _hexCount, __result = self.digit2Hex(_data, 0, len(_data), _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 3:
            _hexCount, __result = self.char256ToHex(_data, 0, len(_data), _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 5:
            _hexCount, __result = self.lower2Hex(_data, 0, len(_data), _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 6:
            _hexCount, __result = self.char64ToHex(_data, 0, len(_data), _result, Len + _resultOff)
            Len += _hexCount
            _result = __result
        elif Type == 7:
            _hexCount, __result = self.upper2Hex(_data, 0, len(_data), _result, Len + _resultOff)
            Len += _hexCount
            _result = __result

        return (Len, _result)

    def encodeType(self, _data, _dataLen, _APartLen):
        """
        Taken From Java APK Source Code
        """

        type0 = True
        type1 = False
        type2 = False
        type3 = True
        type4 = False
        type5 = True
        type6 = True
        type7 = True

        apart1Len = 0
        apart2Len = 0
        apart4Len = 0

        for i in range(_dataLen):
            isDigit_ = util.Util.isDigit(_data[i])
            isLowerChar_ = util.Util.isLowerChar(_data[i])
            isUpperChar_ = util.Util.isUpperChar(_data[i])
            is64Char_ = util.Util.is64Char(_data[i])

            if type0 and not isDigit_:
                type0 = False

                if i > 0:
                    type4 = is64Char_
                    apart4Len = i
            if type4 and not is64Char_:
                type4 = False

            if type5 and not isLowerChar_:
                type5 = False

                if i > 0:
                    type1 = isDigit_
                    apart1Len = i

            if type1 and not isDigit_:
                type1 = False

            if type7 and not isUpperChar_:
                type7 = False

            if type6 and not is64Char_:
                type6 = False

            if type6:
                if i > 0:
                    if not type2 and isDigit_:
                        apart2Len = i

                    type2 = isDigit_
            else:
                type2 = False

        if type0:
            return 0
        if type5:
            return 5
        if type7:
            return 7
        if type1 and apart1Len <= MAX_APART_LEN:
            _APartLen[0] = apart1Len

            return 1
        if type2 and apart2Len <= MAX_APART_LEN:
            _APartLen[0] = apart2Len

            return 2
        if type4:
            if apart4Len >= MAX_APART_LEN:
                apart4Len = MAX_APART_LEN

            _APartLen[0] = apart4Len

            return 4
        if type6:
            return 6

        return 3

    def lower2Hex(self, _chars, _charsOff, _charsLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        hexCount = self.lower2HexCount(_chars, _charsOff, _charsLen)
        tempChars = [b'0' for _ in range(_charsLen)]

        for i in range(_charsLen):
            tempChars = self.bitsSet(tempChars, i * 5, (i + 1) * 5, _chars[i + _charsOff] - 97)

        __result = self.charsToHex(tempChars, 0, hexCount, _result, _resultOff)
        _result = __result
        tempChars = None

        return (hexCount, _result)

    def digit2Hex(self, _chars, _charsOff, _charsLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        for i in range(_charsLen):
            _result[i + _resultOff] = _chars[i + _charsOff]

        return (_charsLen, _result)

    def char64ToHex(self, _chars, _charsOff, _charsLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        hexCount = self.char64ToHexCount(_chars, _charsOff, _charsLen)
        tempChars = [b'0' for _ in range(_charsLen)]

        for i in range(_charsLen):
            tempChars = self.bitsSet(tempChars, i * 6, (i + 1) * 6, util.Util.char64ToInt(_chars[i + _charsOff]))

        _result = self.charsToHex(tempChars, 0, hexCount, _result, _resultOff)
        tempChars = None

        return (hexCount, _result)

    def upper2Hex(self, _chars, _charsOff, _charsLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        hexCount = self.upper2HexCount(_chars, _charsOff, _charsLen)
        tempChars = [b'0' for _ in range(_charsLen)]

        for i in range(_charsLen):
            tempChars = self.bitsSet(tempChars, i * 5, (i + 1) * 5, _chars[i + _charsOff] - 65)

        _result = self.charsToHex(tempChars, 0, hexCount, _result, _resultOff)
        tempChars = None

        return (hexCount, _result)

    def upper2HexCount(self, _chars, _charsOff, _charsLen):
        """
        Taken From Java APK Source Code
        """

        return self.lower2HexCount(_chars, _charsOff, _charsLen)

    def lower2HexCount(self, _chars, _charsOff, _charsLen):
        """
        Taken From Java APK Source Code
        """

        bitsCount = _charsLen * 5

        return bitsCount // 4 + 1 if bitsCount % 4 > 0 else bitsCount // 4

    def char64ToHexCount(self, _chars, _charsOff, _charsLen):
        """
        Taken From Java APK Source Code
        """

        bitsCount = _charsLen * 6

        return bitsCount // 4 + 1 if bitsCount % 4 > 0 else bitsCount // 4

    def bitsSet(self, _bits, _bitsStart, _bitsEnd, _c):
        """
        Taken From Java APK Source Code
        """

        byteStart = _bitsStart // 8
        byteEnd = _bitsEnd // 8

        if byteStart == byteEnd:
            _bits[byteStart] = self.bitSet(_bits[byteStart], _bitsStart % 8, _bitsEnd % 8, _c)
        else:
            assert byteEnd == byteStart + 1

            startPos = _bitsStart % 8
            endPos = _bitsEnd % 8
            startSource = _c >> endPos
            endSource = _c & 255 >> 8 - endPos

            _bits[byteStart] = self.bitSet(_bits[byteStart], startPos, 8, startSource)
            _bits[byteEnd] = self.bitSet(_bits[byteEnd], 0, endPos, endSource)

        return _bits

    def bitSet(self, _desBits, _start, _end, _sourceBits):
        """
        Taken From Java APK Source Code
        """

        x = (255 >> _start if _start > 0 else 255) & (255 << 8 - _end if _end < 8 else 255)

        return str(int(_desBits.decode()) & (x ^ 0xFFFFFFFF) | _sourceBits << 8 - _end & x).encode()

    def type2Hex(self, _type, _aPartLen, _result, _resultOff):
        """
        Taken From Java APK Source Code
        """

        _result[0 + _resultOff] = _type << 1
        hexCount = self.type2HexCount(_type, _aPartLen)

        if hexCount > 1:
            _aPartLen -= 1
            _result[0 + _resultOff] = _result[0 + _resultOff] | (_aPartLen & 0x10) >> 4 #encode?
            _result[1 + _resultOff] = self.hexChars[_aPartLen & 0xF].encode()

        _result[0 + _resultOff] = self.hexChars[_result[0 + _resultOff]].encode()

        return (hexCount, _result)

    def type2HexCount(self, _type, _aPartLen):
        """
        Taken From Java APK Source Code
        """

        if _type == 1 or _type == 2 or _type == 4:
            return 2

        return 1
