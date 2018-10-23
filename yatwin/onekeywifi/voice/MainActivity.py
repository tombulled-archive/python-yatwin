from .encoder.DataEncoder import DataEncoder
from .encoder.VoicePlayer import VoicePlayer
import ast

"""
Lots of this code was (pain-stakingly) converted
... from Java to Python from the Java APK Source Code

Contains:
    <MainActivity>

Imports:
    .encoder.DataEncoder.DataEncoder
    .encoder.VoicePlayer.VoicePlayer
    ast
"""

class MainActivity(object):
    """
    Main Activity class.
    This appears to pull together a lot of the
    ... onekeywifi functionality

    Taken from Java APK Source Code
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises self
        """

        pass

    def _gen_mac_bytes(self, mac):
        """
        Taken From Java APK Source Code
        """

        midbytes = None

        try:
            midbytes = self.HexString2Bytes(mac)
        except Exception as error:
            raise

        if len(midbytes) > 6:
            raise Exception('No Support: AP BSSID too long')

        b = []
        num = 0

        if len(midbytes) == 2:
            b = [midbytes[0], midbytes[1]]
            num = 2
        elif len(midbytes) == 3:
            b = [midbytes[0], midbytes[1], midbytes[2]]
            num = 3
        elif len(midbytes) == 4:
            b = [midbytes[0], midbytes[1], midbytes[2], midbytes[3]]
            num = 4
        elif len(midbytes) == 5:
            b = [midbytes[0], midbytes[1], midbytes[2], midbytes[3]. midbytes[4]]
            num = 5
        elif len(midbytes) == 6:
            b = [midbytes[0], midbytes[1], midbytes[2], midbytes[3]. midbytes[4], midbytes[5]]
            num = 6
        elif len(midbytes) == 1:
            b = [midbytes[0]]
            num = 1

        return b

    def _gen_frequencies(self):
        """
        Taken From Java APK Source Code
        """

        a = [6500]

        for i in range(18):
            a.append(a[i] + 200)

        return a

    def HexString2Bytes(self, src):
        """
        Taken From Java APK Source Code
        """

        ret = []
        tmp = src.encode()

        for i in range(len(src) // 2):
            ret.append(str(self.uniteBytes(tmp[i * 2], tmp[i * 2 + 1])).encode())

        return ret

    def uniteBytes(self, src0, src1):
        """
        Taken From Java APK Source Code
        """

        _b0 = ast.literal_eval('0x' + chr(src0))
        _b0 = self._int_to_byte(_b0 << 4)
        _b1 = ast.literal_eval('0x' + chr(src1))
        ret = self._int_to_byte(_b0 ^ _b1)

        return ret

    def _int_to_byte(self, integer):
        """
        Taken From Java APK Source Code
        """

        if integer > 127:
            return integer - 256

        return integer

    @staticmethod
    def _to_mac_address(bssid, _bytes=2):
        """
        Returns the last '_bytes' bytes of bssid
        """

        bssid = bssid.lower().strip()
        return ''.join(bssid.split(':')[-_bytes:])

    @staticmethod
    def _to_mac_address_deprecated(self, bssid):
        """
        Taken From Java APK Source Code
        """
        tomacaddress = bssid.split(':')
        currentLen = len(bssid)

        mList = [bssid]

        sendMac = None

        for m in range(currentLen - 1, -1, -1):
            for j in range(len(mList) - 1, -1, -1):
                if bssid != mList[j]:
                    array = mList[j].split(':')
                    if tomacaddress[m] != array[m]:
                        mList.pop(j)

            if len(mList) == 1 or len(mList) == 0:
                if m == 5:
                    sendMac = str(tomacaddress[m])
                elif m == 4:
                    sendMac = str(tomacaddress[m]) + str(tomacaddress[m + 1])
                else:
                    sendMac = str(tomacaddress[5]) + str(tomacaddress[4]) + str(tomacaddress[3])
                break

        return sendMac
