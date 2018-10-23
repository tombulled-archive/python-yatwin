import ffmpeg
import os

"""
Library containing functions to interface with 'ffmpeg'
All functions have 'url' as their first parameter

Imports:
    ffmpeg
    os

Contains:
    download_audio
    download_snapshot
    download_video

These download methods are superior to vlc's
"""

def download_audio(url, file_out = 'audio.mp3', duration=5):
    """
    Function to download audio from 'url'
    'file_out' can take on most extensions, just
    ... read the docs for ffmpeg
    Audio will be recorded to 'file_out'
    ... for 'duration' seconds
    Returns the current working directory + file_out
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + file_out

    stream = ffmpeg.input(url, t = duration)
    stream = ffmpeg.output(stream, file_out)
    stream = ffmpeg.overwrite_output(stream)

    ffmpeg.run(stream)

    return path

def download_snapshot(url, file_out='snapshot.jpg'):
    """
    Function to download a snapshot from 'url'
    'file_out' can take on most extensions, just
    ... read the docs for ffmpeg
    One frame will be read from 'url', and then
    ... written to 'file_out'
    Returns the current working directory + file_out
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + file_out

    stream = ffmpeg.input(url)
    stream = ffmpeg.output(stream, file_out, vframes = 1)
    stream = ffmpeg.overwrite_output(stream)

    ffmpeg.run(stream)

    return path

def download_video(url, file_out = 'video.mp4', audio = True, duration = 5, input_kwargs={}, output_kwargs={}):
    """
    Function to download video from 'url'
    'file_out' can take on most extensions, just
    ... read the docs for ffmpeg
    Video will be recorded to 'file_out'
    ... for 'duration' seconds
    If 'audio' is True, audio will be recorded too
    Returns the current working directory + file_out
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + file_out

    if not audio:
        output_kwargs.update({'an': None})

    stream = ffmpeg.input(url, t = duration, **input_kwargs)
    stream = ffmpeg.output(stream, file_out, **output_kwargs)
    stream = ffmpeg.overwrite_output(stream)

    out, err = ffmpeg.run(stream, capture_stdout=True, capture_stderr=True)

    return path
