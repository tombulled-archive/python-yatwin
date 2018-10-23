"""
Library which contains Constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution

Contains 'constants' in upper-case, using underscores (_) to seperate words
"""

# Default constants
DEFAULT_USERNAME = '' # ftpd hosts an anonymous server
DEFAULT_PASSWORD = ''
DEFAULT_PORT = 21 # Default FTP port

# FTP status codes
STATUS_CODE_OPERATION_SUCCESSFUL = 230

# FTP commands (https://en.wikipedia.org/wiki/List_of_FTP_commands)
COMMAND_LIST = 'LIST'
COMMAND_HELP = 'HELP'
COMMAND_RETR = 'RETR'
COMMAND_STOR = 'STOR'

# Command timeouts (in seconds)
TIMEOUT = 3
