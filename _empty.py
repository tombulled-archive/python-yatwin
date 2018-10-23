"""
from yatwin.cameras import BaseHackedYatwin

HOST = '192.168.1.227'
ONVIF_PORT = 10080

cam = BaseHackedYatwin(HOST, onvif_port=ONVIF_PORT)

print(cam.telnet.execute('echo "Telnet was auto-hacked"'))
"""

from yatwin.interfaces import Telnet

t = Telnet('192.168.1.227')

print(t.execute('echo "Telnet was auto-hackedsssssssssssssssssssssssssssssssssssssssssssssssssssss"'))
