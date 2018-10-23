from . import constants
import subprocess

"""
Library containing utility functions for netsh

Contains:
    cmd_exec_subprocess

Imports:
    .constants
    subprocess
"""

def cmd_exec_subprocess(command):
    """
    Function to execute a cmd command silently (no shell)
    ... then return its 'stdout' (decoded)
    
    Uses subpocess.Popen
    """

    process = subprocess.Popen \
    (
        command.split(),
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        creationflags = constants.CREATE_NO_WINDOW,
    )

    stdout, stderr = process.communicate()
    stdout = stdout.decode()
    stderr = stderr.decode()

    return stdout
