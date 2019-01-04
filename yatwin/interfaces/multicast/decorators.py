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
            fatal = False,
            log = True,
            ret_val = None,
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

            if attr_failed:
                if fatal:
                    raise errors.AssertAttrFailed(error_message)
                elif log:
                    logger.error(error_message)

                return ret_val
            else:
                return func(*args, **kwargs)

        return wrapper

    return decorator
