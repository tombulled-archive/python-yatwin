from ..CRC import CRC

"""
Lots of this code was (pain-stakingly) converted
... from Java to Python from the Java APK Source Code

Contains:
    <voice>
    <Encoder>
    <VoicePlayer>

Imports:
    ..CRC.CRC
"""

class voice:
    """
    Imitation for importing 'voice'
    ... to be able to access 'CRC'
    """

    CRC = CRC

class Encoder(object):
    """
    Class for encoding data before it can be played
    """

    def __init__(self, callback, sampleRate, bits, bufferSize):
        """
        Initialises self.

        Parameters are currently ignored
        """

        pass

    def encode(self, codes, _frequencies, duration, muteInterval):
        """
        Taken From Java APK Source Code
        """

        freqs = []
        for code_index, code in enumerate(codes):
            index = code

            if index >= 0 and index < len(_frequencies):
                freqs.append(_frequencies[index])
            else:
                raise Exception('Code index error')

        return freqs

class VoicePlayer(object):
    """
    Class for playing frequencies.

    At the moment, audio playing features are not implemented
    """

    mCodeBook = '0123456789abcdef'

    def __init__(self, *args, **kwargs):
        """
        Initialises self.
        """

        pass

    def setFreqs(self, _freqs):
        """
        Sets frequencies

        Not implemented.
        """

        pass

    def play(self, text, _playCount, muteInterval, _priority):
        """
        Plays 'text'

        Not implemented.
        """

        mCodes = self.convertTextToCodes(text)

        if self.mCodeBook and mCodes != None:
            pass # Play here

        return mCodes

    def convertTextToCodes(self, text):
        """
        Taken From Java APK Source Code
        """

        mCodes = None

        if text:
            mCodes = []
            mCodes.append(9)
            mCodes.append(0)
            Len = len(text)
            codeBuffer = [None for _ in range(Len)]

            for i in range(Len):
                ch = text[i]
                index = self.mCodeBook.find(ch)

                if index > -1:
                    codeBuffer[i] = index
                else:
                    mCodes = None
                    raise Exception('invalid character')
                    break

        if mCodes is not None:
            codeBuffer = self.rsEncode(None, codeBuffer)

            preIndex = -1
            fullSignal = ''

            for i in range(Len + 4): # Added +4 because of rsEncode
                index = codeBuffer[i]

                if index != preIndex:
                    mCodes.append(index + 1)
                    preIndex = index
                else:
                    preIndex = 17
                    mCodes.append(preIndex)

                fullSignal += self.mCodeBook[index]

            mCodes.append(18)
            mCodes.append(9)
        else:
            mCodes = None

        return mCodes

    def rsEncode(self, encoder, codeBuffer):
        """
        Taken From Java APK Source Code
        """

        newCodeBuffer = []
        newCodeBuffer = codeBuffer

        crc16 = voice.CRC().calc_crc16(codeBuffer, len(codeBuffer))
        newCodeBuffer.append(crc16 >> 12 & 0xF)
        newCodeBuffer.append(crc16 >> 8 & 0xF)
        newCodeBuffer.append(crc16 >> 4 & 0xF)
        newCodeBuffer.append(crc16 & 0xF)

        return newCodeBuffer

    def doPlay(self, mCodes, frequencies, _playCount, muteInterval, _priority):
        """
        Taken From Java APK Source Code

        Returns data instead of playing it.
        """

        mEncoder = Encoder(None, 44100, 1024, 3)

        return mEncoder.encode(mCodes, frequencies, 65, 0 if _playCount - 1 <= 0 else muteInterval)
