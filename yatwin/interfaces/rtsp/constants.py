from . import ffmpeg
from . import vlc

"""
Library which contains Constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution
Contains 'constants' in upper-case, using underscores (_) to seperate words

Imports:
    .ffmpeg
    .vlc
"""

#FUNCTION_DOWNLOAD_AUDIO = ffmpeg.download_audio
#FUNCTION_DOWNLOAD...

#DEFAULT_AUDIO_PLAY_DURATION = 5
#DEFAULT_AUDIO_DOWNLOAD_DURATION = 5
#DEFAULT_VIDEO_PLAY_DURATION = 5
#DEFAULT_VIDEO_DOWNLOAD_DURATION = 5

VLC_SNAPSHOT_WAIT = 2

DEFAULT_USERNAME = 'admin'
DEFAULT_PASSWORD = '888888'
DEFAULT_PORT = 10554
DEFAULT_ENDPOINT = 'udp/av1_0'
