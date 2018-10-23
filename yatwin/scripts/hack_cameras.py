from .. import scripts
from .. import cameras
from .. import interfaces
from .. import decorators
import logging

"""
Imports:
    ..scripts
    ..cameras
    ..interfaces
    ..decorators
    logging

Contains:
    hack_cameras
    hack_camera
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def hack_cameras(aim=1):
    """
    Wrapper for ..scripts.find_cameras(max_interest=aim)
    ... which then hacks the cameras interfaces

    Returns cameras as <BaseHackedYatwin> instances
    """

    raw_cameras = scripts.find_cameras(max_interest=aim)

    logger.debug(f'Found {len(raw_cameras)} cameras')

    cameras = []

    for camera_index, raw_camera in enumerate(raw_cameras):
        host = raw_camera['Host']
        onvif_port = raw_camera['Port']

        logger.debug(f'Camera{camera_index + 1}: host={host}, onvif_port={onvif_port}')

        cam = hack_camera(host, onvif_port)

        cameras.append(cam)

    return cameras

@decorators.debug()
def hack_camera(host, onvif_port=interfaces.onvif.constants.DEFAULT_PORT):
    """
    Hacks the cameras interfaces
    Returns the camera as a <BaseHackedYatwin> instance
    """

    cam = cameras.BaseHackedYatwin(host, onvif_port)

    return cam
