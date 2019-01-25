import winreg
import os

"""
Imports:
    winreg
    os

Contains:
    get_path
    _get_path_win
    _get_reg
"""

def get_path():
    """
    Get the systems PATH variable
    """

    return _get_path_win()

def _get_path_win():
    """
    Get the PATH on Windows
    """

    USER_PATH = _get_reg \
    (
        winreg.HKEY_CURRENT_USER,
        'Environment',
        'Path',
    )
    LOCAL_PATH = _get_reg \
    (
        winreg.HKEY_LOCAL_MACHINE,
        r'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
        'Path',
    )

    PATH = LOCAL_PATH + os.pathsep + USER_PATH

    return PATH

def _get_reg(hkey, path, key):
    """
    Open the registrey path located at {hkey}\{path}
    ... and return the value of the key {key}

    Note: For Windows
    """

    reg_key = winreg.OpenKey(hkey, path)

    val = winreg.QueryValueEx(reg_key, key)[0]

    return val
