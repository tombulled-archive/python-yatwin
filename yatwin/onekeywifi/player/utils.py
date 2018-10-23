from . import constants
import numpy
import math

"""
Library containing utility functions for the library 'player'

Contains:
    sine
    play_tone

Imports:
    .constants
    numpy
    math
"""

def sine(frequency, length, rate):
    """
    Used by .utils.play_tone
    """

    length = int(length * rate)
    factor = (float(frequency) * (math.pi * 2) / rate)
    return numpy.sin(numpy.arange(length) * factor)

def play_tone(stream, frequency, length, rate=44100, fade=200.):
    """
    Requires .utils.sine
    Plays a tone at 'frequency' HZ for 'length' seconds at 'rate' fps
        with a fade of 'fade'
    A fade is used to avoid clicking sounds
    """

    chunks = [sine(frequency, length, rate)]

    chunk = numpy.concatenate(chunks) * 0.25

    fade_i = int(fade)

    fade_in = numpy.arange(0., 1., 1/fade)
    fade_out = numpy.arange(1., 0., -1/fade)

    chunk[:fade_i] = numpy.multiply(chunk[:fade_i], fade_in)
    chunk[-fade_i:] = numpy.multiply(chunk[-fade_i:], fade_out)

    np_f = chunk.astype(constants.FORMAT_NP)

    stream.write(np_f.tostring())
