from . import wincmdping
from . import decorators

"""
Imports:
    .wincmdping
    .decorators

Contains:
    <Icmp>
"""

class Icmp(object):
    """
    Class for pinging ip addresses
    """

    def __init__(self, dst=None):
        """
        Initialises self

        :param dst - destination for all .ping()'s to ping.
            Can be omitted.
        """

        self._init_attrs()

        self.dst = dst

    def __repr__(self):
        """
        Returns a string representation of the object
        ... in the form <class_name(dst)>
        """

        return f'<{self.__class__.__name__}({self.dst})>'

    @decorators.kwarg_or_attr('dst', not_in=(None,))
    def ping(self, dst=None):
        """
        Ping 'dst'

        Decorators:
            @staticmethod

        :param dst - Destination to ping.
            If None, attempts to use self.dst, will raise a <TypeError> if that fails

        Returns 'True' if host is up (>= 50% ping sucess rate)
        Else, returns 'False'
        """

        pinged = wincmdping.ping(dst)

        if pinged is None:
            return False # Raise an error?

        loss = int(pinged['Statistics']['Packets']['Loss'])

        return loss <= 50

    @decorators.kwarg_or_attr('dst', not_in=(None,))
    def ping_raw(self, dst=None):
        """
        Ping 'dst'

        Decorators:
            @staticmethod

        :param dst - Destination to ping.
            If None, attempts to use self.dst, will raise a <TypeError> if that fails

        Returns the raw command-line stdout for the ping
        """

        pinged = wincmdping.ping(dst, raw=True)

        pinged_pretty = pinged.replace('\r', '').strip()

        return pinged_pretty

    def _init_attrs(self):
        """
        Initialises the class attributes
        It creates them, then fills them with a default/null value (usualy None)
        """

        self.dst = None
