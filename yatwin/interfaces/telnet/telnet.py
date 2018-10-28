from . import constants
from . import errors
from . import decorators
import telnetlib
import random
import socket

"""
Library which contains:
    <Telnet>

Imports:
    .constants
    .errors
    .decorators
    telnetlib
    random
    socket
"""

class Telnet(object):
    """
    Indirect wrapper for telnetlib.Telnet (https://docs.python.org/3/library/telnetlib.html#telnetlib.Telnet)
    """

    def __init__ \
            (
                self,
                host,
                *args,
                username = constants.DEFAULT_USERNAME,
                password = constants.DEFAULT_PASSWORD,
                port = constants.DEFAULT_PORT,
                **kwargs
            ):
        """
        Initialises super
        Initialises class attributes
        Logs into telnet session (https://docs.python.org/3/library/telnetlib.html#telnet-example)
        Attempts to read-off the banner (Welcome to HiLinux.)
        If login failed, raises errors.LoginFailed

        Default username: constants.DEFAULT_USERNAME
        Default password: constants.DEFAULT_PASSWORD
        """

        kwargs.update({'timeout': constants.TIMEOUT_GENERAL})

        try:
            self.Telnet = telnetlib.Telnet(host, *args, port=port, **kwargs)
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

        self._creation_args = args
        self._creation_kwargs = kwargs

        self._init_attrs()

        self.username = username
        self.password = password
        self.host = host
        self.port = port

        self._initialise()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@ip:port)>
        """

        return '<{name}({username}:{password}@{ip}:{port})>'.format \
        (
            name = self.__class__.__name__,
            username = self.username,
            password = self.password,
            ip = self.host,
            port = self.port,
        )

    def __call__(self, *args, **kwargs):
        """
        Shorthand wrapper for self.execute
        """

        return self.execute(*args, **kwargs)

    def login(self):
        """
        Login to the telnet session (https://docs.python.org/3/library/telnetlib.html#telnet-example)
        Called automatically by __init__
        Reads up until 'login: ' (constants.FLAG_LOGIN)
        Sends username
        Reads up until 'Password: ' (constants.FLAG_PASSWORD)
        Sends password
        """

        self.Telnet.read_until(constants.FLAG_LOGIN, timeout=constants.TIMEOUT_GENERAL)
        self.Telnet.write(self.username.encode('ascii') + constants.LF)

        if self.password:
            self.Telnet.read_until(constants.FLAG_PASSWORD, timeout=constants.TIMEOUT_GENERAL)
            self.Telnet.write(self.password.encode('ascii') + constants.LF)

    def execute(self, command):
        """
        Calls the appropriate execution function, depending on constants.EXECUTION_MODE
        E.g. constants.EXECUTION_MODE_HASH -> self.hash_execute
        """

        exec_func = self.exec_mode_map.get(constants.EXECUTION_MODE, None)

        if exec_func is None:
            raise errors.InvalidExecutionMode \
            (
                'Unrecognised execution mode \'{mode}\''.format \
                (
                    mode = constants.EXECUTION_MODE
                )
            )

        return exec_func(command)

    def hash_execute(self, command):
        """
        For when constants.EXECUTION_MODE == constants.EXECUTION_MODE_HASH
        Adds a randomly generated flag to the end of the output
        ... to ensure all output of 'command' is captured and returned
        Only for use with commands that will eventually return the prompt
        ... (constants.FLAG_PROMPT)
        This is the recommended mode of execution
        Instead of executing:
            # command
        It will execute:
            # command && echo flag
        Then will capture all data until it sees the flag
        """

        flag = str(random.getrandbits(constants.HASH_BITS))

        comm_line = '{command} && echo \'{flag}\''.format(command=command, flag=flag).encode()

        exp_line = constants.CRLF + flag.encode() + constants.FLAG_PROMPT

        return self._execute(comm_line, exp_line)


    def basic_execute(self, command):
        """
        For when constants.EXECUTION_MODE == constants.EXECUTION_MODE_BASIC
        Only for use with commands that will eventually return the prompt
        ... (constants.FLAG_PROMPT)
        This is the most basic mode of execution
        Will capture all data until it sees the first prompt
        """

        comm_line = command.encode()
        exp_line = constants.FLAG_PROMPT

        return self._execute(comm_line, exp_line)

    def execute_bg(self, command):
        """
        For use with commands that won't return a prompt, e.g. 'top'
        This is equivelant to executing the command with an ampersand at the end
        ... (https://www.javatpoint.com/linux-ampersand)
        ... the function will add the ampersand (&) for you, do not do it yourself
        Telnet will not return a prompt, so it gets faked using 'echo'
        Insted of executing:
            # command &
        It will execute:
            # (command &) && echo '# '
        """

        comm_line = f'({command} &) && echo \'# \''.encode()

        exp_line = comm_line

        return self._execute(comm_line, exp_line)

    def ls(self, directory=''):
        """
        Executes: ls {directory}
        Uses basic execution

        :param directory - directory to list, leave as '' for current directory
        """

        return self.basic_execute(f'{constants.COMMAND_LS} {directory}')

    def top(self):
        """
        Executes: top -n 1
        Uses basic execution
        """

        return self.basic_execute(f'{constants.COMMAND_TOP} -n 1')

    def pwd(self):
        """
        Executes: pwd
        Uses basic execution
        """

        return self.basic_execute(f'{constants.COMMAND_PWD}')

    def whoami(self):
        """
        Executes: whoami
        Uses basic execution
        """

        return self.basic_execute(f'{constants.COMMAND_WHOAMI}')

    def exit(self):
        """
        Executes: exit
        Uses basic execution
        """

        return self.basic_execute(f'{constants.COMMAND_EXIT}')

    def cd(self, directory='/'):
        """
        Executes: cd {directory}
        Uses basic execution

        :param directory - defaults to '/'
        """

        return self.basic_execute(f'{constants.COMMAND_CD} {directory}')

    def ps(self):
        """
        Executes: ps
        Uses basic execution
        """

        return self.basic_execute(f'{constants.COMMAND_PS}')

    def _initialise(self):
        self.login()

        banner = self.Telnet.read_until(constants.FLAG_PROMPT, timeout=constants.TIMEOUT_LOGIN)

        if constants.FLAG_LOGIN_FAILED in banner:
            raise errors.LoginFailed('Login incorrect')
        else:
            self.banner = self._decode_resp(banner)

    @decorators.keep_alive
    def _execute(self, comm_line, exp_line = constants.FLAG_PROMPT):
        """
        The underlying execute function
        This sends comm_line, then reads all data until it sees exp_line
        The output is decoded using _decode_resp, then returned
        """

        self.Telnet.write(comm_line + constants.LF)

        raw_resp = self.Telnet.read_until(exp_line, timeout=constants.TIMEOUT_GENERAL)

        return self._decode_resp(raw_resp, comm_line, exp_line)

    def _decode_resp(self, resp, comm_line = None, exp_line = None):
        """
        Strips the executed command (comm_line) from the left of resp
        Strips the expected line (exp_line) from the right of resp
        Removes Colourization and other unwanted (?) data
        Returns the decoded resp as a stripped string
        """

        resp = resp.replace(b'\r\r\n', b'') # Long data wraps over multiple lines

        if comm_line is not None:
            lstrip_data = comm_line

            if resp.startswith(lstrip_data):
                resp = resp[len(lstrip_data):]

        if exp_line is not None:
            rstrip_data = exp_line

            if resp.endswith(rstrip_data):
                resp = resp[:-(len(rstrip_data))]

        if resp.endswith(constants.FLAG_PROMPT):
            resp = resp[:-len(constants.FLAG_PROMPT)]

        resp = resp.replace(b'\x1b[0m', b'')
        resp = resp.replace(b'\x1b[1;34m', b'') # Dark Blue
        resp = resp.replace(b'\x1b[1;32m', b'') # Light Blue
        resp = resp.replace(b'\x1b[1;36m', b'') # Green
        resp = resp.replace(b'\x1b[1;35m', b'') # Pink
        resp = resp.replace(b'\x1b[0;0m', b'') # Grey (White?)
        resp = resp.replace(b'\x1b[0;39m', b'') # Telnet banner
        resp = resp.replace(b'\x1b[H', b'') # Top of 'ps'
        resp = resp.replace(b'\x1b[J', b'') # Top of 'ps'
        resp = resp.replace(b'\x1b[7m', b'') # White bg, Black fg ('ps')
        resp = resp.replace(constants.CRLF, constants.LF)

        return resp.decode().strip()

    def _get_banner(self):
        """
        Returns the decoded banner which gets
        ... read-off after a successfull login
        """

        banner = self.banner

        prompt = constants.FLAG_PROMPT.decode().replace('\r\n', '\n').rstrip()

        if banner.endswith(prompt):
            banner = banner[:-len(prompt)]

            banner = banner.strip()

        return banner

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default value
        """

        self.username = ''
        self.password = ''
        self.host = None
        self.port = None

        self._creation_args = ()
        self._creation_kwargs = {}

        self.exec_mode_map = \
        {
            constants.EXECUTION_MODE_HASH: self.hash_execute,
            constants.EXECUTION_MODE_BASIC: self.basic_execute,
        }

        self.banner = None
