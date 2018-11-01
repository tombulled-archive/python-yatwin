from . import constants
from .wsdl.wsdl import methods as wsdl_methods
from . import wsdl
from .wsdl import xsd
import onvif
import onvif.exceptions
import operator

"""
Imports:
    .constants
    .wsdl.wsdl.methods as wsdl_methods
    .wsdl
    .wsdl.xsd
    onvif
    onvif.exceptions
    operator
"""

class Onvif(object):
    """
    Indirect wrapper for onvif.ONVIFCamera (https://github.com/quatanium/python-onvif#initialize-an-onvifcamera-instance)

    Default username: constants.DEFAULT_USERNAME
    Default password: constants.DEFAULT_PASSWORD
    Default port: constants.DEFAULT_PORT
    """

    service_map = \
    {
        'DeviceMgmt': 'create_devicemgmt_service',
        'Analytics': 'create_analytics_service',
        'DeviceIO': 'create_deviceio_service',
        'Events': 'create_events_service',
        'Imaging': 'create_imaging_service',
        'Media': 'create_media_service',
        #'Onvif': 'create_onvif_service',
        'PTZ': 'create_ptz_service',
        #'Pullpoint': 'create_pullpoint_service',
        'Receiver': 'create_receiver_service',
        'Recording': 'create_recording_service',
        'Replay': 'create_replay_service',
        'Search': 'create_search_service',
    }

    wsdl_map = \
    {
        'DeviceMgmt': wsdl.WSDL_DEVICE_MGMT,
        'Analytics': wsdl.WSDL_ANALYTICS,
        'DeviceIO': wsdl.WSDL_DEVICE_IO,
        'Events': wsdl.WSDL_EVENTS,
        'Imaging': wsdl.WSDL_IMAGING,
        'Media': wsdl.WSDL_MEDIA,
        #'Onvif': wsdl.WSDL_ONVIF,
        'PTZ': wsdl.WSDL_PTZ,
        #'Pullpoint': wsdl.WSDL_PULLPOINT,
        'Receiver': wsdl.WSDL_RECEIVER,
        'Recording': wsdl.WSDL_RECORDING,
        'Replay': wsdl.WSDL_REPLAY,
        'Search': wsdl.WSDL_SEARCH,
    }

    def __init__ \
            (
                self,
                host,
                port = constants.DEFAULT_PORT,
                username = constants.DEFAULT_USERNAME,
                password = constants.DEFAULT_PASSWORD,
            ):
        """
        Initialises super
        Initialises class attributes

        Default port: constants.DEFAULT_PORT
        Default username: constants.DEFAULT_USERNAME
        Default password: constants.DEFAULT_PASSWORD
        """

        self._init_attrs()

        self.ONVIFCamera = onvif.ONVIFCamera(host, port, username, password)

        self.username = username
        self.password = password
        self.host = host
        self.port = port

        if constants.AUTO_BUILD:
            self.build() # There will be a time cost

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(username:password@ip:port)>
        """

        return '<{class_name}({username}:{password}@{host}:{port})>'.format \
        (
            class_name = self.__class__.__name__,
            username = self.username,
            password = self.password,
            host = self.host,
            port = self.port,
        )

    def build(self):
        """
        Wrapper for self.build_zeep
        """

        return self.build_zeep()

    def build_wsdl(self):
        """
        Builds services.
        Builds each operation in self.services
        """

        self._build_services()

        for service_name, service in self.services.items():
            self._build_operations(service_name)

    def build_zeep(self):
        """
        Builds services and each of their operations
        ... using self.ONVIFCamera's Zeep Client

        This is recommended over self.build_wsdl
        ... for time efficiency, and accuracy
        """

        for service_name, method in self.service_map.items():
            try:
                setattr(self, service_name, getattr(self.ONVIFCamera, method)())
                self.services[service_name] = getattr(self, service_name)
            except onvif.exceptions.ONVIFError:
                pass

        for service_name, service in self.services.items():
            service = self.services.get(service_name, None)

            if service is None: continue

            zeep_client = service.zeep_client
            wsdl = zeep_client.wsdl

            services = wsdl.services
            service_ = list(services.values())[0]

            ports = service_.ports

            # Some services have two ports (Events does)
            # ... onvif-zeep seems to ignore >1 port
            port = list(ports.values())[0]

            operations = sorted \
            (
                port.binding._operations.values(),
                key = operator.attrgetter('name')
            )

            service.operations = {}

            for operation in operations:
                operation_name = operation.name

                operation_obj = getattr(service, operation_name)

                setattr(service, operation_name, operation_obj)
                func = getattr(service, operation_name)

                func.__name__ = operation_name
                func.__doc__ = str(operation)

                service.operations[operation_name] = operation_obj


    def _build_services(self):
        """
        Attempts to create all available services.
        If a service is successfully created,
        ... it is stored in self.services.
        ... It is also set as a class method of self
        E.g:
            To access the 'DeviceMgmt' service, do either:
                onvif_obj.DeviceMgmt.***() OR
                onvig_onj.services.get('DeviceMgmt').***()
        """

        onvif_xsd = xsd.Xsd(wsdl.XSD_ONVIF)
        common_xsd = xsd.Xsd(wsdl.XSD_COMMON)

        self._xsd_scope = (onvif_xsd, common_xsd,)

        for service_name, method in self.service_map.items():
            try:
                setattr(self, service_name, getattr(self.ONVIFCamera, method)())
                self.services[service_name] = getattr(self, service_name)
            except onvif.exceptions.ONVIFError:
                pass

    def _build_operations(self, service_name):
        """
        Calls wsdl_methods.identify_operations on the service
        For each operation identified it sets it as a
        ... class method of that service
        E.g:
            To access the operation 'GetServiceCapabilities' of 'DeviceMgmt', do:
            onvif_obj.DeviceMgmt.GetServiceCapabilities()

        :param service_name - A key for a service from self.services
        """

        wsdl_path = self.wsdl_map.get(service_name, None)

        if wsdl_path is None: return

        service = self.services.get(service_name, None)

        if service is None: return

        wsdl_obj = wsdl.Wsdl(wsdl_path, xsd_scope=self._xsd_scope)

        self._wsdls[service_name] = wsdl_obj

        operations = wsdl_methods.identify_operations(service, wsdl_obj)

        for operation in operations:
            operation_name = operation['Name']

            setattr(service, operation_name, getattr(service, operation_name))
            func = getattr(service, operation_name)

            func.__name__ = operation_name
            func.__doc__ = wsdl_methods.sprintf_compiled_operation(operation)

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value
        """

        self.username = None
        self.password = None
        self.host = None
        self.port = None

        self.DeviceMgmt = None
        self.Analytics = None
        self.DeviceIO = None
        self.Events = None
        self.Imaging = None
        self.Media = None
        #self.Onvif = None
        self.PTZ = None
        #self.Pullpoint = None
        self.Receiver = None
        self.Recording = None
        self.Replay = None
        self.Search = None

        self.services = {}
        self._wsdls = {}
        self._xsd_scope = ()
