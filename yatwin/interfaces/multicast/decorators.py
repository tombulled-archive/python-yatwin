import logging
from . import errors

"""
Imports:
    .errors
    logging

Contains:
    assert_attr()
"""

logger = logging.getLogger(__name__)

def assert_attr \
        (
            attr_name,
            not_val = None,
            fatal = True,
            log = True,
            ret_val = None,
            help_message = None,
        ):
    """
    Decorator to raise/warn/fail if
    ... the attribute 'attr_name' is (==) 'not_val'
    """

    def decorator(func):
        """
        Level: assert_attr.decorator
        """

        def wrapper(cls, *args, **kwargs):
            """
            Level: assert_attr.decorator.wrapper
            """

            attr = getattr(cls, attr_name)
            attr_failed = attr == not_val

            error_message = \
            (
                'Attribute assertion failed: '
                f'{attr_name} != {not_val}'
            )

            if help_message is not None:
                error_message += f' ({help_message})'

            if attr_failed:
                if fatal:
                    raise errors.AssertAttrFailed(error_message)
                elif log:
                    logger.error(error_message)

                return ret_val
            else:
                return func(cls, *args, **kwargs)

        return wrapper

    return decorator
