from . import utils
from .cmdsoup.CmdSoup import CmdSoup

"""
Contains:
    <Netsh>

Imports:
    .utils
    .cmdsoup.CmdSoup.CmdSoup
"""

class Netsh(object):
    """
    Class to interface with the cmd command 'netsh'
    Very limited support
    """

    @staticmethod
    def get_networks(interface='wlan', mode='bssid'):
        """
        Returns a dictionay of data extacted from
        ... the command 'netsh {interface} show networks mode={mode}'
        Tailored for when 'mode' == 'bssid'
        """

        kwargs = {'mode': mode}
        command = 'netsh {interface} show networks {kwargs}'.format \
        (
            interface = interface,
            kwargs = ' '.join \
            (
                ['{key}={val}'.format(key=key, val=val) for key, val in kwargs.items()]
            )
        )
        cmd_resp = utils.cmd_exec_subprocess(command)
        cmd_resp = '\n'.join(cmd_resp.splitlines()[3:]).strip()

        soup = CmdSoup(cmd_resp)

        networks_dict = soup.as_dict()

        ret_data = []

        for ssid_key, ssid_val in networks_dict.items():
            bssids = []

            for nested_key, nested_val in ssid_val.items():
                if nested_key.startswith('BSSID'):
                    bssid_data = \
                    {
                        'BSSID': nested_val.get(nested_key, None),
                        'BasicRates': nested_val.get('Basic rates (Mbps)', None),
                        'OtherRates': nested_val.get('Other rates (Mbps)', None),
                        'Channel': nested_val.get('Channel', None),
                        'RadioType': nested_val.get('Radio type', None),
                        'Signal': nested_val.get('Signal', None),
                    }

                    bssids.append(bssid_data)

            network_data = \
            {
                'SSID': ssid_val.get(ssid_key, None),
                'Authentication': ssid_val.get('Authentication', None),
                'Encryption': ssid_val.get('Encryption', None),
                'NetworkType': ssid_val.get('Network type', None),
                'BSSIDs': bssids,
            }

            ret_data.append(network_data)

        return ret_data

    @staticmethod
    def get_interfaces(interface='wlan'):
        """
        Returns a dictionay of data extacted from
        ... the command 'netsh {interface} show networks mode={mode}'
        Tailored for when 'mode' == 'bssid'
        """

        command = f'netsh {interface} show interfaces'

        cmd_resp = utils.cmd_exec_subprocess(command)
        cmd_resp = '\n'.join(cmd_resp.splitlines()[3:]).strip()

        soup = CmdSoup(cmd_resp)

        interfaces_dict = soup.as_dict()

        ret_data = (list(interfaces_dict.values())[0],) # Only returns the first interface

        return ret_data
