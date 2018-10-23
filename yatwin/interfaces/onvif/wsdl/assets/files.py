import os
import os.path

#PATH = os.getcwd() + '\\'
PATH = os.path.dirname(__file__) + '\\'

WSDL_ANALYTICS = PATH + 'analytics.wsdl'
WSDL_ANALYTICS_DEVICE = PATH + 'analyticsdevice.wsdl'
WSDL_DEVICE_IO = PATH + 'deviceio.wsdl'
WSDL_DEVICE_MGMT = PATH + 'devicemgmt.wsdl'
WSDL_DISPLAY = PATH + 'display.wsdl'
WSDL_EVENT = PATH + 'event.wsdl'
WSDL_IMAGING = PATH + 'imaging.wsdl'
WSDL_MEDIA = PATH + 'media.wsdl'
WSDL_PTZ = PATH + 'ptz.wsdl'
WSDL_REMOTE_DISCOVERY = PATH + 'remotediscovery.wsdl'
WSDL_RECORDING = PATH + 'recording.wsdl'
WSDL_SEARCH = PATH + 'search.wsdl'
WSDL_REPLAY = PATH + 'replay.wsdl'
WSDL_RECEIVER = PATH + 'receiver.wsdl'
WSDL_EVENTS = PATH + 'events.wsdl'

XSD_ONVIF = PATH + 'onvif.xsd'
XSD_COMMON = PATH + 'common.xsd'

WSDLS = \
(
    WSDL_ANALYTICS,
    WSDL_ANALYTICS_DEVICE,
    WSDL_DEVICE_IO,
    WSDL_DEVICE_MGMT,
    WSDL_DISPLAY,
    WSDL_EVENT,
    WSDL_IMAGING,
    WSDL_MEDIA,
    WSDL_PTZ,
    WSDL_REMOTE_DISCOVERY,
    WSDL_RECORDING,
    WSDL_SEARCH,
    WSDL_REPLAY,
    WSDL_RECEIVER,
    WSDL_EVENTS,
)

XSDS = \
(
    XSD_ONVIF,
    XSD_COMMON,
)
