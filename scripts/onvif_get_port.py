from ..interfaces import Onvif
from .. import decorators
import logging

"""
Imports:
    ..interfaces.Onvif
    ..decorators
    logging

Contains:
    get_http_port
    get_rtsp_port
    _get_port
"""

logger = logging.getLogger(__name__)
logger.info(f'Library imported: {__name__}')

@decorators.debug()
def get_http_port(onvif):
    """
    Gets the cameras HTTP port using onvif

    The onvif instance should have been built

    Returns: The HTTP port
    """

    return _get_port(onvif, 'HTTP')

@decorators.debug()
def get_rtsp_port(onvif):
    """
    Gets the cameras RTSP port using onvif

    The onvif instance should have been built

    Returns: The RTSP port
    """

    return _get_port(onvif, 'RTSP')

@decorators.debug()
def _get_port(onvif, protocol_name):
    """
    Gets the cameras {protocol_name} port using onvif

    The onvif instance should have been built

    Returns: The {protocol_name} port

    Example protocols:
        HTTP
        RTSP
    """

    protocols = onvif.DeviceMgmt.GetNetworkProtocols()

    for protocol in protocols:
        if protocol.Name != protocol_name:
            continue

        ports = protocol.Port

        if not ports:
            logger.debug(f'{protocol_name} protocol had no ports')

            return

        port = ports[0]

        logger.debug(f'Found {protocol_name} protocol port: {port}')

        return port
