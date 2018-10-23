from .parameter_types.Param import Param

"""
Library containing parameters.

These parameters are either only sent (e.g. url?param=val)
... or only receieved (e.g. status parameters)
... therefore they only need an identifier and a description
... and values.

Imports:
	.parameter_types.Param.Param
"""

SUBMODE = Param \
(
	identifier = 'submode',
	getter_identifier = None,
	setter_identifier = 'submode',
	description = 'submode',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_media.cgi',
	values = \
	{
		0: 'means the attached parameter is useful',
		1: 'means adopt system customize',
		2: 'means adopt system customize',
		3: 'means adopt system customize',
		4: 'means adopt system customize',
		5: 'means adopt system customize',
		6: 'means adopt system customize',
		7: 'means adopt system customize',
		8: 'means adopt system customize',
		9: 'means adopt system customize',
		10: 'means adopt system customize',
	},
	identifiers = \
	{
		'set_media.cgi': 'submode',
	},
)
MAINMODE = Param \
(
	identifier = 'mainmode',
	getter_identifier = None,
	setter_identifier = 'mainmode',
	description = 'Mainmode',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_media.cgi',
	values = \
	{
		0: 'means the attached parameter is useful',
		1: 'means adopt system customize',
		2: 'means adopt system customize',
		3: 'means adopt system customize',
		4: 'means adopt system customize',
		5: 'means adopt system customize',
		6: 'means adopt system customize',
		7: 'means adopt system customize',
		8: 'means adopt system customize',
		9: 'means adopt system customize',
		10: 'means adopt system customize',
	},
	identifiers = \
	{
		'set_media.cgi': 'mainmode',
	},
)
MAINRATE = Param \
(
	identifier = 'mainrate',
	getter_identifier = None,
	setter_identifier = 'mainrate',
	description = 'Stream rate',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_media.cgi',
	values = \
	{
		0: 'main stream rate',
		1: 'second stream rate',
	},
	identifiers = \
	{
		'set_media.cgi': 'mainrate',
	},
)
VAL = Param \
(
	identifier = 'val',
	getter_identifier = None,
	setter_identifier = 'val',
	description = 'Whether to turn off infrared light',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_ir_gpio.cgi',
	values = \
	{
		0: 'turn off infrared light',
		1: 'Auto infrared',
	},
	identifiers = \
	{
		'set_ir_gpio.cgi': 'val',
	},
)
CLOSE_MIC = Param \
(
	identifier = 'close_mic',
	getter_identifier = None,
	setter_identifier = 'close_mic',
	description = 'disable MIC',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_extra.cgi',
	values = {},
	identifiers = \
	{
		'set_extra.cgi': 'close_mic',
	},
)
CLOSE_AP = Param \
(
	identifier = 'close_ap',
	getter_identifier = None,
	setter_identifier = 'close_ap',
	description = 'disable ap function',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_extra.cgi',
	values = {},
	identifiers = \
	{
		'set_extra.cgi': 'close_ap',
	},
)
BOOTDAY = Param \
(
	identifier = 'bootday',
	getter_identifier = None,
	setter_identifier = 'bootday',
	description = 'how many days reboot',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = 'set_bootday.cgi',
	values = {},
	identifiers = \
	{
		'set_bootday.cgi': 'bootday',
	},
)
OFFSET = Param \
(
	identifier = 'offset',
	getter_identifier = None,
	setter_identifier = None,
	description = 'works in playback the requested file location',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = \
	{
		'livestream.cgi': 'offset',
	},
)
FILE_NAME = Param \
(
	identifier = 'file_name',
	getter_identifier = None,
	setter_identifier = None,
	description = 'works in playback. The requested file name.',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = \
	{
		'livestream.cgi': 'filename',
	},
)
SUB_STREAM = Param \
(
	identifier = 'sub_stream',
	getter_identifier = None,
	setter_identifier = None,
	description = \
	(
		'when substream exists will ignore res input, '
		'reconfiguration resolution'
	),
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = \
	{
		0: '1280*720',
		1: '1280*720',
		14: '1280*720',
		15: '1280*720',
		16: '1280*720',
		17: '1280*720',
		18: '1280*720',
		19: '1280*720',
		20: '1280*720',
		21: '1280*720',
		22: '1280*720',
		2: '640*360',
		3: '640*360',
		7: '640*360',
		8: '640*360',
		9: '640*360',
		10: '640*360',
		11: '640*360',
		12: '640*360',
		5: '320*180',
		6: '320*180',
	},
	identifiers = \
	{
		'livestream.cgi': 'substream',
	},
)
RES = Param \
(
	identifier = 'res',
	getter_identifier = None,
	setter_identifier = None,
	description = 'Resolution',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = \
	{
		0: '640*360',
		1: '320*180',
		2: 'Snapshot: 1280*720',
		3: '1280*720',
		4: '1920*1080',
	},
	identifiers = \
	{
		'livestream.cgi': 'res',
		'snapshot.cgi': 'res',
	},
)
AUDIO = Param \
(
	identifier = 'audio',
	getter_identifier = None,
	setter_identifier = None,
	description = 'Whether to enable sound transmission',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = \
	{
		0: 'disable sound transmission',
		1: 'Enable sound transmission',
	},
	identifiers = \
	{
		'livestream.cgi': 'audio',
	},
)
STREAM_ID = Param \
(
	identifier = 'stream_id',
	getter_identifier = None,
	setter_identifier = None,
	description = 'Stream ID',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = \
	{
		0x00: \
		(
			'enable listen, request return of index and reference '
			'are cleared. IE request real-time video playback'
		),
		0x01: \
		(
			'enable listen, request return of index and reference '
			'are cleared.'
		),
		0x02: \
		(
			'enable listen, request return of index and reference '
			'are cleared.'
		),
		0x03: \
		(
			'enable listen, request return of index and reference '
			'are cleared. IE request real-time video playback'
		),
		0x04: \
		(
			'enable listen, request return of index and reference '
			'are not cleared. request video playback'
		),
		0x10: 'disable listen. Stop real-time video playback',
		0x50: 'IE request main stream video playback',
		0x51: 'IE request secondary stream video playback',
		0x52: 'IE request secondary stream video playback',
		0x0A: 'request real-time video playback',
		0x11: 'Stop video playback',
	},
	identifiers = \
	{
		'audiostream.cgi': 'streamid',
		'livestream.cgi': 'streamid',
	},
)
NEXT_URL = Param \
(
	identifier = 'next_url',
	getter_identifier = 'next_url',
	setter_identifier = None,
	description = 'Endpoint to redirect to. E.g. \'index.htm\'',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
ALARM_HTTP_PORT = Param \
(
	identifier = 'alarm_http_port',
	getter_identifier = 'alarm_port',
	setter_identifier = 'alarm_port',
	description = 'http url port when alarm (unused)',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
ALARM_NOTE = Param \
(
	identifier = 'alarm_note',
	getter_identifier = 'alarm_note',
	setter_identifier = 'alarm_note',
	description = 'support alarm notification',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {1: 'support alarm notification'},
	identifiers = {},
)
ALARM_STATUS = Param \
(
	identifier = 'alarm_status',
	getter_identifier = 'alarm_status',
	setter_identifier = 'alarm_status',
	description = 'Device alarm current status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = \
	{
		0: 'No alarm',
        1: 'Motion detection alarm',
        2: 'Input alarm',
        3: 'Sensor alarm'},
	identifiers = {},
)
ALARM_TEMPERATURE = Param \
(
	identifier = 'alarm_temperature',
	getter_identifier = 'alarm_temperture',
	setter_identifier = 'alarm_temperature',
	description = 'temperature alarm',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = \
	{
		0: 'disable temperature alarm',
                1: 'high sensitivity',
                2: 'medium sensitivity',
                3: 'low sensitivity (unused)'},
	identifiers = {},
)
APP_VERSION = Param \
(
	identifier = 'app_version',
	getter_identifier = 'app_version',
	setter_identifier = 'app_version',
	description = 'User interface firmware version',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_CHANNEL = Param \
(
	identifier = 'ap_channel',
	getter_identifier = 'ap_channel',
	setter_identifier = 'ap_channel',
	description = 'Wireless channel number',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_DBM_0 = Param \
(
	identifier = 'ap_dbm_0',
	getter_identifier = 'ap_dbm0',
	setter_identifier = 'ap_dbm_0',
	description = 'DBM0 signal strength',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_DBM_1 = Param \
(
	identifier = 'ap_dbm_1',
	getter_identifier = 'ap_dbm1',
	setter_identifier = 'ap_dbm_1',
	description = 'DBM1 signal strength',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_MAC = Param \
(
	identifier = 'ap_mac',
	getter_identifier = 'ap_mac',
	setter_identifier = 'ap_mac',
	description = 'WIFI router MAC address',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_MODE = Param \
(
	identifier = 'ap_mode',
	getter_identifier = 'ap_mode',
	setter_identifier = 'ap_mode',
	description = 'Working mode',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {0: 'Infra', 1: 'adhoc'},
	identifiers = {},
)
AP_NUMBER = Param \
(
	identifier = 'ap_number',
	getter_identifier = 'ap_number',
	setter_identifier = 'ap_number',
	description = "Limit on how many SSID's can be searched",
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
AP_SECURITY = Param \
(
	identifier = 'ap_security',
	getter_identifier = 'ap_security',
	setter_identifier = 'ap_security',
	description = 'Safety mode',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = \
	{
		1: None,
        2: 'WEP',
        3: 'WPA-PSK AES',
        4: 'WPA-PSK TKIP',
        5: 'WPA2-PSK AES',
        6: 'WPA2-PSK TKIP'},
	identifiers = {},
)
AP_SSID = Param \
(
	identifier = 'ap_ssid',
	getter_identifier = 'ap_ssid',
	setter_identifier = 'ap_ssid',
	description = 'WIFI SSID',
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
DDNS_MODE = Param \
(
	identifier = 'ddns_mode',
	getter_identifier = 'ddns_mode',
	setter_identifier = 'ddns_mode',
	description = ('DDNS mode. Call set_ddns?serviceindex=13 to enable and '
 'set_ddns?serviceindex=0 to disable'),
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
DDNS_STATUS = Param \
(
	identifier = 'ddns_status',
	getter_identifier = 'ddns_status',
	setter_identifier = 'ddns_status',
	description = 'Current ddns status',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
DEVICE_SUB_TYPE = Param \
(
	identifier = 'device_sub_type',
	getter_identifier = 'devicesubtype',
	setter_identifier = 'device_sub_type',
	description = 'Factory-defined device function sub-type. Unused',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
DNS_ENABLE = Param \
(
	identifier = 'dns_enable',
	getter_identifier = 'dnsenable',
	setter_identifier = 'dns_enable',
	description = 'Indicates whether third-party DNS is enabled',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
DNS_STATUS = Param \
(
	identifier = 'dns_status',
	getter_identifier = 'dns_status',
	setter_identifier = 'dns_status',
	description = 'DNS status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
ENCRYPT = Param \
(
	identifier = 'encrypt',
	getter_identifier = 'encrypt',
	setter_identifier = 'encrypt',
	description = 'Encryption check',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {0: 'Encryption check successful', 1: 'Encryption check unsuccessful'},
	identifiers = {},
)
ENC_SUB_MODE = Param \
(
	identifier = 'enc_sub_mode',
	getter_identifier = 'enc_sub_mode',
	setter_identifier = 'enc_sub_mode',
	description = 'enc_sub_mode',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
EXTERN_WIFI = Param \
(
	identifier = 'extern_wifi',
	getter_identifier = 'externwifi',
	setter_identifier = 'extern_wifi',
	description = 'extern_wifi. Unused',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
FACTORY_DDNS_STATUS = Param \
(
	identifier = 'factory_ddns_status',
	getter_identifier = 'factory_status',
	setter_identifier = 'factory_status',
	description = 'Factory ddns status',
	constant = None,
	constant_assumed = None,
	getter = 'get_factory_param.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
INTERNET = Param \
(
	identifier = 'internet',
	getter_identifier = 'internet',
	setter_identifier = 'internet',
	description = 'Network status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = \
	{
		1: "Device isn't connected to the internet",
                2: 'Device is connected to the internet'},
	identifiers = {},
)
MAC = Param \
(
	identifier = 'mac',
	getter_identifier = 'mac',
	setter_identifier = 'mac',
	description = 'Wired MAC address',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
MAIL_INET_IP = Param \
(
	identifier = 'mail_inet_ip',
	getter_identifier = 'mail_inet_ip',
	setter_identifier = 'mail_inet_ip',
	description = ('Whether send email notification when Camera inetip changes. Changes when you '
 'call set_mail?smtpport={port}'),
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {0: 'no', 1: 'yes'},
	identifiers = {},
)
OEM_ID = Param \
(
	identifier = 'oem_id',
	getter_identifier = 'oem_id',
	setter_identifier = 'oem_id',
	description = 'OEM client code',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
P2P_STATUS = Param \
(
	identifier = 'p2p_status',
	getter_identifier = 'p2pstatus',
	setter_identifier = 'p2p_status',
	description = 'P2P connection status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = \
	{
		0: "Device heart-beat didn't reach P2P server",
                1: 'Device has heart-beat and reached P2P server'},
	identifiers = {},
)
P2P_UPNP_ENABLE = Param \
(
	identifier = 'p2p_upnp_enable',
	getter_identifier = 'p2p_upnp_enable',
	setter_identifier = 'p2p_upnp_enable',
	description = 'P2P upnp mapping. Potentially unused.',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PAGE_COUNT = Param \
(
	identifier = 'page_count',
	getter_identifier = 'PageCount',
	setter_identifier = 'page_count',
	description = 'Total number of pages',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PARAMS_MD5 = Param \
(
	identifier = 'params_md5',
	getter_identifier = 'params_md5',
	setter_identifier = 'params_md5',
	description = 'params_md5',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PASSWORD_CHANGE_REALTIME = Param \
(
	identifier = 'password_change_realtime',
	getter_identifier = 'pwd_change_realtime',
	setter_identifier = 'password_change_realtime',
	description = 'password_change_realtime',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PRI = Param \
(
	identifier = 'pri',
	getter_identifier = 'pri',
	setter_identifier = 'pri',
	description = "Current user's privileges",
	constant = None,
	constant_assumed = None,
	getter = 'get_wifi_scan_result.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
RECORD_COUNT = Param \
(
	identifier = 'record_count',
	getter_identifier = 'RecordCount',
	setter_identifier = 'record_count',
	description = 'total recording files',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {100: 'Default'},
	identifiers = {},
)
RECORD_NAME_0 = Param \
(
	identifier = 'record_name_0',
	getter_identifier = 'record_name0',
	setter_identifier = 'record_name_0',
	description = 'recording file names',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
RECORD_NUM_0 = Param \
(
	identifier = 'record_num_0',
	getter_identifier = 'record_num0',
	setter_identifier = 'record_num_0',
	description = ('recording file number, query one time, max file number depends on SD card '
 'capacity'),
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
RECORD_SD_STATUS = Param \
(
	identifier = 'record_sd_status',
	getter_identifier = 'record_sd_status',
	setter_identifier = 'record_sd_status',
	description = 'TF card status',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
RECORD_SIZE = Param \
(
	identifier = 'record_size',
	getter_identifier = 'record_size',
	setter_identifier = 'record_size',
	description = 'record_size',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
RECORD_SIZE_0 = Param \
(
	identifier = 'record_size_0',
	getter_identifier = 'record_size0',
	setter_identifier = 'record_size_0',
	description = 'recording file sizes',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
SD_FREE = Param \
(
	identifier = 'sd_free',
	getter_identifier = 'sdfree',
	setter_identifier = 'sd_free',
	description = 'TF card remaining storage',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
SD_LEVEL = Param \
(
	identifier = 'sd_level',
	getter_identifier = 'sdlevel',
	setter_identifier = 'sd_level',
	description = 'TF card remaining capacity',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
SD_STATUS = Param \
(
	identifier = 'sd_status',
	getter_identifier = 'sdstatus',
	setter_identifier = 'sd_status',
	description = 'TF card status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
SD_TOTAL = Param \
(
	identifier = 'sd_total',
	getter_identifier = 'sdtotal',
	setter_identifier = 'sd_total',
	description = 'TF card total capacity',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
SUPPORT_ADPCM_VERSION = Param \
(
	identifier = 'support_adpcm_version',
	getter_identifier = 'support_adpcm_version',
	setter_identifier = 'support_adpcm_version',
	description = 'Support ADPCM version',
	constant = None,
	constant_assumed = None,
	getter = 'get_factory_param.cgi',
	setter = None,
	values = \
	{
		1: 'firmware only supports ADPCM audio data index and '
                   'reference are cleared.',
                2: 'firmware supports ADPCM audio data index and reference '
                   'both are not cleared. if no such field , then default is '
                   'firmware only support ADPCM audio data index and reference '
                   'are cleared.'},
	identifiers = {},
)
SUPPORT_CLOUD_STORAGE = Param \
(
	identifier = 'support_cloud_storage',
	getter_identifier = 'support_cloud_storage',
	setter_identifier = 'support_cloud_storage',
	description = 'support cloud storage',
	constant = None,
	constant_assumed = None,
	getter = 'get_factory_param.cgi',
	setter = None,
	values = {1: 'support cloud storage'},
	identifiers = {},
)
SUPPORT_PIGEON_PUSH = Param \
(
	identifier = 'support_pigeon_push',
	getter_identifier = 'support_pigeon_push',
	setter_identifier = 'support_pigeon_push',
	description = 'support pigeon push',
	constant = None,
	constant_assumed = None,
	getter = 'get_factory_param.cgi',
	setter = None,
	values = {1: 'Pigeon pushes 1.0', 2: 'Pegeon pushes 2.0'},
	identifiers = {},
)
SYSTEM_WIFI_MODE = Param \
(
	identifier = 'system_wifi_mode',
	getter_identifier = 'syswifi_mode',
	setter_identifier = 'system_wifi_mode',
	description = 'System WIFI status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {0: 'Station mode', 1: 'AP mode'},
	identifiers = {},
)
TF_ENABLE = Param \
(
	identifier = 'tf_enable',
	getter_identifier = 'tf_enable',
	setter_identifier = 'tf_enable',
	description = 'TF card loading status',
	constant = None,
	constant_assumed = None,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
TIMEPLAN_VERSION = Param \
(
	identifier = 'timeplan_version',
	getter_identifier = 'timeplan_ver',
	setter_identifier = 'timeplan_version',
	description = 'timeplan_version',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
TIME_NOW = Param \
(
	identifier = 'time_now',
	getter_identifier = 'now',
	setter_identifier = 'time_now',
	description = 'Seconds past from 1970',
	constant = None,
	constant_assumed = None,
	getter = 'get_params.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
UNDER = Param \
(
	identifier = 'under',
	getter_identifier = 'under',
	setter_identifier = 'under',
	description = 'Whether arrears. Unused',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {0: 'Device working properly', 1: 'Device has been delinquent'},
	identifiers = {},
)
UPNP_STATUS = Param \
(
	identifier = 'upnp_status',
	getter_identifier = 'upnp_status',
	setter_identifier = 'upnp_status',
	description = 'upnp_status',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PAGE_INDEX = Param \
(
	identifier = 'page_index',
	getter_identifier = 'PageIndex',
	setter_identifier = 'page_index',
	description = 'access TF card video PageIndex PageSize record file.',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
PAGE_SIZE = Param \
(
	identifier = 'page_size',
	getter_identifier = 'PageSize',
	setter_identifier = 'page_size',
	description = 'The maximum number of video files once returned.',
	constant = None,
	constant_assumed = None,
	getter = 'get_record_file.cgi',
	setter = None,
	values = {},
	identifiers = {},
)
ADC_V = Param \
(
	identifier = 'adc_v',
	getter_identifier = 'adc_v',
	setter_identifier = 'adc_v',
	description = 'adc_v',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
"""
CAMERATYPE = Param \
(
	identifier = 'cameratype',
	getter_identifier = 'cameratype',
	setter_identifier = 'cameratype',
	description = 'camera type',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {0: 'solomon ssd1935', 1: 'rt5350', 2: 'ar9331', 3: 'hi3518e'},
	identifiers = {},
)
"""
CAMERA_TYPE = Param \
(
	identifier = 'camera_type',
	getter_identifier = 'camera_type',
	setter_identifier = 'camera_type',
	description = 'camera type',
	constant = None,
	constant_assumed = None,
	getter = 'get_status.cgi',
	setter = None,
	values = \
	{
		0: 'solomon ssd1935',
		1: 'rt5350',
		2: 'ar9331',
		3: 'hi3518e'
	},
	identifiers = \
	{
		'get_camera_params.cgi': 'cameratype',
		'get_status.cgi': 'camera_type'
	}
)
COMMAND = Param \
(
	identifier = 'command',
	getter_identifier = 'command',
	setter_identifier = 'command',
	description = 'command',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
EXP_ADC = Param \
(
	identifier = 'exp_adc',
	getter_identifier = 'exp_adc',
	setter_identifier = 'exp_adc',
	description = 'exp_adc',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
EXP_AVELUM = Param \
(
	identifier = 'exp_avelum',
	getter_identifier = 'exp_avelum',
	setter_identifier = 'exp_avelum',
	description = 'exp_avelum',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
EXP_GAIN = Param \
(
	identifier = 'exp_gain',
	getter_identifier = 'exp_gain',
	setter_identifier = 'exp_gain',
	description = 'exp_gain',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
GET_ADC = Param \
(
	identifier = 'get_adc',
	getter_identifier = 'get_adc',
	setter_identifier = 'get_adc',
	description = 'get_adc',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
GET_AVELUM = Param \
(
	identifier = 'get_avelum',
	getter_identifier = 'get_avelum',
	setter_identifier = 'get_avelum',
	description = 'get_avelum',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
GET_GAIN = Param \
(
	identifier = 'get_gain',
	getter_identifier = 'get_gain',
	setter_identifier = 'get_gain',
	description = 'get_gain',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
IR_ATTR = Param \
(
	identifier = 'ir_attr',
	getter_identifier = 'ir_attr',
	setter_identifier = 'ir_attr',
	description = 'ir_attr',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
IR_OFF_COM = Param \
(
	identifier = 'ir_off_com',
	getter_identifier = 'ir_off_com',
	setter_identifier = 'ir_off_com',
	description = 'ir_off_com',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
IR_OFF_VAL = Param \
(
	identifier = 'ir_off_val',
	getter_identifier = 'ir_off_val',
	setter_identifier = 'ir_off_val',
	description = 'ir_off_val',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
IR_ON_COM = Param \
(
	identifier = 'ir_on_com',
	getter_identifier = 'ir_on_com',
	setter_identifier = 'ir_on_com',
	description = 'ir_on_com',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
IR_ON_VAL = Param \
(
	identifier = 'ir_on_val',
	getter_identifier = 'ir_on_val',
	setter_identifier = 'ir_on_val',
	description = 'ir_on_val',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
LOGINPAS = Param \
(
	identifier = 'loginpas',
	getter_identifier = 'loginpas',
	setter_identifier = 'loginpas',
	description = 'Current users password',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {'login.cgi': 'loginpass'},
)
LOGINUSE = Param \
(
	identifier = 'loginuse',
	getter_identifier = 'loginuse',
	setter_identifier = 'loginuse',
	description = 'Current users username',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {'login.cgi': 'loginuser'},
)
LOG_TEXT = Param \
(
	identifier = 'log_text',
	getter_identifier = 'log_text',
	setter_identifier = 'log_text',
	description = 'Log text',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
MAINSTREAMHEIGHT = Param \
(
	identifier = 'MainStreamHeight',
	getter_identifier = 'MainStreamHeight',
	setter_identifier = 'MainStreamHeight',
	description = 'Main stream height',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {180: '180p', 360: '360p', 720: '720p'},
	identifiers = {},
)
MAINSTREAMWIDTH = Param \
(
	identifier = 'MainStreamWidth',
	getter_identifier = 'MainStreamWidth',
	setter_identifier = 'MainStreamWidth',
	description = 'Main stream width',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {320: '320p', 640: '640p', 1280: '1280p'},
	identifiers = {},
)
NAME = Param \
(
	identifier = 'name',
	getter_identifier = 'name',
	setter_identifier = 'name',
	description = 'name',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
ONESTEP = Param \
(
	identifier = 'onestep',
	getter_identifier = 'onestep',
	setter_identifier = 'onestep',
	description = 'onestep',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
PARAM = Param \
(
	identifier = 'param',
	getter_identifier = 'param',
	setter_identifier = 'param',
	description = 'param',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
RESOLUTION = Param \
(
	identifier = 'resolution',
	getter_identifier = 'resolution',
	setter_identifier = 'resolution',
	description = 'main stream resolution',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {2: '1280*720', 3: '1280*920', 4: '1920*1080'},
	identifiers = {},
)
RESOLUTIONSUB = Param \
(
	identifier = 'resolutionsub',
	getter_identifier = 'resolutionsub',
	setter_identifier = 'resolutionsub',
	description = 'secondary stream resolution',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {0: '640*360', 2: '1280*720'},
	identifiers = {},
)
RESOLUTIONSUBSUB = Param \
(
	identifier = 'resolutionsubsub',
	getter_identifier = 'resolutionsubsub',
	setter_identifier = 'resolutionsubsub',
	description = 'third stream resolution',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {0: '640*360', 1: '320*180'},
	identifiers = {},
)
RESULT = Param \
(
	identifier = 'result',
	getter_identifier = 'result',
	setter_identifier = 'result',
	description = 'result',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
SIT = Param \
(
	identifier = 'sit',
	getter_identifier = 'sit',
	setter_identifier = 'sit',
	description = 'sit',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
SYS_VER = Param \
(
	identifier = 'sys_ver',
	getter_identifier = 'sys_ver',
	setter_identifier = 'sys_ver',
	description = 'system firmware version',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
VALUE = Param \
(
	identifier = 'value',
	getter_identifier = 'value',
	setter_identifier = 'value',
	description = 'value',
	constant = None,
	constant_assumed = None,
	getter = None,
	setter = None,
	values = {},
	identifiers = {},
)
