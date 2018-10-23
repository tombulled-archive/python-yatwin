import functools
import logging

"""
Library containing decorators for 'yatwin'

Imports:
    functools
    logging

Contains:
    debug_call
    debug_resp
    debug

Constants defined here:
    MAX_ARG_LEN
    MAX_KEY_LEN
    MAX_RESP_LEN
"""

logger = logging.getLogger(__name__)

MAX_ARG_LEN = 30
MAX_KEY_LEN = 30
MAX_RESP_LEN = 30

def debug_call(logger):
    """
    Decorator that debugs, using logger.debug,
    ... the positional, and keyword arguments
    ... passed to the decorated function

    Example use:

    @debug_call(my_logger)
    def do_something(number, name='Name'):
        pass

    do_something(1, 'Sam')

    Output:
    DEBUG: do_something(1, name='Sam')
    """

    def decorator(func):
        """
        Decorates 'func'

        Level: debug_call.decorator
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wraps 'func'

            Implements functools.wraps to maintain 'func's
            ... __name__ and __doc__

            If arguments are too long, an ellipsis is appended
            ... to the end

            Level: debug_call.decorator.wrapper
            """

            log_args = []

            for arg in args:
                repr_arg = repr(arg).replace('\n', '\\n').replace('\r', '\\r')
                len_arg = len(repr_arg)
                pretty_arg = repr_arg[:MAX_ARG_LEN] + ('...' if len(repr_arg) > MAX_ARG_LEN else '')

                log_args.append(pretty_arg)

            log_args_str = ', '.join(log_args)

            log_kwargs = []

            for key, val in kwargs.items():
                repr_key = str(key).replace('\n', '\\n').replace('\r', '\\r')
                len_key = len(repr_key)
                pretty_key = repr_key[:MAX_KEY_LEN] + ('...' if len(repr_key) > MAX_KEY_LEN else '')

                repr_val = repr(val).replace('\n', '\\n').replace('\r', '\\r')
                len_val = len(repr_val)
                pretty_val = repr_val[:MAX_ARG_LEN] + ('...' if len(repr_val) > MAX_ARG_LEN else '')

                pretty_kwarg = f'{pretty_key}={pretty_val}'

                log_kwargs.append(pretty_kwarg)

            log_kwargs_str = ', '.join(log_kwargs)

            logger.debug \
            (
                f'{func.__name__}'
                '('
                    f'{log_args_str}'
                    f'{", " if log_kwargs and log_args else ""}'
                    f'{log_kwargs_str}'
                ')'
            )

            return func(*args, **kwargs)

        return wrapper

    return decorator

def debug_resp(logger):
    """
    Decorator that debugs, using logger.debug,
    ... the response of the decorated function

    Example use:

    @debug_resp(my_logger)
    def do_something(number, name='Name'):
        return 'Some Output'

    do_something(1, 'Sam')

    Output:
    DEBUG: do_something(...) -> 'Some Output'

    Note: This does not print the arguments passed
    ... to the function
    """

    def decorator(func):
        """
        Decorates 'func'

        Level: debug_resp.decorator
        """

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wraps 'func'

            Implements functools.wraps to maintain 'func's
            ... __name__ and __doc__

            If the response is too long, an ellipsis is appended
            ... to the end

            Level: debug_resp.decorator.wrapper
            """

            resp = func(*args, **kwargs)

            repr_resp = repr(resp).replace('\n', '\\n').replace('\r', '\\r')
            len_resp = len(repr_resp)

            pretty_resp = repr_resp[:MAX_RESP_LEN] + ('...' if len(repr_resp) > MAX_RESP_LEN else '')

            logger.debug(f'{func.__name__}(...) -> {pretty_resp}')

            return resp

        return wrapper

    return decorator

def debug(logger=logger):
    """
    Shorthand for using both:
        debug_call
        debug_resp

    E.g:
        @debug(my_logger)
        def my_func(...):
            ...

        Is equivelant to:

        @debug_call(my_logger)
        @debug_resp(my_logger)
        def my_func(...):
            ...

    Note: You can do @debug(), which will
        use the packages logger
    """

    def decorator(func):
        """
        Decorates 'func'

        Level: debug.decorator
        """

        @debug_call(logger)
        @debug_resp(logger)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            """
            Wraps 'func'

            Implements functools.wraps to maintain 'func's
            ... __name__ and __doc__

            Decorates using:
                @debug_call(logger)
                @debug_resp(logger)
                @functools.wraps(func)

            Level: debug.decorator.wrapper
            """

            return func(*args, **kwargs)

        return wrapper

    return decorator
