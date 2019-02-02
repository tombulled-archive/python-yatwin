from .add_to_path import add_to_path

"""
Imports:
    .add_to_path.add_to_path

Contains:
    set_nmap_path()
"""

def set_nmap_path(path):
    """
    Set the Nmap path to {path}

    Note: {path} should be the directory containing
    ... the executable, NOT a path to it
    """

    return add_to_path(path)
