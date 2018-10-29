from ..interfaces import INTERFACES
from .. import onekeywifi
from . import decorators
from . import utils

"""
Imports:
    ..interfaces.INTERFACES
    ..onekeywifi
    .decorators
    .utils

Contains:
    <BaseCamera>
"""

class BaseCamera(object):
    """
    The most base camera
    """

    def __init__(self, host):
        """
        Initialises self
        """

        self._init_attrs()

        self.host = host

        self._build_service_creators()

        self.multicast = self.create_service('multicast')
        self.icmp = self.create_service('icmp', self.host)
        self.onekeywifi = self.create_service('onekeywifi')

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form: <class_name(host)>
        """

        return f'<{self.__class__.__name__}({self.host})>'

    def create_service(self, service_name, *args, **kwargs):
        """
        Attempts to create the service assosciated with
        ... service_name. Found in self._service_creators
        If the service does not exist, or it fails, it
        ... returns None
        """

        creator = self._service_creators.get(service_name, None)

        if creator is None:
            return None

        return creator(*args, **kwargs)

    def _build_service_creators(self):
        """
        Builds service creators

        E.g:
            service: onekeywifi.OneKeyWifi
            service_name: 'onekeywifi'
            service_creator: self.create_onekeywifi_service

            self._service_creators[service_name] = service
        """

        INTERFACES.update({'onekeywifi': onekeywifi.OneKeyWifi})

        for name, interface in INTERFACES.items():
            method_name = f'create_{name}_service'
            method_doc = \
            (
                f'Create a new {name} service\n'
                f'Returns service(*args, **kwargs)\n'
                'If service creation fails, returns None'
            )

            method = utils.create_service(interface)
            method.__name__ = method_name
            method.__doc__ = method_doc

            setattr(self, method_name, method)

            self._service_creators[name] = method

    def _init_attrs(self):
        """
        Initialises class attributes
        """

        self.host = None

        self._service_creators = {}
