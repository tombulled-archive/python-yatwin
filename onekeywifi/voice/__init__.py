"""
Python implementation of VStarcam's Java OneKeyWifi code

Download page: http://www.vstarcam.com/SDK-Download.html

Download link: http://download.eye4.cn/download/sdk/SDK_TPNP.zip

Java code location: /SDK_TPNP.zip/SDK_TPNP_NDA-20180725/OneKeyWifi.zip/OneKeyWifi/LibVoice/Android 8/voice.jar

.jar extracted with: http://www.javadecompilers.com/

Imports:
    .util.Util
    .Constants
    .CRC.CRC
    .MainActivity.MainActivity
    .encoder.DataEncoder
    .encoder.VoicePlayer
    .decoder.DataDecoder
"""

from .util import Util
from . import Constants
from .CRC import CRC
from .MainActivity import MainActivity
from .encoder import DataEncoder
from .encoder import VoicePlayer
from .decoder import DataDecoder
