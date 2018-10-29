from . import constants
import ftplib
from typing import *

"""
Library which contains Decorators for 'ftp' and ftplib

Imports:
    ftplib
    typing
    .constants

Contains:
    keep_alive
    callback_store
"""

def keep_alive(func: Callable) -> Callable:
    """
    Decorator to keep an FTP session alive.

    :param func - The function to be 'wrapped' by the decorator
    :returns - The 'wrapped' function

    Attempts to execute 'func'
    If a timeout error is raised, it will re-connect and re-login
    ... and then try again
    If an attribute error is raised, it will re-create the Ftp
    ... session
    """

    def func_wrapper(cls: Type, *args: Any, **kwargs: Any) -> Any:
        """
        Function wrapper created by the keep_alive decorator

        :param cls - Instance of <Ftp>
        :param *args - Arguments to be passed to the wrapped function
        :param **kwargs - Keyword arguments to be passed to the wrapped function
        :returns - The output of the wrapped function
        """

        try:
            return func(cls, *args, **kwargs)
        except ftplib.error_temp as error: # Timeout exception raised
            resp_conn = cls.FTP.connect()
            resp_login = cls.login()

            return func(cls, *args, **kwargs)
        except AttributeError as attribute_error: # Session has been destroyed
            cls.FTP = ftplib.FTP()

            resp_conn = cls.FTP.connect(cls.host, cls.port, timeout=constants.TIMEOUT)
            resp_login = cls.login(cls.username, cls.password)

            return func(cls, *args, **kwargs)
        except ConnectionAbortedError as error_connection_aborted: # An established connection was aborted by the software in your host machine
            resp_conn = cls.FTP.connect()
            resp_login = cls.login()

            return func(cls, *args, **kwargs)

    return func_wrapper

def callback_store(func: Callable, callback_key: str = 'callback', data_append: str = '\n') -> Callable:
    """
    Decorator that adds its own callback to the function

    :param func - The function to be 'wrapped' by the decorator
    :param callback_key - The callback keyword-argument's key
        ... It's unlikely this value needs to be changed
    :param data_append - Seperate each line of input by this string
        ... It's unlikely this value needs to be changed
    :returns - The 'wrapped' function

    Stores each line of input into a string
    ... seperated by 'data_append'
    """

    class func_wrapper(object):
        """
        Class which uses itself as a callback to store
        ... each iteration of input data, which it then
        ... returns
        """

        def __init__(self: Type) -> None:
            """
            Initialises self

            :param self - The class instance
            :returns - None

            Initialises class attributes
            """

            self._init_attrs()

        def __call__(self: Type, *args: Any, **kwargs) -> Any:
            """
            Wrapper for the function

            :param self - The class instance
            :param *args - *args passed to the function
            :param **kwargs - **kwargs passed to the function
            :returns - The output of the wrapped function

            Adds itself as a callback to kwargs using callback_key
            Returns the compiled data
            """

            kwargs.update({callback_key: self.store}) # Add self.store as the callback

            resp = func(*args, **kwargs)

            data = self.data.strip()

            self.data = '' # Reset the value

            return data

        def store(self: Type, data: str) -> None:
            """
            Stores data to a class attribute (self.data)

            :param self - The class instance
            :param data - The data to be stored
            :returns - None
            """

            self.data += data + data_append # Store data + the seperator

        def _init_attrs(self: Type):
            """
            Initialises class attributes

            :param self - The class instance
            :returns - None
            """

            self.data = ''

    wrapper = func_wrapper()

    return wrapper
