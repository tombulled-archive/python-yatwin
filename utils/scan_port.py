import socket

"""
Imports:
    socket

Contains:
    scan_port
"""

def scan_port(host, port):
    """
    Returns, boolean, whether port is open
    """

    Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    return Socket.connect_ex((host, port)) == 0
