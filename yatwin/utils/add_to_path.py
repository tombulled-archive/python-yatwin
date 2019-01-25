import os

"""
Imports:
    os

Contains:
    add_to_path()
"""

ENVIRON_PATH = 'PATH'

def add_to_path(path):
    """
    Add {path} to os.environ['PATH']
    """

    os.environ[ENVIRON_PATH] += os.pathsep + path

    return os.environ[ENVIRON_PATH]
