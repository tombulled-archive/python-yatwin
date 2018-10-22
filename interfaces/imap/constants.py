import imaplib

"""
Library which contains constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution
Constants are in upper-case, using underscores (_) to seperate words
... E.g: CONSTANT_NAME = 'constant_value'

Imports:
    imaplib
"""

DOMAIN_GMAIL = 'imap.gmail.com'

DEFAULT_DOMAIN = DOMAIN_GMAIL
DEFAULT_PORT = imaplib.IMAP4_SSL_PORT

IMAPLIB_INBOX = 'INBOX'
IMAPLIB_ALL = 'ALL'
IMAPLIB_RFC_822 = '(RFC822)'
