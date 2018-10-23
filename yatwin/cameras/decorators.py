import logging

"""
Library containing decorators for 'cameras'

Imports:
    logging

Contains:
    try_except
    create_service
"""

logger = logging.getLogger(__name__)

def try_except(val):
    """
    Returns a decorator, which returns a wrapper,
    ... which attempts to call the decorated function,
    ... however, upon an exception being raised, it
    ... returns 'val'
    Level: try_except
    """

    def decorator(func):
        """
        The try_except decorator

        Level: try_except.decorator
        """

        def wrapper(*args, **kwargs):
            """
            The try_except wrapper

            Level: try_except.decorator.wrapper
            """

            try:
                return func(*args, **kwargs)
            except:
                return val

        return wrapper

    return decorator

def create_service(service):
    """
    Decorator which attempts to call service(*args, **kwargs)
    However, by implementing the try_except decorator,
    ... if an exception is raised, returns None

    Level: create_service
    """

    @try_except(None)
    def wrapper(*args, **kwargs):
        """
        The create_service wrapper

        Level: create_service.wrapper
        """

        return service(*args, **kwargs)

    return wrapper
