from ..voice.MainActivity import MainActivity
from ..voice.decoder.DataDecoder import DataDecoder

"""
Contains:
    <Decoder>

Imports:
    ..voice.MainActivity.MainActivity
    ..voice.decoder.DataDecoder
"""

class Decoder(object):
    """
    Essentially a minimalist wrapper for ..voice.decoder.DataDecoder
    """

    @staticmethod
    def decode(frequencies, bssids):
        """
        Decode 'frequencies' into (bssid, psk) using 'bssids'
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder.decode
        available_frequencies defaults to
            ..voice.MainActivity.MainActivity._gen_frequencies()

        :param frequencies - A list of frequencies to be decoded.
        :param bssids - A list of BSSID's on the network to cross
        ... reference the decoded BSSID endpoint against
        """

        main = MainActivity()
        decoder = DataDecoder()

        available_frequencies = main._gen_frequencies()

        return decoder.decode(frequencies, available_frequencies, bssids)

    @staticmethod
    def decode_hex(frequencies):
        """
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder._hex_from_frequencies
        Decode 'frequencies' into hex
        available_frequencies defaults to
            ..voice.MainActivity.MainActivity._gen_frequencies()
        """

        main = MainActivity()
        decoder = DataDecoder()

        available_frequencies = main._gen_frequencies()

        enc_hex = decoder._hex_from_frequencies(frequencies, available_frequencies)

        return enc_hec

    @staticmethod
    def decode_mac(enc_hex):
        """
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder._mac_psk_hex_from_hex
        Decode 'enc_hex' into ('mac', 'enc_psk')
            where 'mac' is the end of the bssid e.g. 'a2fe'
            and 'enc_psk' is the psk encoded in hex
        Returns 'mac'
        """

        decoder = DataDecoder()

        mac, enc_psk = decoder._mac_psk_hex_from_hex(enc_hex)

        return mac

    @staticmethod
    def decode_psk_hex(enc_hex):
        """
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder._mac_psk_hex_from_hex
        Decode 'enc_hex' into ('mac', 'enc_psk')
            where 'mac' is the end of the bssid e.g. 'a2fe'
            and 'enc_psk' is the psk encoded in hex
        Returns 'enc_psk'
        """

        decoder = DataDecoder()

        mac, enc_psk = decoder._mac_psk_hex_from_hex(enc_hex)

        return enc_psk

    @staticmethod
    def decode_psk(psk_hex):
        """
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder._psk_from_psk_hex
        Decode 'psk_hex' into a plain-text 'psk'
        """

        decoder = DataDecoder()

        psk = decoder._psk_from_psk_hex(psk_hex)

        return psk

    @staticmethod
    def decode_bssid(mac, bssids):
        """
        Wrapper for ..voice.decoder.DataDecoder.DataDecoder._bssid_from_mac
        Decode 'mac' into a 'bssid' using 'bssids'
        """

        decoder = DataDecoder()

        bssid = decoder._bssid_from_mac(mac, bssids)

        return bssid
