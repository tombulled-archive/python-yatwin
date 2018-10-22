from . import vlc
from . import ffmpeg
from . import constants

"""
Contains:
    <Rtsp>

Imports:
    .vlc
    .ffmpeg
    .constants
"""

class Rtsp(object):
    """
    Provides methods to interact with the RTSP stream
    """

    def __init__ \
            (
                self,
                host,
                username = constants.DEFAULT_USERNAME,
                password = constants.DEFAULT_PASSWORD,
                port = constants.DEFAULT_PORT,
                endpoint = constants.DEFAULT_ENDPOINT,
            ):
        """
        No rtsplib is available, so this class
        ... provides high-level (basic) interaction with
        ... the camera over rtsp, using .vlc and .ffmpeg

        Initialises class attributes

        Default username: constants.DEFAULT_USERNAME
        Default password: constants.DEFAULT_PASSWORD
        Default port: constants.DEFAULT_PORT
        Default endpoint: constants.DEFAULT_ENDPOINT
        """

        self._init_attrs()

        self.host = host
        self.username = username
        self.password = password
        self.port = port
        self.endpoint = endpoint

        self.url = self._make_url()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@ip:port)[endpoint]>
        """

        return '<{class_name}({username}:{password}@{host}:{port})[{endpoint}]>'.format \
        (
            class_name = self.__class__.__name__,
            username = self.username,
            password = self.password,
            host = self.host,
            port = self.port,
            endpoint = self.endpoint,
        )

    def download_audio(self, *args, **kwargs):
        """
        Direct wrapper for .ffmpeg.download_audio
        """

        return ffmpeg.download_audio(self.url, *args, **kwargs)

    def download_snapshot(self, *args, **kwargs):
        """
        Direct wrapper for .ffmpeg.download_snapshot
        """

        return ffmpeg.download_snapshot(self.url, *args, **kwargs)

    def download_video(self, *args, **kwargs):
        """
        Direct wrapper for .ffmpeg.download_video
        """

        return ffmpeg.download_video(self.url, *args, **kwargs)

    def play_audio(self, *args, **kwargs):
        """
        Direct wrapper for .vlc.play_audio
        """

        return vlc.play_audio(self.url, *args, **kwargs)

    def view_snapshot(self, *args, **kwargs):
        """
        Direct wrapper for .vlc.view_snapshot
        """

        return vlc.view_snapshot(self.url, *args, **kwargs)

    def view_video(self, *args, **kwargs):
        """
        Direct wrapper for .vlc.view_video
        """

        return vlc.view_video(self.url, *args, **kwargs)

    def _make_url(self):
        """
        Generate an rtsp url in the form
        ... rtsp://username:password@host:port/endpoint
        """

        return 'rtsp://{username}:{password}@{host}:{port}/{endpoint}'.format \
        (
            username = self.username,
            password = self.password,
            host = self.host,
            port = self.port,
            endpoint = self.endpoint,
        )

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value
        """

        self.host = None
        self.username = None
        self.password = None
        self.port = None
        self.url = None
        self.endpoint = None
