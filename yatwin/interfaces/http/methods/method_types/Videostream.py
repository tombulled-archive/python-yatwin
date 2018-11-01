from .BaseMethod import BaseMethod
from . import decorators
from ....rtsp import ffmpeg as rtsp_ffmpeg
from ....rtsp import vlc as rtsp_vlc
from ... import parameters
import socket
import numpy
import cv2

"""
Imports:
    .BaseMethod.BaseMethod
    .decorators
    ....rtsp.ffmpeg as rtsp_ffmpeg
    ....rtsp.vlc as rtsp_vlc
    socket
    numpy
    cv2
"""

class Videostream(BaseMethod):
    """
    Inherits from <BaseMethod>

    Provides methods to interact with the video stream
    """

    PACKET_SIZE = 1024

    def __init__(self, *args, **kwargs):
        """
        Initialises self
        Initialises super
        """

        self._init_attrs()

        super().__init__(*args, **kwargs)

        self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __call__(self, *args, **kwargs):
        """
        Disable super().__call__
        """

        return

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def embed_video(self, http=None, **kwargs):
        """
        Wrapper for rtsp_vlc.embed_video
        """

        url = self._make_url(http=http)

        return rtsp_vlc.embed_video(url, **kwargs)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def view_snapshot(self, http=None, **kwargs):
        """
        Wrapper for rtsp_vlc.view_snapshot
        """

        url = self._make_url(http=http)

        return rtsp_vlc.view_snapshot(url, **kwargs)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def download_snapshot(self, http=None, **kwargs):
        """
        Wrapper for rtsp_ffmpeg.download_snapshot
        """

        url = self._make_url(http=http)

        return rtsp_ffmpeg.download_snapshot(url, **kwargs)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def download_video(self, http=None, **kwargs):
        """
        Wrapper for rtsp_ffmpeg.download_video
        """

        url = self._make_url(http=http)

        return rtsp_ffmpeg.download_video(url, **kwargs)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def view_video(self, http=None):
        """
        Wrapper for self.view_video_cv2
        """

        return self.view_video_cv2(http=http)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def view_video_cv2(self, http=None):
        """
        Requests frames over a raw http socket
        Displays them using cv2.imshow
        """

        self._endpoint = self._make_endpoint(http=http)

        try:
            self.Socket.connect((http.host, http.port))
        except:
            self.Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            self.Socket.send(f'GET {self._endpoint} HTTP/1.1\r\n\r\n'.encode())

            while True:
                result = self._handle(self.Socket.recv(self.PACKET_SIZE))

                if result:
                    self._show_video(result)
        finally:
            self.Socket.close()

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def view_video_vlc(self, http=None, **kwargs):
        """
        Wrapper for rtsp_vlc.view_video
        """

        url = self._make_url(http=http)

        return rtsp_vlc.view_video(url, audio=False, **kwargs)

    def _handle(self, data):
        """
        Handles the data, slicing it into a jpeg frame
        """

        self.bytes += data

        a = self.bytes.find(b'\xff\xd8')
        b = self.bytes.find(b'\xff\xd9')

        if a != -1 and b != -1:
            jpg = self.bytes[a:b+2]
            self.bytes = self.bytes[b+2:]

            return jpg

    @staticmethod
    def _show_video(jpg):
        """
        Shows a singular jpg frame using cv2.imshow
        """

        img = cv2.imdecode(numpy.fromstring(jpg, dtype=numpy.uint8), cv2.IMREAD_COLOR)

        cv2.imshow('i',img)

        if cv2.waitKey(1) == 27:
            exit(0)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def _make_endpoint(self, http=None):
        """
        Returns the endpoint with http-formatted parameters
        """

        return \
        (
            f'/{self.endpoint}?'
                f'loginuse={http.username}&'
                f'loginpas={http.password}'
        )

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def _make_url(self, http=None):
        """
        Returns the full http url for the video stream
        """

        return http._make_url(self.endpoint)

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.bytes = b''

        self.Socket = None

        self._endpoint = None
