from .BaseMethod import BaseMethod
from . import decorators
import audioop
import socket
import numpy
import pyaudio
import wave

"""
Imports:
    .BaseMethod.BaseMethod
    .decorators
    audioop
    socket
    numpy
    pyaudio
    wave

Contains:
    <Speaker>
    <Audiostream>
"""

class Speaker:
    """
    Highly specialised class to play audio data using PyAudio

    Designed for use by <Audiostream>
    """

    CHUNK_SZ = 1016

    RATE_HZ = 8000
    NCHANNELS = 1

    def __init__(self):
        """
        Initialises self

        Initialises the PyAudio stream
        """

        self._init_attrs()

        self.PyAudio = pyaudio.PyAudio()

        self.stream = self.PyAudio.open \
        (
            format = pyaudio.paInt16,
            channels = self.NCHANNELS,
            rate = self.RATE_HZ,
            input = True,
            output = True,
            frames_per_buffer = self.CHUNK_SZ
        )

    def __call__(self, *args, **kwargs):
        """
        Disable super().__call__
        """

        return

    def play(self, numpy_buf):
        """
        Plays numpy_buf using the classes PyAudio stream
        """

        signal = wave.struct.pack('%dh' % len(numpy_buf), *list(numpy_buf))

        self.stream.write(signal)

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.PyAudio = None

        self.stream = None

class Audiostream(BaseMethod):
    """
    Inherits from <BaseMethod>

    Provides methods to interact with the audio stream
    """

    HEADER_SZ = 32
    PACKET_SZ = 544
    SAMPLE_SZ = 2

    def __init__(self, *args, **kwargs):
        """
        Initialises the class
        """

        self._init_attrs()

        super().__init__(*args, **kwargs)

        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.Speaker = Speaker()

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def play_stream(self, http=None):
        """
        Plays the live audio stream
        """

        try:
            self.Socket.connect((http.host, http.port))

            url = self._make_endpoint()

            self.Socket.send(f'GET {url} HTTP/1.1\r\n\r\n'.encode())

            while True:
                result = self._handle(self.Socket.recv(self.PACKET_SZ))

                if result:
                    self._play(result)
        finally:
            self.Socket.close()

    def _handle(self, data):
        """
        Handler which formats data into wav format
        """

        # Strip the header at the beginning of the data
        data = data[self.HEADER_SZ:]

        result = b''
        state = None

        # Decompress from ADPCM (differential) to PCM-16L (WAV) format
        for index in range(0, len(data), self.SAMPLE_SZ):
            adpcm_fragment = data[index:index + self.SAMPLE_SZ]

            sample, state = audioop.adpcm2lin \
            (
                adpcm_fragment,
                self.SAMPLE_SZ,
                state
            )

            result += sample

        return result

    def _play(self, data):
        """
        Plays the data through the <Speaker> instance
        """

        self.Speaker.play(numpy.fromstring(data, dtype=numpy.int16))

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def _make_endpoint(self, http=None, streamid=2, filename=''):
        """
        Returns the endpoint with url-formatted parameters
        """

        return \
        (
            f'/{self.endpoint}?'
                f'loginuse={http.username}&'
                f'loginpas={http.password}&'
                f'streamid={streamid}&'
                f'filename={filename}&'
                f'user={http.username}&'
                f'pwd={http.password}'
        )

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.Socket = None
        self.Speaker = None
