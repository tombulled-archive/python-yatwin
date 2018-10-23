from ..interfaces import Multicast
from .. import decorators
import logging

"""
Imports:
    ..interfaces.Multicast
    ..decorators
    logging

Contains:
    find_devices
    find_devices_nmap

Variables defined here:
    multicast
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

multicast = Multicast()

@decorators.debug()
def find_devices():
    """
    Broadcasts *wsdd discover* packets
    ... using ..interfaces.Multicast.ws_discover
    Returns a list of:
        {
            'DeviceCategory': 'Devices',
            'SsdpIp': '239.255.255.250',
            'Address': The device URL,
            'Type': The device type,
        }
    """

    raw_devices = multicast.ws_discover()

    devices = []

    for raw_device in raw_devices:
        device = \
        {
            'DeviceCategory': 'Devices',
            'SsdpIp': '239.255.255.250',
            'Address': raw_device['XAddrs'][0],
            'Type': 'n:' + raw_device['Types'][0].getLocalname(),
        }

        logger.debug(f'Found device: {device["Address"]}')

        devices.append(device)

    return devices

@decorators.debug()
def find_devices_nmap(device_type='n:NetworkVideoTransmitter'):
    """
    Broadcasts *wsdd discover* packets using
    ... ..interfaces.Multicast.broadcast_wsdd_discover_nmap
    Returns a list of:
        {
            'DeviceCategory': The device category,
            'SsdpIp': The SSDP IP,
            'Address': The device URL,
            'Type': The device type,
        }
    """

    devices = multicast.broadcast_wsdd_discover_nmap()

    if devices is None:
        logger.debug('Nmap found no devices')

        return []

    data = []

    for device_category, device_category_contents in devices.items():
            for ip_index, ip_item in enumerate(device_category_contents):
                for ip, ip_contents in ip_item.items():
                    if ip_contents.get('Type', None) != device_type:
                        continue

                    sub_data = \
                    {
                        'DeviceCategory': device_category,
                        'SsdpIp': ip,
                        'Address': ip_contents.get('Address', None),
                        #'Message ID': ip_contents.get('Message id', None),
                        'Type': ip_contents.get('Type', None),
                    }

                    logger.debug(f'Found device: {sub_data["Address"]}')

                    data.append(sub_data)

    return data
