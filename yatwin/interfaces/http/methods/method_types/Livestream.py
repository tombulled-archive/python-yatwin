from .BaseMethod import BaseMethod
from . import decorators
from ....rtsp import ffmpeg as rtsp_ffmpeg
from ....rtsp import vlc as rtsp_vlc

"""
Imports:
    .BaseMethod.BaseMethod
    .decorators
    ....rtsp.ffmpeg as rtsp_ffmpeg
    ....rtsp.vlc as rtsp_vlc
"""

class Livestream(BaseMethod):
    """
    Inherits from <BaseMethod>

    Provides methods to interact with the live stream
    """

    def __init__(self, *args, **kwargs):
        """
        Initialises super
        """

        self._init_attrs()

        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        """
        Disable super().__call__
        """

        return

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def download_video(self, http=None, file=None, audio=True, **kwargs):
        """
        Downloads the stream as a video

        :param http - The <Http> instance
        :param file - The filename of the video to download
        :param audio - Boolean indicating whether to download audio
        :param **kwargs - **kwargs passes to rtsp_ffmpeg.download_video

        A wrapper for rtsp_ffmpeg.download_video
        """

        if file is None:
            url = self._make_url(http=http, filename='', streamid=10, audio=audio)
        else:
            url = self._make_url(http=http, filename=file, streamid=0, audio=audio)

        kwargs.update(dict(input_kwargs={'f': 'h264'}, output_kwargs={'pix_fmt': 'yuvj420p'}))

        return rtsp_ffmpeg.download_video(url, **kwargs)

    @decorators.kwarg_or_attr('http', attr='Http', not_in=(None,))
    def _make_url(self, http=None, filename='', audio=True, streamid=0):
        """
        Returns the url of the live stream
        ... with the url-formatted parameters
        """

        url = http._make_url \
        (
            f'{self.endpoint}?'
                f'user={http.username}&'
                f'pwd={http.password}&'
                f'streamid={streamid}&'
                f'audio={int(audio)}&'
                f'filename={filename}'
        )

        return url
