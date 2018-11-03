"""
Library which contains Constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution
"""

DEFAULT_USERNAME = '' # 'vstarcam2017'
DEFAULT_PASSWORD = '' # '20170912'
DEFAULT_PORT = 23

KNOWN_LOGINS = \
(
    (
        'vstarcam2017',
        '20170912',
    ),
    (
        'vstarcam2015',
        '20150602',
    ),
    (
        'root',
        '123456',
    ),
    (
        '',
        '',
    ),
)

FLAG_LOGIN = b'login: '
FLAG_PASSWORD = b'Password: '
FLAG_LOGIN_FAILED = b'Login incorrect'

FLAG_PROMPT = b'\r\n# '

LF = b'\n'
CRLF = b'\r\n'

EXECUTION_MODE_HASH = 'hash'
EXECUTION_MODE_BASIC = 'basic'

HASH_BITS = 128

EXECUTION_MODE = EXECUTION_MODE_HASH

CONTROL_C = '\x03'

TIMEOUT_LOGIN = 4
TIMEOUT_GENERAL = 4

FILE_STARTUP = '/system/init/ipcam.sh'
FILE_FTP_TEST = '/tmp/ftpupload.sh'

COMMAND_LS = 'ls'
COMMAND_TOP = 'top'
COMMAND_PWD = 'pwd'
COMMAND_WHOAMI = 'whoami'
COMMAND_EXIT = 'exit'
COMMAND_CD = 'cd'
COMMAND_PS = 'ps'
