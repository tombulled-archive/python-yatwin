# python-yatwin: /yatwin/interfaces/onvif/

## Contents:
* [constants](#example-constants)
* [onvif.Onvif](#example-onvifonvif)

### Example: constants
```python
>>> from yatwin.interfaces.onvif import constants
>>> from pprint import pprint
>>> 
>>> # See what constants are available
>>> pprint([attr for attr in dir(constants) if not attr.startswith('_')])
['AUTO_BUILD', 'DEFAULT_PASSWORD', 'DEFAULT_PORT', 'DEFAULT_USERNAME']
>>> 
>>> # Pick a constant
>>> DEFAULT_PASSWORD = constants.DEFAULT_PASSWORD
>>> DEFAULT_PASSWORD
'888888'
>>> 
>>> # Import a constant
>>> from yatwin.interfaces.onvif.constants import DEFAULT_USERNAME
>>> DEFAULT_USERNAME
'admin'
>>> 
>>> # Change a constants value
>>> DEAULT_USERNAME = 'john'
>>> DEAULT_USERNAME
'john'
>>> 
>>> # Create a new constant
>>> constants.FOO_BAR = 'Value'
>>> constants.FOO_BAR
'Value'
>>> 
```

### Example: onvif.Onvif
```python
>>> from yatwin.interfaces import Onvif
>>> from pprint import pprint
>>> 
>>> # Camera (Onvif) information
>>> HOST = '192.168.1.227'
>>> PORT = 10080
>>> USERNAME = 'admin'
>>> PASSWORD = '888888'
>>> 
>>> # Create an Onvif instance
>>> onvif = Onvif \
(
	HOST,
	port = PORT,
	username = USERNAME,
	password = PASSWORD,
)
>>> onvif
<Onvif(admin:888888@192.168.1.227:10080)>
>>> 
>>> # See which services are available
>>> pprint(onvif.services)
{'DeviceMgmt': <onvif.client.ONVIFService object at 0x000001BF607AF0F0>,
 'Events': <onvif.client.ONVIFService object at 0x000001BF60B894E0>,
 'Imaging': <onvif.client.ONVIFService object at 0x000001BF60BDD6D8>,
 'Media': <onvif.client.ONVIFService object at 0x000001BF60E17470>,
 'PTZ': <onvif.client.ONVIFService object at 0x000001BF61168B00>}
>>> 
>>> # See which operations a service has
>>> pprint(onvif.DeviceMgmt.operations)
{'AddIPAddressFilter': <function safe_func.<locals>.wrapped at 0x000001BF613D97B8>,
 'AddScopes': <function safe_func.<locals>.wrapped at 0x000001BF613D98C8>,
 'CreateCertificate': <function safe_func.<locals>.wrapped at 0x000001BF613D99D8>,
 'CreateDot1XConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF613D9AE8>,
 'CreateUsers': <function safe_func.<locals>.wrapped at 0x000001BF613D9BF8>,
 'DeleteCertificates': <function safe_func.<locals>.wrapped at 0x000001BF613D9D08>,
 'DeleteDot1XConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF613D9E18>,
 'DeleteUsers': <function safe_func.<locals>.wrapped at 0x000001BF613D9F28>,
 'GetAccessPolicy': <function safe_func.<locals>.wrapped at 0x000001BF613ED0D0>,
 'GetCACertificates': <function safe_func.<locals>.wrapped at 0x000001BF613ED1E0>,
 'GetCapabilities': <function safe_func.<locals>.wrapped at 0x000001BF613ED2F0>,
 'GetCertificateInformation': <function safe_func.<locals>.wrapped at 0x000001BF613ED488>,
 'GetCertificates': <function safe_func.<locals>.wrapped at 0x000001BF613ED598>,
 'GetCertificatesStatus': <function safe_func.<locals>.wrapped at 0x000001BF613ED6A8>,
 'GetClientCertificateMode': <function safe_func.<locals>.wrapped at 0x000001BF613ED7B8>,
 'GetDNS': <function safe_func.<locals>.wrapped at 0x000001BF613ED8C8>,
 'GetDPAddresses': <function safe_func.<locals>.wrapped at 0x000001BF613ED9D8>,
 'GetDeviceInformation': <function safe_func.<locals>.wrapped at 0x000001BF613EDAE8>,
 'GetDiscoveryMode': <function safe_func.<locals>.wrapped at 0x000001BF613EDBF8>,
 'GetDot11Capabilities': <function safe_func.<locals>.wrapped at 0x000001BF613EDD08>,
 'GetDot11Status': <function safe_func.<locals>.wrapped at 0x000001BF613EDE18>,
 'GetDot1XConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF613EDF28>,
 'GetDot1XConfigurations': <function safe_func.<locals>.wrapped at 0x000001BF613F20D0>,
 'GetDynamicDNS': <function safe_func.<locals>.wrapped at 0x000001BF613F21E0>,
 'GetEndpointReference': <function safe_func.<locals>.wrapped at 0x000001BF613F22F0>,
 'GetHostname': <function safe_func.<locals>.wrapped at 0x000001BF613F2400>,
 'GetIPAddressFilter': <function safe_func.<locals>.wrapped at 0x000001BF613F2510>,
 'GetNTP': <function safe_func.<locals>.wrapped at 0x000001BF613F2620>,
 'GetNetworkDefaultGateway': <function safe_func.<locals>.wrapped at 0x000001BF613F2730>,
 'GetNetworkInterfaces': <function safe_func.<locals>.wrapped at 0x000001BF613F2840>,
 'GetNetworkProtocols': <function safe_func.<locals>.wrapped at 0x000001BF613F2950>,
 'GetPkcs10Request': <function safe_func.<locals>.wrapped at 0x000001BF613F2A60>,
 'GetRelayOutputs': <function safe_func.<locals>.wrapped at 0x000001BF613F2B70>,
 'GetRemoteDiscoveryMode': <function safe_func.<locals>.wrapped at 0x000001BF613F2C80>,
 'GetRemoteUser': <function safe_func.<locals>.wrapped at 0x000001BF613F2D90>,
 'GetScopes': <function safe_func.<locals>.wrapped at 0x000001BF613F2EA0>,
 'GetServiceCapabilities': <function safe_func.<locals>.wrapped at 0x000001BF613FB048>,
 'GetServices': <function safe_func.<locals>.wrapped at 0x000001BF613FB158>,
 'GetSystemBackup': <function safe_func.<locals>.wrapped at 0x000001BF613FB268>,
 'GetSystemDateAndTime': <function safe_func.<locals>.wrapped at 0x000001BF613FB378>,
 'GetSystemLog': <function safe_func.<locals>.wrapped at 0x000001BF613FB488>,
 'GetSystemSupportInformation': <function safe_func.<locals>.wrapped at 0x000001BF613FB598>,
 'GetSystemUris': <function safe_func.<locals>.wrapped at 0x000001BF613FB6A8>,
 'GetUsers': <function safe_func.<locals>.wrapped at 0x000001BF613FB7B8>,
 'GetWsdlUrl': <function safe_func.<locals>.wrapped at 0x000001BF613FB8C8>,
 'GetZeroConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF613FB9D8>,
 'LoadCACertificates': <function safe_func.<locals>.wrapped at 0x000001BF613FBAE8>,
 'LoadCertificateWithPrivateKey': <function safe_func.<locals>.wrapped at 0x000001BF613FBBF8>,
 'LoadCertificates': <function safe_func.<locals>.wrapped at 0x000001BF613FBD08>,
 'RemoveIPAddressFilter': <function safe_func.<locals>.wrapped at 0x000001BF613FBE18>,
 'RemoveScopes': <function safe_func.<locals>.wrapped at 0x000001BF613FBF28>,
 'RestoreSystem': <function safe_func.<locals>.wrapped at 0x000001BF614030D0>,
 'ScanAvailableDot11Networks': <function safe_func.<locals>.wrapped at 0x000001BF614031E0>,
 'SendAuxiliaryCommand': <function safe_func.<locals>.wrapped at 0x000001BF614032F0>,
 'SetAccessPolicy': <function safe_func.<locals>.wrapped at 0x000001BF61403400>,
 'SetCertificatesStatus': <function safe_func.<locals>.wrapped at 0x000001BF61403510>,
 'SetClientCertificateMode': <function safe_func.<locals>.wrapped at 0x000001BF61403620>,
 'SetDNS': <function safe_func.<locals>.wrapped at 0x000001BF61403730>,
 'SetDPAddresses': <function safe_func.<locals>.wrapped at 0x000001BF61403840>,
 'SetDiscoveryMode': <function safe_func.<locals>.wrapped at 0x000001BF61403950>,
 'SetDot1XConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF61403A60>,
 'SetDynamicDNS': <function safe_func.<locals>.wrapped at 0x000001BF61403B70>,
 'SetHostname': <function safe_func.<locals>.wrapped at 0x000001BF61403C80>,
 'SetHostnameFromDHCP': <function safe_func.<locals>.wrapped at 0x000001BF61403D90>,
 'SetIPAddressFilter': <function safe_func.<locals>.wrapped at 0x000001BF61403EA0>,
 'SetNTP': <function safe_func.<locals>.wrapped at 0x000001BF6140C048>,
 'SetNetworkDefaultGateway': <function safe_func.<locals>.wrapped at 0x000001BF6140C158>,
 'SetNetworkInterfaces': <function safe_func.<locals>.wrapped at 0x000001BF6140C268>,
 'SetNetworkProtocols': <function safe_func.<locals>.wrapped at 0x000001BF6140C378>,
 'SetRelayOutputSettings': <function safe_func.<locals>.wrapped at 0x000001BF6140C488>,
 'SetRelayOutputState': <function safe_func.<locals>.wrapped at 0x000001BF6140C598>,
 'SetRemoteDiscoveryMode': <function safe_func.<locals>.wrapped at 0x000001BF6140C6A8>,
 'SetRemoteUser': <function safe_func.<locals>.wrapped at 0x000001BF6140C7B8>,
 'SetScopes': <function safe_func.<locals>.wrapped at 0x000001BF6140C8C8>,
 'SetSystemDateAndTime': <function safe_func.<locals>.wrapped at 0x000001BF6140C9D8>,
 'SetSystemFactoryDefault': <function safe_func.<locals>.wrapped at 0x000001BF6140CAE8>,
 'SetUser': <function safe_func.<locals>.wrapped at 0x000001BF6140CBF8>,
 'SetZeroConfiguration': <function safe_func.<locals>.wrapped at 0x000001BF6140CD08>,
 'StartFirmwareUpgrade': <function safe_func.<locals>.wrapped at 0x000001BF6140CE18>,
 'StartSystemRestore': <function safe_func.<locals>.wrapped at 0x000001BF6140CF28>,
 'SystemReboot': <function safe_func.<locals>.wrapped at 0x000001BF614140D0>,
 'UpgradeSystemFirmware': <function safe_func.<locals>.wrapped at 0x000001BF614141E0>}
>>> 
>>> # Call a services operation
>>> resp = onvif.DeviceMgmt.GetServiceCapabilities()
>>> resp
{
    'Network': {
        'IPFilter': False,
        'ZeroConfiguration': False,
        'IPVersion6': False,
        'DynDNS': True,
        'Dot11Configuration': False,
        'Dot1XConfigurations': None,
        'HostnameFromDHCP': False,
        'NTP': 1,
        'DHCPv6': None,
        '_attr_1': {
    }
    },
    'Security': {
        'TLS1.0': False,
        'TLS1.1': False,
        'TLS1.2': False,
        'OnboardKeyGeneration': False,
        'AccessPolicyConfig': False,
        'DefaultAccessPolicy': False,
        'Dot1X': False,
        'RemoteUserHandling': False,
        'X.509Token': False,
        'SAMLToken': False,
        'KerberosToken': False,
        'UsernameToken': True,
        'HttpDigest': True,
        'RELToken': False,
        'SupportedEAPMethods': None,
        'MaxUsers': None,
        '_attr_1': {
    }
    },
    'System': {
        'DiscoveryResolve': True,
        'DiscoveryBye': False,
        'RemoteDiscovery': False,
        'SystemBackup': True,
        'SystemLogging': True,
        'FirmwareUpgrade': True,
        'HttpFirmwareUpgrade': True,
        'HttpSystemBackup': True,
        'HttpSystemLogging': True,
        'HttpSupportInformation': True,
        '_attr_1': {
    }
    },
    'Misc': None
}
>>> 
>>> # Access some data from the response
>>> resp.Security['HttpDigest']
True
>>> 
```
