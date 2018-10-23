from .find_devices import find_devices
from ..utils import disect_url
from .. import decorators
import logging

"""
Imports:
    .find_devices.find_devices
    ..utils.disect_url
    ..decorators
    logging

Contains:
    _filter
    find_cameras
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def _filter(device):
    """
    Determines whether device is a yatwin camera

    Checks:
        '/onvif/device_service' in device['Address']
        (AND) device['Type'] == 'n:NetworkVideoTransmitter'
    """

    # device['DeviceCategory'] usually in ('WCF Services', 'Devices')
    # device['SsdpIp'] == '239.255.255.250'

    check_address_onvif = '/onvif/device_service' in device['Address']
    check_type_network = device['Type'] == 'n:NetworkVideoTransmitter'

    if not check_address_onvif:
        logger.debug \
        (
            'Determined device not camera because: '
            'Address did not contain "/onvif/device_service"'
        )

    if not check_address_onvif:
        logger.debug \
        (
            'Determined device not camera because: '
            'Type != "n:NetworkVideoTransmitter"'
        )

    return check_address_onvif and check_type_network

@decorators.debug()
def find_cameras(attempts=10, max_interest=1, filter=_filter):
    """
    Attempts to find 'max_interest' cameras in at
    ... most 'attempts' attempts
    A device is counted as a camera if _filter(device) == True
    """

    camera_devices = []

    for _ in range(attempts):
        devices = find_devices()

        for device in devices:
            url = device['Address']

            logger.debug \
            (
                'Checking to see if device is a camera: '
                f'{url}'
            )

            url_disected = disect_url(url)

            host = url_disected['IP']
            port = int(url_disected['Port'])
            endpoint = url_disected['Endpoint']

            exists = any(camera_device['Host'] == host for camera_device in camera_devices)

            if exists:
                continue

            if not _filter(device):
                logger.debug("Device was not a camera, skipping")

                continue

            data = \
            {
                'Host': host,
                'Port': port,
                'Endpoint': endpoint,
            }

            logger.debug('Device was a camera')

            camera_devices.append(data)

        if len(camera_devices) >= max_interest:
            logger.debug('Max interest reached, stopping search')
            break

    return camera_devices
