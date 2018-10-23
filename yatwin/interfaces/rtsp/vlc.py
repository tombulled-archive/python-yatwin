from . import constants
import vlc
import time
import os

"""
Library containing functions to interface with 'vlc'
All functions have 'url' as their first parameter

Imports:
    .constants
    vlc
    time
    os

Contains:
    download_audio
    download_snapshot
    download_video
    play_audio
    view_snapshot
    view_video
    embed_video
"""

def download_audio \
        (
            url,
            transcode_acodec = 'flac',
            std_access = 'file',
            std_mux = 'raw',
            std_dst = 'audio.flac',
            duration = 5,
        ):
    """
    Function to download audio from 'url'
    The output file can take on most extensions, just
    ... read the docs for vlc, this is more complicated
    ... than ffmpeg
    Audio will be recorded to 'std_dst'
    ... for 'duration' seconds
    Returns the current working directory + 'std_dst'
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + std_dst

    options = \
        'sout=' + \
            '#transcode' + \
            '{' + \
                'acodec={transcode_acodec}'.format(transcode_acodec = transcode_acodec) + \
            '}:' + \
            'std' + \
            '{' + \
                'access={std_access},'.format(std_access = std_access) + \
                'mux={std_mux},'.format(std_mux = std_mux) + \
                'dst={std_dst}'.format(std_dst = std_dst) + \
            '}'

    instance = vlc.Instance \
    (
        (
            '-Vdummy '
            '-I dummy '
            '--no-sout-video '
            '--sout-audio '
            '--sout-keep'
        )
    )

    player = instance.media_player_new()

    media = instance.media_new(url, options)

    player.set_media(media)

    player.play()

    time.sleep(duration)

    player.stop()

    return path

def download_snapshot(url, file_out='snapshot.png'):
    """
    Function to download a snapshot from 'url'
    Calls vlc.MediaPlayer.video_take_snapshot
    ... so research this to see which extensions
    ... 'file_out' can take on
    Returns the current working directory + 'file_out'
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + file_out

    instance = vlc.Instance('-Vdummy')

    player = instance.media_player_new()

    player.set_mrl(url)

    player.play()

    time.sleep(constants.VLC_SNAPSHOT_WAIT)

    player.video_take_snapshot(0, file_out, 0, 0)

    player.stop()

    return path

def download_video \
        (
            url,
            transcode_vcodec = 'mp4v',
            transcode_vfilter_canvas_width = 1280,
            transcode_vfilter_canvas_height = 720,
            transcode_acodec = 'mp4a',
            std_access = 'file',
            std_mux = 'mp4',
            std_dst = 'video.mp4',
            audio = True,
            duration = 5
        ):
    """
    Function to download video from 'url'
    The output file can take on most extensions, just
    ... read the docs for vlc, this is more complicated
    ... than ffmpeg
    Video will be recorded to 'std_dst'
    ... for 'duration' seconds
    If 'audio' is True, audio will be recorded too
    If 'duration' is not None, returns the current
    ... working directory + 'std_dst'
    If 'duration' is None, returns the vlc.MediaPlayer object
    """

    local_dir = os.getcwd()
    path = local_dir + '\\' + std_dst

    options = \
        'sout=' + \
            '#transcode' + \
            '{' + \
                'vcodec={transcode_vcodec},'.format(transcode_vcodec = transcode_vcodec) + \
                'vfilter=canvas' + \
                '{' + \
                    'width={transcode_vfilter_canvas_width},'.format \
                    (
                        transcode_vfilter_canvas_width = transcode_vfilter_canvas_width
                    ) + \
                    'height={transcode_vfilter_canvas_height}'.format \
                    (
                        transcode_vfilter_canvas_height = transcode_vfilter_canvas_height
                    ) + \
                '}' + \
                (
                    'acodec={transcode_acodec}'.format(transcode_acodec = transcode_acodec)
                        if audio else ''
                ) + \
            '}:' + \
            'std' + \
            '{' + \
                'access={std_access},'.format(std_access = std_access) + \
                'mux={std_mux},'.format(std_mux = std_mux) + \
                'dst={std_dst}'.format(std_dst = std_dst) + \
            '}'

    instance = vlc.Instance('-Vdummy')

    player = instance.media_player_new()

    media = instance.media_new(url, options)

    player.set_media(media)

    player.play()

    if duration is not None:
        time.sleep(duration)

        player.stop()

        return path
    else:
        return player

def play_audio(url, duration = 5):
    """
    Plays audio from 'url' for 'duration' seconds
    This essentially just hides the video output
    ... therefore audio can be slightly delayed
    If 'duration' is not None, returns None
    If 'duration' is None, returns the vlc.MediaPlayer object
    """

    instance = vlc.Instance('-Vdummy')

    player = instance.media_player_new()

    player.set_mrl(url)

    player.play()

    if duration is not None:
        time.sleep(duration)

        player.stop()
    else:
        return player

def view_snapshot(url):
    """
    Opens up a window displaying a snapshot from 'url'
    This window cannot be closed via the GUI
    Returns the vlc.MediaPlayer object
    To destroy the window, call vlc.MediaPlayer.stop
    Will capture frames from 'url' for
    ... .constants.VLC_SNAPSHOT_WAIT seconds
    """

    player = vlc.MediaPlayer(url)

    player.play()

    time.sleep(constants.VLC_SNAPSHOT_WAIT)

    player.pause()

    return player

def view_video(url, audio = True, duration = 10):
    """
    Opens up a window displaying the video
    ... feed from 'url' for 'duration' seconds
    This window cannot be closed via the GUI
    To destroy the window, call vlc.MediaPlayer.stop
    If 'audio' is True, plays the audio too
    If 'duration' is not None, returns None
    If 'duration' is None, return the vlc.MediaPlayer object
    """

    player = vlc.MediaPlayer(url)

    if not audio:
        player.audio_set_mute(True)

    player.play()

    if duration is not None:
        time.sleep(duration)

        player.stop()
    else:
        return player

def embed_video(url, tk_frame):
    """
    Embeds the video stream from 'url' into
    ... the tkinter.Frame 'tk_frame'
    Returns the vlc.MediaPlayer object
    *Remember* to call vlc.MediaPlayer.play so that you
    ... can see the video
    """

    instance = vlc.Instance()
    player = instance.media_player_new()

    media = instance.media_new(url)
    player.set_media(media)

    player.set_hwnd(tk_frame.winfo_id())

    return player
