import os

"""
Imports:
    os

Contains:
    set_path
    _set_path_win
"""

ENVIRON_PATH = 'PATH'

def set_path(path):
    """
    Set the PATH environment variable to {path}
    """

    return _set_path_win(path)

def _set_path_win(path):
    """
    Set the PATH environment variable to {path}
    ... on Windows
    """

    os.environ[ENVIRON_PATH] = path
