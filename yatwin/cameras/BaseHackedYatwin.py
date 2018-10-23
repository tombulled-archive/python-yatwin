from .. import scripts
from .BaseCamera import BaseCamera
from ..interfaces import onvif

"""
Imports:
    ..scripts
    .BaseCamera.BaseCamera

Contains:
    <BaseHackedYatwin>
"""

class BaseHackedYatwin(BaseCamera):
    """
    The most base yatwin camera, which condones hacking
    """

    def __init__ \
            (
                self,
                host,
                onvif_port = onvif.constants.DEFAULT_PORT
            ):
        """
        Initialises self

        Default onvif_port: onvif.constants.DEFAULT_PORT
        """

        self._init_attrs()

        super().__init__(host)

        self.onvif_port = onvif_port

        self._build_interfaces()

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form:
            <class_name
            (
                interface_name: interface
                ...
            )>
        """

        interfaces_data = []

        for interface_name, interface in self._interfaces.items():
            interfaces_data.append(f'{(interface_name + ":").ljust(10)} {repr(interface)}')

        str_interfaces = '\n\t'.join(interfaces_data)

        str_data = f'<{self.__class__.__name__}\n(\n\t{str_interfaces}\n)>'

        return str_data

    def _build_interfaces(self):
        """
        Builds interfaces, setting them as class attributes
        
        E.g:
            interface_name: 'Http'
            interface: <Http(admin:888888@192.168.1.1:81)>

            self.http = interface
            self._interfaces['http'] = interface
        """

        interfaces = scripts.hack_interfaces(self.host, self.onvif_port)

        for interface_name, interface in interfaces.items():
            attr_name = interface_name.lower()

            setattr(self, attr_name, interface)

            self._interfaces[attr_name] = interface

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        super()._init_attrs()

        self.ftp = None
        self.http = None
        self.icmp = None
        self.imap = None
        self.multicast = None
        self.onvif = None
        self.rtsp = None
        self.telnet = None

        self.onvif_port = None

        self._interfaces = {}
