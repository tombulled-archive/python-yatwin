from . import utils
from . import constants
import numpy
import pyaudio
import time

"""
Contains:
    <Player>

Import:
    .utils
    .constants
    numpy
    pyaudio
    time
"""

class Player(object):
    """
    Class for playing audio
    Tailored for playing frequencies
    """

    @staticmethod
    def play_frequencies(frequencies, play_count=8):
        """
        @staticmethod
        Play 'frequencies' 'play_count' times using 'pyaudio'
        """

        player = pyaudio.PyAudio()
        stream = player.open(format=constants.FORMAT, channels=constants.CHANNELS, rate=constants.RATE, output=1)

        for _ in range(play_count):
            for freq in frequencies:
                utils.play_tone(stream, freq, constants.TONE_DURATION)

            time.sleep(constants.WAIT_GAP)
