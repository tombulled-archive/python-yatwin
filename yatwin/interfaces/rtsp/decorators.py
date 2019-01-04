from . import errors
import logging

"""
Library containing decorators for: rtsp

Imports:
    .errors
    logging

Contains:
    library_required()
    try_except_raise()
"""

logger = logging.getLogger(__name__)

def try_except_raise(error_message):
    """
    Decorator to try and call the function,
    ... however raises Exception(error_message)
    ... on an error
    """

    def decorator(func):
        """
        Level: try_except_raise.decorator
        """

        def wrapper(*args, **kwargs):
            """
            Level: try_except_raise.decorator.wrapper
            """

            try:
                return func(*args, **kwargs)
            except:
                raise Exception(error_message)

        return wrapper

    return decorator

def library_required \
        (
            library_name,
            library,
            failed_val = None,
            fatal = False,
            log = True,
            ret_val = None,
        ):
    """
    Decorator to raise/warn/fail if
    ... a library failed to be imported
    """

    def decorator(func):
        """
        Level: library_required.decorator
        """

        def wrapper(*args, **kwargs):
            """
            Level: library_required.decorator.wrapper
            """

            import_failed = library == failed_val

            error_message = \
            (
                'Required library failed to '
                f'import: {library_name}'
            )

            if import_failed:
                if fatal:
                    raise errors.ImportFailed(error_message)
                elif log:
                    logger.error(error_message)

                return ret_val
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator
