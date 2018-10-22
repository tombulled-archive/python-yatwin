from .network.NetworkScanner import NetworkScanner
from .decoder.Decoder import Decoder
from .encoder.Encoder import Encoder
from .player.Player import Player
from .receiver.Receiver import Receiver

"""
Imports:
    .network.NetworkScanner.NetworkScanner
    .decoder.Decoder.Decoder
    .encoder.Encoder.Encoder
    .player.Player.Player
    .receiver.Receiver.Receiver

Contains:
    <OneKeyWifi>
"""

class OneKeyWifi(object):
    """
    Class packaging together all the basic
    ... onekeywifi methods
    """

    def __init__(self):
        """
        Initialise the class
        """

        self._init_attrs()

        self.NetworkScanner = NetworkScanner()
        self.Decoder = Decoder()
        self.Encoder = Encoder()
        self.Player = Player()
        self.Receiver = Receiver()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name()>
        """

        return f'<{self.__class__.__name__}()>'

    def get_interface(self):
        """
        Wrapper for self.NetworkScanner.get_interface
        """

        return self.NetworkScanner.get_interface()

    def get_networks(self):
        """
        Wrapper for self.NetworkScanner.get_networks
        """

        return self.NetworkScanner.get_networks()

    def decode(self, frequencies, bssids):
        """
        Wrapper for self.Decoder.decode
        """

        return self.Decoder.decode(frequencies, bssids)

    def encode(self, bssid, psk):
        """
        Wrapper for self.Encoder.encode
        """

        return self.Encoder.encode(bssid, psk)

    def play(self, frequencies, play_count=8):
        """
        Wrapper for self.Player.play_frequencies
        """

        self.Player.play_frequencies(frequencies, play_count=play_count)

    #def receive(...): ...

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.NetworkScanner = None
        self.Decoder = None
        self.Encoder = None
        self.Player = None
        self.Receiver = None
