import telnetlib

"""
Library containing decorators for 'telnet'
Designed specifically for <telnet.Telnet>

Contains:
    keep_alive

Imports:
    telnetlib
"""

def keep_alive(function):
    """
    Decorator to keep the telnet session alive

    If the telnet connection is closed, creates
    ... a new one and tries to execute the
    ... function again
    """

    def wrapper(cls, *args, **kwargs):
        """
        Function to wrap the decorated function
        """

        try:
            return function(cls, *args, **kwargs)
        except EOFError as eof_error: # eof_error == 'telnet connection closed'
            cls.Telnet = telnetlib.Telnet \
            (
                cls.host,
                *cls._creation_args,
                **cls._creation_kwargs
            )

            cls._initialise()

            return function(cls, *args, **kwargs)

    return wrapper
