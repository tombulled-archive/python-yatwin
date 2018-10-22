from .netsh.Netsh import Netsh
from .PyWiWi import WindowsWifi

"""
Library containing:
    <NetworkScanner>

Imports:
    .netsh.Netsh.Netsh
    .PyWiWi.WindowsWifi
"""

class NetworkScanner(object):
    """
    Class to discover Wireless Access Points (WAP's)
    Designed to retrieve their SSID's and respective BSSID's

    It's strongly advised to use .scan_pywiwi

    These methods both seem to suffer from a bug where
    ... networks are not always discovered
    """

    @staticmethod
    def scan():
        return NetworkScanner.scan_pywiwi()

    @staticmethod
    def scan_netsh(interface='wlan'):
        """
        Wrapper for .netsh.Netsh.Netsh.get_networks
        Returns a list of .Network.Network's
        """

        netsh = Netsh()

        networks = netsh.get_networks(interface, mode='bssid')

        safe_networks = []

        for network in networks:
            network_data = {}

            for key, val in network.items():
                safe_key = key.replace('(Mbps)', '')
                safe_key = safe_key.title()
                safe_key = safe_key.replace(' ', '')

                network_data[safe_key] = val

            safe_networks.append(network_data)

        return safe_networks

    @staticmethod
    def scan_pywiwi(interface_index=0):
        """
        Wrapper for:
            .PyWiWi.WindowsWifi.WindowsWifi.getWirelessInterfaces
            .PyWiWi.WindowsWifi.WindowsWifi.getWirelessAvailableNetworkList
            .PyWiWi.WindowsWifi.WindowsWifi.getWirelessNetworkBssList
        'interface' == WindowsWifi.getWirelessInterfaces()[interface_index]
        Returns a dictionary in the form {SSID: BSSIDS}
            Where 'BSSIDS' is a list in the form ['BSSID 1', 'BSSID 2', ...]
        """

        interfaces = WindowsWifi.getWirelessInterfaces()
        interface = interfaces[interface_index]

        networks = WindowsWifi.getWirelessAvailableNetworkList(interface)
        networks_bss = WindowsWifi.getWirelessNetworkBssList(interface)

        ssid_bssids_map = {}

        for network in networks:
            ssid_bssids_map[network.ssid.decode()] = []

        for network_bss in networks_bss:
            if network_bss.ssid.decode() not in ssid_bssids_map:
                ssid_bssids_map[network_bss.ssid.decode()] = []

            ssid_bssids_map[network_bss.ssid.decode()].append(network_bss.bssid)

        return ssid_bssids_map

    @staticmethod
    def get_interfaces():
        return NetworkScanner.get_interfaces_netsh()

    @staticmethod
    def get_interface():
        return NetworkScanner.get_interfaces_netsh()[0]

    @staticmethod
    def get_networks():
        return NetworkScanner.scan_pywiwi()

    @staticmethod
    def get_interfaces_netsh():
        netsh = Netsh()

        interfaces = netsh.get_interfaces()

        safe_interfaces = []

        for interface in interfaces:
            interface_data = {}

            for key, val in interface.items():
                safe_key = key.replace('(Mbps)', '')
                safe_key = safe_key.title()
                safe_key = safe_key.replace(' ', '')

                interface_data[safe_key] = val

            safe_interfaces.append(interface_data)

        return safe_interfaces
