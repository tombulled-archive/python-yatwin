"""
Imports:
    .ftp.ftp.Ftp
    .rtsp.rtsp.Rtsp
    .telnet.telnet.Telnet
    .http.http.Http
    .onvif.onvif.Onvif
    .icmp.icmp.Icmp
    .imap.imap.Imap
    .multicast.multicast.Multicast
"""

from .ftp.ftp import Ftp # Negligible time cost
from .rtsp.rtsp import Rtsp # Negligible time cost
from .telnet.telnet import Telnet # Negligible time cost
from .http.http import Http # Time cost (caused by Auto-Build): ~0.5s
from .onvif.onvif import Onvif # Time cost (caused by Auto-Build): ~0.5s
from .icmp.icmp import Icmp # Time cost: ~0.5s
from .imap.imap import Imap # Negligible time cost
from .multicast.multicast import Multicast # Negligible time cost

INTERFACES = \
{
    'ftp': Ftp,
    'rtsp': Rtsp,
    'telnet': Telnet,
    'http': Http,
    'onvif': Onvif,
    'icmp': Icmp,
    'imap': Imap,
    'multicast': Multicast,
}
