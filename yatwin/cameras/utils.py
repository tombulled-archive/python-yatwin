from . import decorators
import logging

"""
Library containing utility functions for 'cameras'

Imports:
    .decorators
    logging

Contains:
    create_service
"""

logger = logging.getLogger(__name__)

def create_service(service):
    """
    Function which attempts to return service(*args, **kwargs)
    However, by implementing the try_except decorator,
    ... if an exception is raised, returns None

    Level: create_service
    """

    @decorators.try_except(None)
    def wrapper(*args, **kwargs):
        """
        The create_service wrapper

        Level: create_service.wrapper
        """

        return service(*args, **kwargs)

    return wrapper
