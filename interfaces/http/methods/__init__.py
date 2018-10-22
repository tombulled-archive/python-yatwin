"""
Provides fast access to all methods

Imports:
	.{method_name}.{method_name}

	E.g:
		.get_status.get_status

Therefore, can do (e.g.):
	from methods import get_status

Also defined here:
	METHODS - a dictionary of:
		'{method_name}': method,

Methods not-implemented:
	auto_download_file | Crashes camera, left un-implemented
	check_user | Crashes camera, left un-implemented
	trans_cmd_string | Just returns: var cmd={whatever cmd you gave it};
"""

from .audiostream import audiostream
from .camera_control import camera_control
from .decoder_control import decoder_control
from .del_file import del_file
from .ftptest import ftptest
from .get_aging import get_aging
from .get_alarmlog import get_alarmlog
from .get_apwifi import get_apwifi
from .get_camera_params import get_camera_params
from .get_factory_extra import get_factory_extra
from .get_factory_param import get_factory_param
from .get_log import get_log
from .get_misc import get_misc
from .get_onvif import get_onvif
from .get_params import get_params
from .get_pnp_server import get_pnp_server
from .get_record import get_record
from .get_record_file import get_record_file
from .get_rtsp import get_rtsp
from .get_status import get_status
from .get_wifi_scan_result import get_wifi_scan_result
from .livestream import livestream
from .login import login
from .mailtest import mailtest
from .reboot import reboot
from .restore_factory import restore_factory
from .set_aging import set_aging
from .set_alarm import set_alarm
from .set_alarmlogclr import set_alarmlogclr
from .set_alias import set_alias
from .set_apwifi import set_apwifi
from .set_bootday import set_bootday
from .set_datetime import set_datetime
from .set_ddns import set_ddns
from .set_default import set_default
from .set_devices import set_devices
from .set_extra import set_extra
from .set_factory_extra import set_factory_extra
from .set_factory_param import set_factory_param
from .set_formatsd import set_formatsd
from .set_ftp import set_ftp
from .set_ir_gpio import set_ir_gpio
from .set_mail import set_mail
from .set_media import set_media
from .set_misc import set_misc
from .set_moto_run import set_moto_run
from .set_network import set_network
from .set_onvif import set_onvif
from .set_pnp_server import set_pnp_server
from .set_pppoe import set_pppoe
from .set_recordsch import set_recordsch
from .set_rtsp import set_rtsp
from .set_update_push_user import set_update_push_user
from .set_upnp import set_upnp
from .set_users import set_users
from .set_wifi import set_wifi
from .snapshot import snapshot
from .test_ftp import test_ftp
from .test_mail import test_mail
from .upgrade_firmware import upgrade_firmware
from .upgrade_htmls import upgrade_htmls
from .videostream import videostream
from .wifi_scan import wifi_scan

METHODS = \
{
    'audiostream': audiostream,
	'camera_control': camera_control,
	'decoder_control': decoder_control,
	'del_file': del_file,
	'ftptest': ftptest,
	'get_aging': get_aging,
	'get_alarmlog': get_alarmlog,
	'get_apwifi': get_apwifi,
	'get_camera_params': get_camera_params,
	'get_factory_extra': get_factory_extra,
	'get_factory_param': get_factory_param,
	'get_log': get_log,
	'get_misc': get_misc,
	'get_onvif': get_onvif,
	'get_params': get_params,
	'get_pnp_server': get_pnp_server,
	'get_record': get_record,
	'get_record_file': get_record_file,
	'get_rtsp': get_rtsp,
	'get_status': get_status,
	'get_wifi_scan_result': get_wifi_scan_result,
	'livestream': livestream,
	'login': login,
	'mailtest': mailtest,
	'reboot': reboot,
	'restore_factory': restore_factory,
	'set_aging': set_aging,
	'set_alarm': set_alarm,
	'set_alarmlogclr': set_alarmlogclr,
	'set_alias': set_alias,
	'set_apwifi': set_apwifi,
	'set_bootday': set_bootday,
	'set_datetime': set_datetime,
	'set_ddns': set_ddns,
	'set_default': set_default,
	'set_devices': set_devices,
	'set_extra': set_extra,
	'set_factory_extra': set_factory_extra,
	'set_factory_param': set_factory_param,
	'set_formatsd': set_formatsd,
	'set_ftp': set_ftp,
	'set_ir_gpio': set_ir_gpio,
	'set_mail': set_mail,
	'set_media': set_media,
	'set_misc': set_misc,
	'set_moto_run': set_moto_run,
	'set_network': set_network,
	'set_onvif': set_onvif,
	'set_pnp_server': set_pnp_server,
	'set_pppoe': set_pppoe,
	'set_recordsch': set_recordsch,
	'set_rtsp': set_rtsp,
	'set_update_push_user': set_update_push_user,
	'set_upnp': set_upnp,
	'set_users': set_users,
	'set_wifi': set_wifi,
	'snapshot': snapshot,
	'test_ftp': test_ftp,
	'test_mail': test_mail,
	'upgrade_firmware': upgrade_firmware,
	'upgrade_htmls': upgrade_htmls,
	'videostream': videostream,
	'wifi_scan': wifi_scan,
}
