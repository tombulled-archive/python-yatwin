# python-yatwin: /yatwin/onekeywifi/network/netsh/cmdsoup/

## Contents:
* [CmdSoup.CmdSoup](#example-cmdsoupcmdsoup)

### Example: CmdSoup.CmdSoup
```python
>>> from yatwin.onekeywifi.network.netsh.cmdsoup import CmdSoup
>>> from yatwin.onekeywifi.network.netsh import utils
>>> from pprint import pprint
>>> 
>>> # Execute a netsh command
>>> stdout = utils.cmd_exec_subprocess('netsh wlan show networks mode=bssid')
>>> stdout = '\n'.join(stdout.splitlines()[3:]).strip()
>>>
>>> # See the commands stdout
>>> print(stdout)
SSID 1 : SomeSSID
    Network type            : Infrastructure
    Authentication          : WPA2-Personal
    Encryption              : CCMP 
    BSSID 1                 : 96:df:e9:fc:dc:7b
         Signal             : 88%  
         Radio type         : 802.11n
         Channel            : 4
         Basic rates (Mbps) : 1 2 5.5 11
         Other rates (Mbps) : 6 9 12 18 24 36 48 54
>>> 
>>> # Create a CmdSoup instance
>>> cmd_soup = CmdSoup(stdout)
>>> networks_dict = cmd_soup.as_dict()
>>> 
>>> # View the parsed dictionary
>>> pprint(networks_dict)
{'SSID 1': {'Authentication': 'WPA2-Personal',
            'BSSID 1': {'BSSID 1': '96:df:e9:fc:dc:7b',
                        'Basic rates (Mbps)': '1 2 5.5 11',
                        'Channel': '4',
                        'Other rates (Mbps)': '6 9 12 18 24 36 48 54',
                        'Radio type': '802.11n',
                        'Signal': '88%'},
            'Encryption': 'CCMP',
            'Network type': 'Infrastructure',
            'SSID 1': 'SomeSSID'}}
>>> 
```
