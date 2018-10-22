from ..voice.MainActivity import MainActivity
from ..voice.encoder.DataEncoder import DataEncoder
from ..voice.encoder.VoicePlayer import VoicePlayer

"""
Library containing:
    <Encoder>

Imports:
    ..voice.MainActivity.MainActivity
    ..voice.encoder.DataEncoder.DataEncoder
    ..voice.encoder.VoicePlayer.VoicePlayer
"""

class Encoder(object):
    """
    Essentially a minimalist wrapper for ..voice.encoder.DataEncoder.DataEncoder
    Utilising:
        ..voice.MainActivity.MainActivity
        ..voice.encoder.VoicePlayer.VoicePlayer
    """

    @staticmethod
    def encode(bssid, psk):
        """
        Shortcut for:
            Encoder.encode_hex
            Encoder.encode_frequencies
        Encode 'bssid' and 'psk' into 'frequencies'
        """

        enc_hex = Encoder.encode_hex(bssid, psk)
        enc_freq = Encoder.encode_frequencies(enc_hex)

        return enc_freq

    @staticmethod
    def encode_hex(bssid, psk):
        """
        Wrapper for:
            ..voice.MainActivity.MainActivity._to_mac_address
            ..voice.MainActivity.MainActivity._gen_mac_bytes
            ..voice.encoder.DataEncoder.DataEncoder.encodeMacWifi
        Encode 'bssid' and 'psk' into 'hex'
        """

        bssid = bssid.lower().strip()
        psk = psk.strip()

        main = MainActivity()
        encoder = DataEncoder()

        short_bssid = main._to_mac_address(bssid)
        mac = main._gen_mac_bytes(short_bssid)

        encoded = encoder.encodeMacWifi(mac, psk)

        return encoded

    @staticmethod
    def encode_frequencies(enc_hex):
        """
        Wrapper for:
            ..voice.MainActivity.MainActivity._gen_frequencies
            ..voice.encoder.VoicePlayer.VoicePlayer.play
            ..voice.encoder.VoicePlayer.VoicePlayer.doPlay
        Encode 'enc_hex' into 'frequencies'
        """

        enc_hex = enc_hex.lower().strip()

        main = MainActivity()
        player = VoicePlayer()

        frequencies = main._gen_frequencies()

        codes = player.play(enc_hex, 5, 1000, 1)

        return player.doPlay(codes, frequencies, 5, 1000, 1)
