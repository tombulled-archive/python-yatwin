"""
Python API for Yatwin IP Cameras (which are Vstarcam cameras)

By default logging is disabled.

Imports:
    logging

Contains:
    _enable_logging

Variables defined here:
    logger
"""

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)

logging.disable(logging.CRITICAL)

from .cameras import BaseCamera
from .cameras import BaseHackedYatwin

def _enable_logging():
    logging.disable(logging.NOTSET)
    logger.info('Logging has been enabled')
