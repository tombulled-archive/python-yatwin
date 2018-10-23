import subprocess
import re

"""
Imports:
    subprocess
    re

Contains:
    ping
    _parse_ping

Constants defined here:
    CREATE_NO_WINDOW
    CRLF
"""

CREATE_NO_WINDOW = 0x08000000
CRLF = '\r\n'

def ping(dst, raw=False):
    """
    Executes the system ping command
    ... using subprocess.Popen
    Hides the shell using creationflags
    Pings dst *once*
    If raw == True, returns the raw stdout
    ... else, returns a parsed dictionary
    """

    process = subprocess.Popen \
    (
        ['ping', '-n', '1', dst],
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        creationflags = CREATE_NO_WINDOW
    )

    stdout = process.communicate()[0].decode()

    if raw:
        return stdout

    parsed = _parse_ping(stdout)

    return parsed

def _parse_ping(resp):
    """
    Parses the stdout of a system ping command ('resp')
    ... into a dictionary
    """

    resp = resp.strip()

    if 'Destination host unreachable.' in resp:
        return None

    if 'Request timed out.' in resp:
        return None

    (
        line_pinging,
        line_reply,
        _,
        line_statistics,
        line_packets,
        line_approximate,
        line_times,
    ) = resp.split(CRLF)

    search_pinging = re.search \
    (
        r'Pinging (?P<ip>.*?) with (?P<bytes>.*?) bytes of data:',
        line_pinging
    )

    pinging_ip = search_pinging.group('ip')
    pinging_bytes = search_pinging.group('bytes')

    search_reply = re.search \
    (
        r'Reply from (?P<ip>.*?): bytes=(?P<bytes>.*?) time=(?P<time>.*?)ms TTL=(?P<ttl>.*)',
        line_reply
    )

    reply_ip = search_reply.group('ip')
    reply_bytes = search_reply.group('bytes')
    reply_time = search_reply.group('time')
    reply_ttl = search_reply.group('ttl')

    search_packets = re.search \
    (
        r'    Packets: Sent = (?P<sent>.*?), Received = (?P<received>.*?), Lost = (?P<lost>.*?) \((?P<loss>.*?)\% loss\),',
        line_packets
    )

    packets_sent = search_packets.group('sent')
    packets_received = search_packets.group('received')
    packets_lost = search_packets.group('lost')
    packets_loss = search_packets.group('loss')

    search_times = re.search \
    (
        r'    Minimum = (?P<minimum>.*?)ms, Maximum = (?P<maximum>.*?)ms, Average = (?P<average>.*?)ms',
        line_times
    )

    times_minimum = search_times.group('minimum')
    times_maximum = search_times.group('maximum')
    times_average = search_times.group('average')

    data = \
    {
        'Pinging': \
        {
            'IP': pinging_ip,
            'Bytes': pinging_bytes,
        },
        'Replies': \
        [
            {
                'From': reply_ip,
                'Bytes': reply_bytes,
                'Time': reply_time, #Ms
                'TTL': reply_ttl,
            },
        ],
        'Statistics': \
        {
            'Packets': \
            {
                'Sent': packets_sent,
                'Received': packets_received,
                'Lost': packets_lost,
                'Loss': packets_loss,
            },
        },
        'Times': \
        {
            'Minimum': times_minimum,
            'Maximum': times_maximum,
            'Average': times_average,
        },
        'Raw': resp,
    }

    return data
