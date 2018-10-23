import pyaudio
import numpy

"""
Library which contains constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution

Imports:
    pyaudio
    numpy
"""

FADE = 200.0
CHANNELS = 1
RATE = 44100
FORMAT = pyaudio.paFloat32
FORMAT_NP = numpy.float32
TONE_DURATION = 0.06
WAIT_GAP = 1
