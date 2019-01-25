import os

"""
Imports:
    os

Contains:
    set_vlc_path()
"""

ENVIRON_VLC_PATH = 'VLC_PATH'

def set_vlc_path(path):
    """
    Set the VLC path to {path}

    Note: At the moment, by the time this has been
    ... imported, so has VLC. Therefore you must
    ... replicate this function and call it before
    ... anything is imported from yatwin
    """

    os.environ[ENVIRON_VLC_PATH] = path

    return path
