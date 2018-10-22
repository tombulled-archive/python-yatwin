"""
Library which contains constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution
"""

START_TOKEN = 0
STOP_TOKEN = 18
OVERLAP_TOKEN = 17
MAX_FREQ_COUNT = 19
SIGNAL_SIZE = 10
DEFAULT_CODE_BOOK = "0123456789abcdef"
DEFAULT_BUFFER_SIZE = 1024
DEFAULT_OVERLAP_SIZE = 512
DEFAULT_BUFFER_COUNT = 3
DEFAULT_SAMPLE_RATE = 44100
CODE_FREQUENCY = [15000, 15200, 15400, 15600, 15800, 16000, 16200, 16400, 16600, 16800, 17000, 17200, 17400, 17600, 17800, 18000, 18200, 18400, 18600]
MIN_FREQUENCY = 14800
MAX_FREQUENCY = 18800
TestSignal = "0ce0a6a088"
TestFullSignal = "1f0fee123456782f5bb"
