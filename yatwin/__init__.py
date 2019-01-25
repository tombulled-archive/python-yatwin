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

from . import utils
import os

PATH = utils.get_path()
_PATH = os.environ['PATH']

# Set the environ PATH to the systems PATH
# ... This fixes a bug with python-nmap not
# ... finding Nmap in the PATH
# This bug may be because of WinPython
utils.set_path(PATH)

def _enable_logging():
    """
    Enable logging
    """

    logging.disable(logging.NOTSET)
    logger.info('Logging has been enabled')
