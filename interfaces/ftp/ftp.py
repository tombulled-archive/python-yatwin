from . import constants
from . import errors
from . import decorators
import ftplib
import os
import os.path
import socket

"""
Imports:
    .constants
    .errors
    .decorators
    ftplib
    os
    os.path
    socket

Contains:
    <Ftp>
"""

class Ftp(object):
    """
    Indirect wrapper for ftplib.FTP (https://docs.python.org/3/library/ftplib.html#ftplib.FTP)
    """
    
    def __init__ \
            (
                self,
                host,
                port = constants.DEFAULT_PORT,
                username = constants.DEFAULT_USERNAME,
                password = constants.DEFAULT_PASSWORD,
            ):
        """
        Initialises self
        Initialises class attributes

        Connects, and logs into the ftp session (https://docs.python.org/3/library/ftplib.html#module-ftplib)

        Default username: constants.DEFAULT_USERNAME
        Default password: constants.DEFAULT_PASSWORD
        """

        self._init_attrs()

        self.FTP = ftplib.FTP()

        try:
            self.FTP.connect(host, port, timeout=constants.TIMEOUT)
        except (TimeoutError, socket.timeout) as error_timeout:
            raise errors.TimeoutError \
            (
                'A connection attempt failed because the connected '
                'party did not properly respond after a period of '
                'time, or established connection failed because '
                'connected host has failed to respond'
            )
        except ConnectionRefusedError as error_refused:
            raise errors.ConnectionRefusedError \
            (
                'No connection could be made because the target '
                'machine actively refused it'
            )

        self.FTP.login(username, password)

        self.host = host
        self.username = username
        self.password = password
        self.port = port

        self.login()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@ip:port)>
        """

        return '<{class_name}({username}:{password}@{ip}:{port})>'.format \
        (
            class_name = self.__class__.__name__,
            username = self.username,
            password = self.password,
            ip = self.host,
            port = self.port,
        )

    def login(self, *args, **kwargs):
        """
        Login to the ftp session (https://docs.python.org/3/library/ftplib.html#module-ftplib)

        If login failed, raises <errors.LoginFailed>
        """

        resp = self.FTP.login(*args, **kwargs)

        if not resp.strip().startswith(str(constants.STATUS_CODE_OPERATION_SUCCESSFUL)):
            raise errors.LoginFailed('Invalid username or password')

        return resp

    @decorators.keep_alive
    def pwd(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.pwd implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.pwd(*args, **kwargs)

    @decorators.keep_alive
    @decorators.callback_store
    def ls(self, directory = '', **kwargs):
        """
        Wrapper for ftplib.FTP.retrlines('LIST')
        ... implementing the decorators:
        ...     @decorators.keep_alive,
        ...     @decorators.callback_store
        """

        comm_ext = '' if not directory else ' ' + directory

        return self.FTP.retrlines(constants.COMMAND_LIST + comm_ext, **kwargs)

    @decorators.keep_alive
    def exit(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.quit implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.quit(*args, **kwargs)

    @decorators.keep_alive
    def rm(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.delete implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.delete(*args, **kwargs)

    @decorators.keep_alive
    def cd(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.cwd implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.cwd(*args, **kwargs)

    @decorators.keep_alive
    def mkdir(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.mkd implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.mkd(*args, **kwargs)

    @decorators.keep_alive
    def rmdir(self, *args, **kwargs):
        """
        Wrapper for ftplib.FTP.rmd implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.rmd(*args, **kwargs)

    @decorators.keep_alive
    def get(self, file_in, file_out=None):
        """
        Wrapper for ftplib.FTP.retrbinary implementing
        ... the decorator @decorators.keep_alive
        Requests the contents of 'file_in' from the server
        ... then writes it into 'file_out'
        'file_out' will be written to inside of self.local_directory
        If 'file_out' is None, it takes on the file name
        ... of 'file_in'
        """

        if file_out is None:
            file_out = os.path.basename(file_in)

        with open(self.local_directory + file_out, 'wb') as file:
            self.FTP.retrbinary(constants.COMMAND_RETR + ' ' + file_in, callback = file.write)

    @decorators.keep_alive
    def help(self):
        """
        Wrapper for ftplib.FTP.sendcmd('HELP') implementing
        ... the decorator @decorators.keep_alive
        """

        return self.FTP.sendcmd(constants.COMMAND_HELP)

    @decorators.keep_alive
    def put(self, file_in, file_out=None):
        """
        Wrapper for ftplib.FTP.storbinary implementing
        ... the decorator @decorators.keep_alive
        Sends the contents of 'file_in' to the server
        ... to be written to 'file_out'
        'file_in' will be read from inside of self.local_directory
        If 'file_out' is None, it takes on the file name
        ... of 'file_in'
        If 'file_in' does not exist, it is created as an empty file
        ... similair to Linux's 'touch'
        """

        if file_out is None:
            file_out = os.path.basename(file_in)

        if not os.path.isfile(self.local_directory + file_in):
            with open(self.local_directory + file_in, 'w') as file:
                pass

        with open(self.local_directory + file_in, 'rb') as file:
            self.FTP.storbinary(constants.COMMAND_STOR + ' ' + file_out, file)

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value
        """

        self.host = None
        self.username = ''
        self.password = ''
        self.port = None
        self.local_directory = os.getcwd() + '\\'
