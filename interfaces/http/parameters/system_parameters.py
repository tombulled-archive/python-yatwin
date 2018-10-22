from .parameter_types.SystemParam import SystemParam

"""
Library containing system parameters.

These parameters are both sent and retrieved (potentially under different names)
... therefore they need a reference to both a setter and a getter

Imports:
	.parameter_types.SystemParam.SytemParam
"""

ALARM_INPUT_ARMED = SystemParam \
(
	identifier = 'alarm_input_armed',
	getter_identifier = 'alarm_input_armed',
	setter_identifier = 'input_armed',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_IOIN_LEVEL = SystemParam \
(
	identifier = 'alarm_ioin_level',
	getter_identifier = 'alarm_ioin_level',
	setter_identifier = 'ioin_level',
	description = 'Input alarm trigger level (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_IOLINKAGE = SystemParam \
(
	identifier = 'alarm_iolinkage',
	getter_identifier = 'alarm_iolinkage',
	setter_identifier = 'iolinkage',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_IOOUT_LEVEL = SystemParam \
(
	identifier = 'alarm_ioout_level',
	getter_identifier = 'alarm_ioout_level',
	setter_identifier = 'ioout_level',
	description = 'io linkage output level (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
APSWIFI_PORT = SystemParam \
(
	identifier = 'apswifi_port',
	getter_identifier = 'apswifi_port',
	setter_identifier = 'apswifi_port',
	description = 'AP port',
	constant = True,
	constant_assumed = False,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
CUSTOMER_CODE = SystemParam \
(
	identifier = 'customer_code',
	getter_identifier = 'customer_code',
	setter_identifier = 'customer_code',
	description = 'Customer code',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
ENC_MAIN_MODE = SystemParam \
(
	identifier = 'enc_main_mode',
	getter_identifier = 'enc_main_mode',
	setter_identifier = 'enc_main_mode',
	description = 'Main encryption mode. Must set mainrate=0 to edit',
	constant = True,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
FACTORY_PRODUCTION_ORDER = SystemParam \
(
	identifier = 'factory_production_order',
	getter_identifier = 'production_order',
	setter_identifier = 'production_order',
	description = 'Production order',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_SHIPMENT_ORDER = SystemParam \
(
	identifier = 'factory_shipment_order',
	getter_identifier = 'shipment_order',
	setter_identifier = 'shipment_order',
	description = 'Shipment order',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FTP_FILENAME = SystemParam \
(
	identifier = 'ftp_filename',
	getter_identifier = 'ftp_filename',
	setter_identifier = 'filename',
	description = 'ftp save file name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
IP = SystemParam \
(
	identifier = 'ip',
	getter_identifier = 'ip',
	setter_identifier = 'ip',
	description = 'Camera IP address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_1 = SystemParam \
(
	identifier = 'motion_plan_1',
	getter_identifier = 'motion_plan1',
	setter_identifier = 'motion_plan1',
	description = 'Motion plan 1',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_10 = SystemParam \
(
	identifier = 'motion_plan_10',
	getter_identifier = 'motion_plan10',
	setter_identifier = 'motion_plan10',
	description = 'Motion plan 10',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_11 = SystemParam \
(
	identifier = 'motion_plan_11',
	getter_identifier = 'motion_plan11',
	setter_identifier = 'motion_plan11',
	description = 'Motion plan 11',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_12 = SystemParam \
(
	identifier = 'motion_plan_12',
	getter_identifier = 'motion_plan12',
	setter_identifier = 'motion_plan12',
	description = 'Motion plan 12',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_13 = SystemParam \
(
	identifier = 'motion_plan_13',
	getter_identifier = 'motion_plan13',
	setter_identifier = 'motion_plan13',
	description = 'Motion plan 13',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_14 = SystemParam \
(
	identifier = 'motion_plan_14',
	getter_identifier = 'motion_plan14',
	setter_identifier = 'motion_plan14',
	description = 'Motion plan 14',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_15 = SystemParam \
(
	identifier = 'motion_plan_15',
	getter_identifier = 'motion_plan15',
	setter_identifier = 'motion_plan15',
	description = 'Motion plan 15',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_16 = SystemParam \
(
	identifier = 'motion_plan_16',
	getter_identifier = 'motion_plan16',
	setter_identifier = 'motion_plan16',
	description = 'Motion plan 16',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_17 = SystemParam \
(
	identifier = 'motion_plan_17',
	getter_identifier = 'motion_plan17',
	setter_identifier = 'motion_plan17',
	description = 'Motion plan 17',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_18 = SystemParam \
(
	identifier = 'motion_plan_18',
	getter_identifier = 'motion_plan18',
	setter_identifier = 'motion_plan18',
	description = 'Motion plan 18',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_19 = SystemParam \
(
	identifier = 'motion_plan_19',
	getter_identifier = 'motion_plan19',
	setter_identifier = 'motion_plan19',
	description = 'Motion plan 19',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_2 = SystemParam \
(
	identifier = 'motion_plan_2',
	getter_identifier = 'motion_plan2',
	setter_identifier = 'motion_plan2',
	description = 'Motion plan 2',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_20 = SystemParam \
(
	identifier = 'motion_plan_20',
	getter_identifier = 'motion_plan20',
	setter_identifier = 'motion_plan20',
	description = 'Motion plan 20',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_21 = SystemParam \
(
	identifier = 'motion_plan_21',
	getter_identifier = 'motion_plan21',
	setter_identifier = 'motion_plan21',
	description = 'Motion plan 21',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_3 = SystemParam \
(
	identifier = 'motion_plan_3',
	getter_identifier = 'motion_plan3',
	setter_identifier = 'motion_plan3',
	description = 'Motion plan 3',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_4 = SystemParam \
(
	identifier = 'motion_plan_4',
	getter_identifier = 'motion_plan4',
	setter_identifier = 'motion_plan4',
	description = 'Motion plan 4',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_5 = SystemParam \
(
	identifier = 'motion_plan_5',
	getter_identifier = 'motion_plan5',
	setter_identifier = 'motion_plan5',
	description = 'Motion plan 5',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_6 = SystemParam \
(
	identifier = 'motion_plan_6',
	getter_identifier = 'motion_plan6',
	setter_identifier = 'motion_plan6',
	description = 'Motion plan 6',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_7 = SystemParam \
(
	identifier = 'motion_plan_7',
	getter_identifier = 'motion_plan7',
	setter_identifier = 'motion_plan7',
	description = 'Motion plan 7',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_8 = SystemParam \
(
	identifier = 'motion_plan_8',
	getter_identifier = 'motion_plan8',
	setter_identifier = 'motion_plan8',
	description = 'Motion plan 8',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
MOTION_PLAN_9 = SystemParam \
(
	identifier = 'motion_plan_9',
	getter_identifier = 'motion_plan9',
	setter_identifier = 'motion_plan9',
	description = 'Motion plan 9',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
RECORD_CHANNEL = SystemParam \
(
	identifier = 'record_channel',
	getter_identifier = 'record_chnl',
	setter_identifier = 'record_chnl',
	description = 'Channel to record',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		0: 'Record main stream',
        1: 'Record secondary stream',
        2: 'Record third stream'},
	identifiers = {},
)
RECORD_TIMER = SystemParam \
(
	identifier = 'record_timer',
	getter_identifier = 'record_timer',
	setter_identifier = 'record_timer',
	description = 'Recording duration',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = {},
	identifiers = {},
)
ADC_MAX = SystemParam \
(
	identifier = 'adc_max',
	getter_identifier = 'adc_max',
	setter_identifier = 'adcmax',
	description = 'setup ADC maximum value',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_extra.cgi',
	setter = 'set_factory_extra.cgi',
	values = {},
	identifiers = {},
)
ADC_MIN = SystemParam \
(
	identifier = 'adc_min',
	getter_identifier = 'adc_min',
	setter_identifier = 'adcmin',
	description = 'setup ACD minimum value',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_extra.cgi',
	setter = 'set_factory_extra.cgi',
	values = {},
	identifiers = {},
)
ADC_USE = SystemParam \
(
	identifier = 'adc_use',
	getter_identifier = 'adc_use',
	setter_identifier = 'adc_use',
	description = 'means whether to enable ADC',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_extra.cgi',
	setter = 'set_factory_extra.cgi',
	values = {1: 'disableADC', 2: 'enable ADC'},
	identifiers = {},
)
AGING_ENABLE = SystemParam \
(
	identifier = 'aging_enable',
	getter_identifier = 'enable',
	setter_identifier = 'enable',
	description = 'whether enable aging mode',
	constant = False,
	constant_assumed = False,
	getter = 'get_aging.cgi',
	setter = 'set_aging.cgi',
	values = {0: 'turn off aging mode', 1: 'turn on aging mode'},
	identifiers = {},
)
ALARM_AUDIO = SystemParam \
(
	identifier = 'alarm_audio',
	getter_identifier = 'alarm_audio',
	setter_identifier = 'alarm_audio',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable', 1: 'high sensitivity', 2: 'medium', 3: 'low sensitivity'},
	identifiers = {},
)
ALARM_HTTP = SystemParam \
(
	identifier = 'alarm_http',
	getter_identifier = 'alarm_http',
	setter_identifier = 'alarm_http',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable', 1: 'enable'},
	identifiers = {},
)
ALARM_HTTP_URL = SystemParam \
(
	identifier = 'alarm_http_url',
	getter_identifier = 'alarm_http_url',
	setter_identifier = 'alarm_http_url',
	description = 'Alarm access URL (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_MAIL = SystemParam \
(
	identifier = 'alarm_mail',
	getter_identifier = 'alarm_mail',
	setter_identifier = 'mail',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable alarm mail notification', 1: 'enable alarm mail notification'},
	identifiers = {},
)
ALARM_MOTION_ARMED = SystemParam \
(
	identifier = 'alarm_motion_armed',
	getter_identifier = 'alarm_motion_armed',
	setter_identifier = 'motion_armed',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Disarming motion detection', 1: 'motion detection arming'},
	identifiers = {},
)
ALARM_MOTION_SENSITIVITY = SystemParam \
(
	identifier = 'alarm_motion_sensitivity',
	getter_identifier = 'alarm_motion_sensitivity',
	setter_identifier = 'motion_sensitivity',
	description = '0-9: high to low',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_PRESETSIT = SystemParam \
(
	identifier = 'alarm_presetsit',
	getter_identifier = 'alarm_presetsit',
	setter_identifier = 'preset',
	description = 'linkage preset position when alarm',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_PWD = SystemParam \
(
	identifier = 'alarm_pwd',
	getter_identifier = 'alarm_pwd',
	setter_identifier = 'alarmpasswd',
	description = 'http url password when alarm (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_RECORD = SystemParam \
(
	identifier = 'alarm_record',
	getter_identifier = 'alarm_record',
	setter_identifier = 'record',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable alarm recording', 1: 'enable alarm recording'},
	identifiers = {},
)
ALARM_SCHEDULE_ENABLE = SystemParam \
(
	identifier = 'alarm_schedule_enable',
	getter_identifier = 'alarm_schedule_enable',
	setter_identifier = 'schedule_enable',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable arming program', 1: 'start arming plan'},
	identifiers = {},
)
ALARM_SCHEDULE_FRI_0 = SystemParam \
(
	identifier = 'alarm_schedule_fri_0',
	getter_identifier = 'alarm_schedule_fri_0',
	setter_identifier = 'schedule_fri_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_FRI_1 = SystemParam \
(
	identifier = 'alarm_schedule_fri_1',
	getter_identifier = 'alarm_schedule_fri_1',
	setter_identifier = 'schedule_fri_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_FRI_2 = SystemParam \
(
	identifier = 'alarm_schedule_fri_2',
	getter_identifier = 'alarm_schedule_fri_2',
	setter_identifier = 'schedule_fri_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_MON_0 = SystemParam \
(
	identifier = 'alarm_schedule_mon_0',
	getter_identifier = 'alarm_schedule_mon_0',
	setter_identifier = 'schedule_mon_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_MON_1 = SystemParam \
(
	identifier = 'alarm_schedule_mon_1',
	getter_identifier = 'alarm_schedule_mon_1',
	setter_identifier = 'schedule_mon_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_MON_2 = SystemParam \
(
	identifier = 'alarm_schedule_mon_2',
	getter_identifier = 'alarm_schedule_mon_2',
	setter_identifier = 'schedule_mon_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SAT_0 = SystemParam \
(
	identifier = 'alarm_schedule_sat_0',
	getter_identifier = 'alarm_schedule_sat_0',
	setter_identifier = 'schedule_sat_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SAT_1 = SystemParam \
(
	identifier = 'alarm_schedule_sat_1',
	getter_identifier = 'alarm_schedule_sat_1',
	setter_identifier = 'schedule_sat_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SAT_2 = SystemParam \
(
	identifier = 'alarm_schedule_sat_2',
	getter_identifier = 'alarm_schedule_sat_2',
	setter_identifier = 'schedule_sat_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SUN_0 = SystemParam \
(
	identifier = 'alarm_schedule_sun_0',
	getter_identifier = 'alarm_schedule_sun_0',
	setter_identifier = 'schedule_sun_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SUN_1 = SystemParam \
(
	identifier = 'alarm_schedule_sun_1',
	getter_identifier = 'alarm_schedule_sun_1',
	setter_identifier = 'schedule_sun_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_SUN_2 = SystemParam \
(
	identifier = 'alarm_schedule_sun_2',
	getter_identifier = 'alarm_schedule_sun_2',
	setter_identifier = 'schedule_sun_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_THU_0 = SystemParam \
(
	identifier = 'alarm_schedule_thu_0',
	getter_identifier = 'alarm_schedule_thu_0',
	setter_identifier = 'schedule_thu_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_THU_1 = SystemParam \
(
	identifier = 'alarm_schedule_thu_1',
	getter_identifier = 'alarm_schedule_thu_1',
	setter_identifier = 'schedule_thu_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_THU_2 = SystemParam \
(
	identifier = 'alarm_schedule_thu_2',
	getter_identifier = 'alarm_schedule_thu_2',
	setter_identifier = 'schedule_thu_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_TUE_0 = SystemParam \
(
	identifier = 'alarm_schedule_tue_0',
	getter_identifier = 'alarm_schedule_tue_0',
	setter_identifier = 'schedule_tue_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_TUE_1 = SystemParam \
(
	identifier = 'alarm_schedule_tue_1',
	getter_identifier = 'alarm_schedule_tue_1',
	setter_identifier = 'schedule_tue_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_TUE_2 = SystemParam \
(
	identifier = 'alarm_schedule_tue_2',
	getter_identifier = 'alarm_schedule_tue_2',
	setter_identifier = 'schedule_tue_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_WED_0 = SystemParam \
(
	identifier = 'alarm_schedule_wed_0',
	getter_identifier = 'alarm_schedule_wed_0',
	setter_identifier = 'schedule_wed_0',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_WED_1 = SystemParam \
(
	identifier = 'alarm_schedule_wed_1',
	getter_identifier = 'alarm_schedule_wed_1',
	setter_identifier = 'schedule_wed_1',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SCHEDULE_WED_2 = SystemParam \
(
	identifier = 'alarm_schedule_wed_2',
	getter_identifier = 'alarm_schedule_wed_2',
	setter_identifier = 'schedule_wed_2',
	description = ('Alarm deployment plan from Monday to Sunday, 24 hours a day, 15mins per '
 'period, total 96 arming period. bit0-95'),
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'Not armed in this time', 1: 'arming in this time'},
	identifiers = {},
)
ALARM_SERVER = SystemParam \
(
	identifier = 'alarm_server',
	getter_identifier = 'alarm_server',
	setter_identifier = 'alarmserver',
	description = 'http url domain name when alarm (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALARM_SNAPSHOT = SystemParam \
(
	identifier = 'alarm_snapshot',
	getter_identifier = 'alarm_snapshot',
	setter_identifier = 'snapshot',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: "Don'tsnapshot when alarm", 1: 'Snapshot when alarm'},
	identifiers = {},
)
ALARM_UPLOAD_INTERVAL = SystemParam \
(
	identifier = 'alarm_upload_interval',
	getter_identifier = 'alarm_upload_interval',
	setter_identifier = 'upload_interval',
	description = 'Picture upload interval (s) when alarm',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {0: 'disable'},
	identifiers = {},
)
ALARM_USER = SystemParam \
(
	identifier = 'alarm_user',
	getter_identifier = 'alarm_user',
	setter_identifier = 'alarmuser',
	description = 'http url user name when alarm (unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_alarm.cgi',
	values = {},
	identifiers = {},
)
ALIAS = SystemParam \
(
	identifier = 'alias',
	getter_identifier = 'alias',
	setter_identifier = 'alias',
	description = 'device name, max 32 bit',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_alias.cgi',
	values = {},
	identifiers = {},
)
APWIFI_ENCRYPT = SystemParam \
(
	identifier = 'apwifi_encrypt',
	getter_identifier = 'apwifi_encrypt',
	setter_identifier = 'apwifi_encrypt',
	description = 'means AP encrypted authentication mode',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_ENDIP = SystemParam \
(
	identifier = 'apwifi_endip',
	getter_identifier = 'apwifi_endip',
	setter_identifier = 'apwifi_endip',
	description = 'WiFi ends IP address',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_IPADDR = SystemParam \
(
	identifier = 'apwifi_ipaddr',
	getter_identifier = 'apwifi_ipaddr',
	setter_identifier = 'apwifi_ipaddr',
	description = 'WiFi IP address',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_KEY = SystemParam \
(
	identifier = 'apwifi_key',
	getter_identifier = 'apwifi_key',
	setter_identifier = 'apwifi_key',
	description = 'encrypted string',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_MASK = SystemParam \
(
	identifier = 'apwifi_mask',
	getter_identifier = 'apwifi_mask',
	setter_identifier = 'apwifi_mask',
	description = 'WiFi MASK',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_SSID = SystemParam \
(
	identifier = 'apwifi_ssid',
	getter_identifier = 'apwifi_ssid',
	setter_identifier = 'apwifi_ssid',
	description = 'WiFi AP SSID',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
APWIFI_STARTIP = SystemParam \
(
	identifier = 'apwifi_startip',
	getter_identifier = 'apwifi_startip',
	setter_identifier = 'apwifi_startip',
	description = 'WiFi start IP address',
	constant = False,
	constant_assumed = True,
	getter = 'get_apwifi.cgi',
	setter = 'set_apwifi.cgi',
	values = {},
	identifiers = {},
)
DDNS_HOST = SystemParam \
(
	identifier = 'ddns_host',
	getter_identifier = 'ddns_host',
	setter_identifier = 'host',
	description = 'ddns domain name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = {},
	identifiers = {},
)
DDNS_PROXY_PORT = SystemParam \
(
	identifier = 'ddns_proxy_port',
	getter_identifier = 'ddns_proxy_port',
	setter_identifier = 'proxy_port',
	description = 'Proxy port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = {},
	identifiers = {},
)
DDNS_PROXY_SVR = SystemParam \
(
	identifier = 'ddns_proxy_svr',
	getter_identifier = 'ddns_proxy_svr',
	setter_identifier = 'proxy_svr',
	description = 'Proxy address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = {},
	identifiers = {},
)
DDNS_PWD = SystemParam \
(
	identifier = 'ddns_pwd',
	getter_identifier = 'ddns_pwd',
	setter_identifier = 'pwd',
	description = 'ddns password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = {},
	identifiers = {},
)
DDNS_SERVICE = SystemParam \
(
	identifier = 'ddns_service',
	getter_identifier = 'ddns_service',
	setter_identifier = 'service',
	description = 'DDNS serial no.',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = \
	{
		0: 'disable ddns service',
                1: 'DynDns(not supported)',
                2: 'DynDns.org(dyndns)',
                3: 'DynDns.org(statdns)',
                4: 'DynDns.org(custom)',
                5: 'reserve',
                6: 'reserve',
                7: 'reserve',
                8: '3322(dyndns)',
                9: '3322(statdns)',
                10: '9299',
                11: 'Manufacture own',
                12: 'Manufacture own'},
	identifiers = {},
)
DDNS_USER = SystemParam \
(
	identifier = 'ddns_user',
	getter_identifier = 'ddns_user',
	setter_identifier = 'user',
	description = 'ddns user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ddns.cgi',
	values = {},
	identifiers = {},
)
DEV2_ALIAS = SystemParam \
(
	identifier = 'dev2_alias',
	getter_identifier = 'dev2_alias',
	setter_identifier = 'dev2_alias',
	description = 'The second channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV2_HOST = SystemParam \
(
	identifier = 'dev2_host',
	getter_identifier = 'dev2_host',
	setter_identifier = 'dev2_host',
	description = 'Second chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV2_PORT = SystemParam \
(
	identifier = 'dev2_port',
	getter_identifier = 'dev2_port',
	setter_identifier = 'dev2_port',
	description = 'The second channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV2_PWD = SystemParam \
(
	identifier = 'dev2_pwd',
	getter_identifier = 'dev2_pwd',
	setter_identifier = 'dev2_pwd',
	description = 'The second channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV2_USER = SystemParam \
(
	identifier = 'dev2_user',
	getter_identifier = 'dev2_user',
	setter_identifier = 'dev2_user',
	description = 'The second channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV3_ALIAS = SystemParam \
(
	identifier = 'dev3_alias',
	getter_identifier = 'dev3_alias',
	setter_identifier = 'dev3_alias',
	description = 'The third channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV3_HOST = SystemParam \
(
	identifier = 'dev3_host',
	getter_identifier = 'dev3_host',
	setter_identifier = 'dev3_host',
	description = 'Third chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV3_PORT = SystemParam \
(
	identifier = 'dev3_port',
	getter_identifier = 'dev3_port',
	setter_identifier = 'dev3_port',
	description = 'The third channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV3_PWD = SystemParam \
(
	identifier = 'dev3_pwd',
	getter_identifier = 'dev3_pwd',
	setter_identifier = 'dev3_pwd',
	description = 'The third channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV3_USER = SystemParam \
(
	identifier = 'dev3_user',
	getter_identifier = 'dev3_user',
	setter_identifier = 'dev3_user',
	description = 'The third channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV4_ALIAS = SystemParam \
(
	identifier = 'dev4_alias',
	getter_identifier = 'dev4_alias',
	setter_identifier = 'dev4_alias',
	description = 'The fourth channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV4_HOST = SystemParam \
(
	identifier = 'dev4_host',
	getter_identifier = 'dev4_host',
	setter_identifier = 'dev4_host',
	description = 'Fourth chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV4_PORT = SystemParam \
(
	identifier = 'dev4_port',
	getter_identifier = 'dev4_port',
	setter_identifier = 'dev4_port',
	description = 'The fourth channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV4_PWD = SystemParam \
(
	identifier = 'dev4_pwd',
	getter_identifier = 'dev4_pwd',
	setter_identifier = 'dev4_pwd',
	description = 'The fourth channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV4_USER = SystemParam \
(
	identifier = 'dev4_user',
	getter_identifier = 'dev4_user',
	setter_identifier = 'dev4_user',
	description = 'The fourth channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV5_ALIAS = SystemParam \
(
	identifier = 'dev5_alias',
	getter_identifier = 'dev5_alias',
	setter_identifier = 'dev5_alias',
	description = 'The fifth channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV5_HOST = SystemParam \
(
	identifier = 'dev5_host',
	getter_identifier = 'dev5_host',
	setter_identifier = 'dev5_host',
	description = 'Fifth chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV5_PORT = SystemParam \
(
	identifier = 'dev5_port',
	getter_identifier = 'dev5_port',
	setter_identifier = 'dev5_port',
	description = 'The fifth channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV5_PWD = SystemParam \
(
	identifier = 'dev5_pwd',
	getter_identifier = 'dev5_pwd',
	setter_identifier = 'dev5_pwd',
	description = 'The fifth channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV5_USER = SystemParam \
(
	identifier = 'dev5_user',
	getter_identifier = 'dev5_user',
	setter_identifier = 'dev5_user',
	description = 'The fifth channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV6_ALIAS = SystemParam \
(
	identifier = 'dev6_alias',
	getter_identifier = 'dev6_alias',
	setter_identifier = 'dev6_alias',
	description = 'The sixth channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV6_HOST = SystemParam \
(
	identifier = 'dev6_host',
	getter_identifier = 'dev6_host',
	setter_identifier = 'dev6_host',
	description = 'Sixth chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV6_PORT = SystemParam \
(
	identifier = 'dev6_port',
	getter_identifier = 'dev6_port',
	setter_identifier = 'dev6_port',
	description = 'The sixth channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV6_PWD = SystemParam \
(
	identifier = 'dev6_pwd',
	getter_identifier = 'dev6_pwd',
	setter_identifier = 'dev6_pwd',
	description = 'The sixth channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV6_USER = SystemParam \
(
	identifier = 'dev6_user',
	getter_identifier = 'dev6_user',
	setter_identifier = 'dev6_user',
	description = 'The sixth channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV7_ALIAS = SystemParam \
(
	identifier = 'dev7_alias',
	getter_identifier = 'dev7_alias',
	setter_identifier = 'dev7_alias',
	description = 'The seventh channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV7_HOST = SystemParam \
(
	identifier = 'dev7_host',
	getter_identifier = 'dev7_host',
	setter_identifier = 'dev7_host',
	description = 'Seventh chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV7_PORT = SystemParam \
(
	identifier = 'dev7_port',
	getter_identifier = 'dev7_port',
	setter_identifier = 'dev7_port',
	description = 'The seventh channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV7_PWD = SystemParam \
(
	identifier = 'dev7_pwd',
	getter_identifier = 'dev7_pwd',
	setter_identifier = 'dev7_pwd',
	description = 'The seventh channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV7_USER = SystemParam \
(
	identifier = 'dev7_user',
	getter_identifier = 'dev7_user',
	setter_identifier = 'dev7_user',
	description = 'The seventh channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV8_ALIAS = SystemParam \
(
	identifier = 'dev8_alias',
	getter_identifier = 'dev8_alias',
	setter_identifier = 'dev8_alias',
	description = 'The eigth channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV8_HOST = SystemParam \
(
	identifier = 'dev8_host',
	getter_identifier = 'dev8_host',
	setter_identifier = 'dev8_host',
	description = 'Eigth chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV8_PORT = SystemParam \
(
	identifier = 'dev8_port',
	getter_identifier = 'dev8_port',
	setter_identifier = 'dev8_port',
	description = 'The Eigth channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV8_PWD = SystemParam \
(
	identifier = 'dev8_pwd',
	getter_identifier = 'dev8_pwd',
	setter_identifier = 'dev8_pwd',
	description = 'The eigth channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV8_USER = SystemParam \
(
	identifier = 'dev8_user',
	getter_identifier = 'dev8_user',
	setter_identifier = 'dev8_user',
	description = 'The eigth channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV9_ALIAS = SystemParam \
(
	identifier = 'dev9_alias',
	getter_identifier = 'dev9_alias',
	setter_identifier = 'dev9_alias',
	description = 'The ninth channel device other name',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV9_HOST = SystemParam \
(
	identifier = 'dev9_host',
	getter_identifier = 'dev9_host',
	setter_identifier = 'dev9_host',
	description = 'Ninth chancel device address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV9_PORT = SystemParam \
(
	identifier = 'dev9_port',
	getter_identifier = 'dev9_port',
	setter_identifier = 'dev9_port',
	description = 'The ninth channel device HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV9_PWD = SystemParam \
(
	identifier = 'dev9_pwd',
	getter_identifier = 'dev9_pwd',
	setter_identifier = 'dev9_pwd',
	description = 'The ninth channel device visit password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEV9_USER = SystemParam \
(
	identifier = 'dev9_user',
	getter_identifier = 'dev9_user',
	setter_identifier = 'dev9_user',
	description = 'The ninth channel device visit user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_devices.cgi',
	values = {},
	identifiers = {},
)
DEVICEID = SystemParam \
(
	identifier = 'deviceid',
	getter_identifier = 'deviceid',
	setter_identifier = 'deviceid',
	description = 'device UID, max32 bit',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
DEVICETYPE = SystemParam \
(
	identifier = 'devicetype',
	getter_identifier = 'devicetype',
	setter_identifier = 'devicetype',
	description = 'factory-defined device function type, unused',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_extra.cgi',
	values = {},
	identifiers = \
	{
		'get_misc.cgi': 'device_type',
                'get_status.cgi': 'devicetype',
                'set_extra.cgi': 'devicetype'},
)
DHCPEN = SystemParam \
(
	identifier = 'dhcpen',
	getter_identifier = 'dhcpen',
	setter_identifier = 'dhcp',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {0: 'disable DHCP', 1: 'enable DHCP'},
	identifiers = {},
)
DNS1 = SystemParam \
(
	identifier = 'dns1',
	getter_identifier = 'dns1',
	setter_identifier = 'dns1',
	description = 'camera first DNS server',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
DNS2 = SystemParam \
(
	identifier = 'dns2',
	getter_identifier = 'dns2',
	setter_identifier = 'dns2',
	description = 'camera second DNS server',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
ENC_BITRATE = SystemParam \
(
	identifier = 'enc_bitrate',
	getter_identifier = 'enc_bitrate',
	setter_identifier = 'enc_bitrate',
	description = 'main stream bitrate',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
ENC_FRAMERATE = SystemParam \
(
	identifier = 'enc_framerate',
	getter_identifier = 'enc_framerate',
	setter_identifier = 'enc_framerate',
	description = 'main frame rate',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
ENC_KEYFRAME = SystemParam \
(
	identifier = 'enc_keyframe',
	getter_identifier = 'enc_keyframe',
	setter_identifier = 'enc_keyframe',
	description = 'main stream key frame',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
ENC_QUANT = SystemParam \
(
	identifier = 'enc_quant',
	getter_identifier = 'enc_quant',
	setter_identifier = 'enc_quant',
	description = 'main stream quality',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
ENC_RATEMODE = SystemParam \
(
	identifier = 'enc_ratemode',
	getter_identifier = 'enc_ratemode',
	setter_identifier = 'enc_ratemode',
	description = 'main stream mode',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {0: 'means CBR', 1: 'means VBR'},
	identifiers = {},
)
ENC_SIZE = SystemParam \
(
	identifier = 'enc_size',
	getter_identifier = 'enc_size',
	setter_identifier = 'enc_size',
	description = 'consistent with resolution',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
FACTORY_ALARM_SERVER = SystemParam \
(
	identifier = 'factory_alarm_server',
	getter_identifier = 'factory_alarmserver',
	setter_identifier = 'alarm_server',
	description = 'alarm domain',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_DDNS_MODE = SystemParam \
(
	identifier = 'factory_ddns_mode',
	getter_identifier = 'factory_mode',
	setter_identifier = 'mode',
	description = 'ddns mode',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_DOMAIN_PORT = SystemParam \
(
	identifier = 'factory_domain_port',
	getter_identifier = 'factory_port',
	setter_identifier = 'port',
	description = 'domain port',
	constant = False,
	constant_assumed = False,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_HEARTBEAT = SystemParam \
(
	identifier = 'factory_heartbeat',
	getter_identifier = 'factory_heartbeat',
	setter_identifier = 'heartbeat',
	description = 'factory ddns heartbeat',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_INDEX = SystemParam \
(
	identifier = 'factory_index',
	getter_identifier = 'factory_index',
	setter_identifier = 'factory_index',
	description = 'factory serial No.',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_PASSWD = SystemParam \
(
	identifier = 'factory_passwd',
	getter_identifier = 'factory_passwd',
	setter_identifier = 'userpwd',
	description = 'factory ddns password',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_SERVER = SystemParam \
(
	identifier = 'factory_server',
	getter_identifier = 'factory_server',
	setter_identifier = 'server',
	description = 'factory DDNS',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FACTORY_USER = SystemParam \
(
	identifier = 'factory_user',
	getter_identifier = 'factory_user',
	setter_identifier = 'username',
	description = 'factory ddns user name',
	constant = False,
	constant_assumed = True,
	getter = 'get_factory_param.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
FTP_DIR = SystemParam \
(
	identifier = 'ftp_dir',
	getter_identifier = 'ftp_dir',
	setter_identifier = 'dir',
	description = 'ftp server stored directory',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
FTP_MODE = SystemParam \
(
	identifier = 'ftp_mode',
	getter_identifier = 'ftp_mode',
	setter_identifier = 'mode',
	description = '',
	constant = True,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {0: 'port mode', 1: 'pasv mode'},
	identifiers = {},
)
FTP_PORT = SystemParam \
(
	identifier = 'ftp_port',
	getter_identifier = 'ftp_port',
	setter_identifier = 'port',
	description = 'ftp sever port',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
FTP_PWD = SystemParam \
(
	identifier = 'ftp_pwd',
	getter_identifier = 'ftp_pwd',
	setter_identifier = 'pwd',
	description = 'ftp server login password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
FTP_SVR = SystemParam \
(
	identifier = 'ftp_svr',
	getter_identifier = 'ftp_svr',
	setter_identifier = 'svr',
	description = 'ftp server address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
FTP_UPLOAD_INTERVAL = SystemParam \
(
	identifier = 'ftp_upload_interval',
	getter_identifier = 'ftp_upload_interval',
	setter_identifier = 'upload_interval',
	description = 'Instantly upload image interval(s)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
FTP_USER = SystemParam \
(
	identifier = 'ftp_user',
	getter_identifier = 'ftp_user',
	setter_identifier = 'user',
	description = 'ftp server login user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_ftp.cgi',
	values = {},
	identifiers = {},
)
GATEWAY = SystemParam \
(
	identifier = 'gateway',
	getter_identifier = 'gateway',
	setter_identifier = 'gateway',
	description = 'Camera gateway',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
IP_ADDRESS = SystemParam \
(
	identifier = 'ip_address',
	getter_identifier = 'ip',
	setter_identifier = 'ipaddr',
	description = 'camera IP address',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
IRCUT = SystemParam \
(
	identifier = 'ircut',
	getter_identifier = 'ircut',
	setter_identifier = 'val',
	description = 'mens infrared lights',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_ir_gpio.cgi',
	values = {0: 'turn off infrared light', 1: 'Auto infrared'},
	identifiers = {},
)
LED_MODE = SystemParam \
(
	identifier = 'led_mode',
	getter_identifier = 'led_mode',
	setter_identifier = 'led_mode',
	description = 'means the indicator mode',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'turn off indicator', 1: 'turn on indicator'},
	identifiers = {},
)
MAC = SystemParam \
(
	identifier = 'mac',
	getter_identifier = 'mac',
	setter_identifier = 'mac',
	description = 'wired MAC address',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
MAILSSL = SystemParam \
(
	identifier = 'mailssl',
	getter_identifier = 'mailssl',
	setter_identifier = 'ssl',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_PORT = SystemParam \
(
	identifier = 'mail_port',
	getter_identifier = 'mail_port',
	setter_identifier = 'smtpport',
	description = 'Mail server port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_PWD = SystemParam \
(
	identifier = 'mail_pwd',
	getter_identifier = 'mail_pwd',
	setter_identifier = 'pwd',
	description = 'Mail server login password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_RECEIVER1 = SystemParam \
(
	identifier = 'mail_receiver1',
	getter_identifier = 'mail_receiver1',
	setter_identifier = 'receiver1',
	description = 'Mail receiver 1',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_RECEIVER2 = SystemParam \
(
	identifier = 'mail_receiver2',
	getter_identifier = 'mail_receiver2',
	setter_identifier = 'receiver2',
	description = 'Mail receiver 2',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_RECEIVER3 = SystemParam \
(
	identifier = 'mail_receiver3',
	getter_identifier = 'mail_receiver3',
	setter_identifier = 'receiver3',
	description = 'Mail receiver 3',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_RECEIVER4 = SystemParam \
(
	identifier = 'mail_receiver4',
	getter_identifier = 'mail_receiver4',
	setter_identifier = 'receiver4',
	description = 'Mail receiver 4',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_SENDER = SystemParam \
(
	identifier = 'mail_sender',
	getter_identifier = 'mail_sender',
	setter_identifier = 'sender',
	description = 'Mail sender',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_SVR = SystemParam \
(
	identifier = 'mail_svr',
	getter_identifier = 'mail_svr',
	setter_identifier = 'svr',
	description = 'Mail server address',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MAIL_USER = SystemParam \
(
	identifier = 'mail_user',
	getter_identifier = 'mail_user',
	setter_identifier = 'user',
	description = 'Mail sever login user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_mail.cgi',
	values = {},
	identifiers = {},
)
MASK = SystemParam \
(
	identifier = 'mask',
	getter_identifier = 'mask',
	setter_identifier = 'mask',
	description = 'Camera sub net',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
NOW = SystemParam \
(
	identifier = 'now',
	getter_identifier = 'now',
	setter_identifier = 'now',
	description = 'Seconds past from 1970',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_datetime.cgi',
	values = {},
	identifiers = {},
)
NTP_ENABLE = SystemParam \
(
	identifier = 'ntp_enable',
	getter_identifier = 'ntp_enable',
	setter_identifier = 'ntp_enable',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_datetime.cgi',
	values = {0: 'ban ntp calibration', 1: 'allow ntp calibration'},
	identifiers = {},
)
NTP_SVR = SystemParam \
(
	identifier = 'ntp_svr',
	getter_identifier = 'ntp_svr',
	setter_identifier = 'ntp_svr',
	description = 'NTP server',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_datetime.cgi',
	values = {},
	identifiers = {},
)
ONVIFENABLE = SystemParam \
(
	identifier = 'onvifenable',
	getter_identifier = 'onvifenable',
	setter_identifier = 'onvifenable',
	description = 'where to enable ONVIF',
	constant = False,
	constant_assumed = True,
	getter = 'get_onvif.cgi',
	setter = 'set_onvif.cgi',
	values = {0: 'turn off ONVIF', 1: 'turn on ONVIF'},
	identifiers = {},
)
OSDENABLE = SystemParam \
(
	identifier = 'osdenable',
	getter_identifier = 'osdenable',
	setter_identifier = 'osdenable',
	description = 'indicate whether OSD is open',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'disableOSD', 1: 'enable OSD'},
	identifiers = \
	{
		'get_camera_params.cgi': 'OSDEnable',
                'get_status.cgi': 'osdenable',
                'set_misc.cgi': 'osdenable'},
)
PNPPORT = SystemParam \
(
	identifier = 'pnpport',
	getter_identifier = 'pnpport',
	setter_identifier = 'pnpport',
	description = 'P2P server port',
	constant = False,
	constant_assumed = True,
	getter = 'get_pnp_server.cgi',
	setter = 'set_pnp_server.cgi',
	values = {},
	identifiers = {},
)
PNPPWD = SystemParam \
(
	identifier = 'pnppwd',
	getter_identifier = 'pnppwd',
	setter_identifier = 'pnppwd',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_pnp_server.cgi',
	setter = 'set_pnp_server.cgi',
	values = {},
	identifiers = {},
)
PNPSERVER = SystemParam \
(
	identifier = 'pnpserver',
	getter_identifier = 'pnpserver',
	setter_identifier = 'pnpserver',
	description = 'P2P server string',
	constant = False,
	constant_assumed = True,
	getter = 'get_pnp_server.cgi',
	setter = 'set_pnp_server.cgi',
	values = {},
	identifiers = {},
)
PNPUSER = SystemParam \
(
	identifier = 'pnpuser',
	getter_identifier = 'pnpuser',
	setter_identifier = 'pnpuser',
	description = '(unused)',
	constant = False,
	constant_assumed = True,
	getter = 'get_pnp_server.cgi',
	setter = 'set_pnp_server.cgi',
	values = {},
	identifiers = {},
)
PORT = SystemParam \
(
	identifier = 'port',
	getter_identifier = 'port',
	setter_identifier = 'port',
	description = 'Camera HTTP port',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_network.cgi',
	values = {},
	identifiers = {},
)
PPPOE_ENABLE = SystemParam \
(
	identifier = 'pppoe_enable',
	getter_identifier = 'pppoe_enable',
	setter_identifier = 'enable',
	description = '',
	constant = True,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_pppoe.cgi',
	values = {0: 'disablepppoe', 1: 'enable'},
	identifiers = {},
)
PPPOE_PWD = SystemParam \
(
	identifier = 'pppoe_pwd',
	getter_identifier = 'pppoe_pwd',
	setter_identifier = 'pwd',
	description = 'pppoe dial-up password',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_pppoe.cgi',
	values = {},
	identifiers = {},
)
PPPOE_USER = SystemParam \
(
	identifier = 'pppoe_user',
	getter_identifier = 'pppoe_user',
	setter_identifier = 'user',
	description = 'pppoe dial-up user',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_pppoe.cgi',
	values = {},
	identifiers = {},
)
PRESET_ONSTART = SystemParam \
(
	identifier = 'preset_onstart',
	getter_identifier = 'preset_onstart',
	setter_identifier = 'preset_onstart',
	description = ('means preset position called when device start. 1-16 call corresponding '
 'preset position; set related preset position when start up, if no setting, '
 'might lead to position inaccuracy.'),
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'reboot centered'},
	identifiers = {},
)
PTRUNTIMES = SystemParam \
(
	identifier = 'ptruntimes',
	getter_identifier = 'ptruntimes',
	setter_identifier = 'ptz_run_times',
	description = 'cruising loop. 1-10 –> corresponding cruise loops',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'unlimited'},
	identifiers = \
	{
		'get_misc.cgi': 'ptruntimes',
		'set_misc.cgi': 'ptz_run_times',
	},
)
PTZSPEED = SystemParam \
(
	identifier = 'ptzspeed',
	getter_identifier = 'ptzspeed',
	setter_identifier = 'ptzspeed',
	description = 'Pan Tile speed in aging mode',
	constant = False,
	constant_assumed = True,
	getter = 'get_aging.cgi',
	setter = 'set_aging.cgi',
	values = {},
	identifiers = {},
)
PTZ_CENTER_ONSTART = SystemParam \
(
	identifier = 'ptz_center_onstart',
	getter_identifier = 'ptz_center_onstart',
	setter_identifier = 'ptz_center_onstart',
	description = 'means auto centered after restart',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'didn’t auto centered', 1: 'auto centered'},
	identifiers = {},
)
PTZ_DISPPRESET = SystemParam \
(
	identifier = 'ptz_disppreset',
	getter_identifier = 'ptz_disppreset',
	setter_identifier = 'ptz_disppreset',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {0: 'enable PT function', 1: 'disable PT function'},
	identifiers = {},
)
PTZ_PATROL_DOWN_RATE = SystemParam \
(
	identifier = 'ptz_patrol_down_rate',
	getter_identifier = 'ptz_patrol_down_rate',
	setter_identifier = 'ptz_patrol_down_rate',
	description = 'means move down speed. Note：Pan tile speed from 0 to 10,11 level',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_PATROL_LEFT_RATE = SystemParam \
(
	identifier = 'ptz_patrol_left_rate',
	getter_identifier = 'ptz_patrol_left_rate',
	setter_identifier = 'ptz_patrol_left_rate',
	description = 'means move left speed. Note：Pan tile speed from 0 to 10,11 level',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_PATROL_RATE = SystemParam \
(
	identifier = 'ptz_patrol_rate',
	getter_identifier = 'ptz_patrol_rate',
	setter_identifier = 'ptz_patrol_rate',
	description = 'Means the entire speed. Note: Pan tile speed from 0 to 10,11 level',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = \
	{
		'get_misc.cgi': 'ptz_patrol_rate',
		'set_misc.cgi': 'ptz_patrol_rate',
		'get_camera_params.cgi': 'speed',
	},
)
PTZ_PATROL_RIGHT_RATE = SystemParam \
(
	identifier = 'ptz_patrol_right_rate',
	getter_identifier = 'ptz_patrol_right_rate',
	setter_identifier = 'ptz_patrol_right_rate',
	description = 'means move right speed. Note：Pan tile speed from 0 to 10,11 level',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_PATROL_UP_RATE = SystemParam \
(
	identifier = 'ptz_patrol_up_rate',
	getter_identifier = 'ptz_patrol_up_rate',
	setter_identifier = 'ptz_patrol_up_rate',
	description = 'means the move up speed. Note：Pan tile speed from 0 to 10,11 level',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_SOFT_LIMIT_MAX_LEVEL = SystemParam \
(
	identifier = 'ptz_soft_limit_max_level',
	getter_identifier = 'ptz_soft_limit_max_level',
	setter_identifier = 'ptz_soft_limit_max_level',
	description = 'soft limit max horizontal step',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_SOFT_LIMIT_MAX_VERT = SystemParam \
(
	identifier = 'ptz_soft_limit_max_vert',
	getter_identifier = 'ptz_soft_limit_max_vert',
	setter_identifier = 'ptz_soft_limit_max_vert',
	description = 'soft limit max vertical step.',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_SOFT_LIMIT_STOP_PERCENT_LEVEL = SystemParam \
(
	identifier = 'ptz_soft_limit_stop_percent_level',
	getter_identifier = 'ptz_soft_limit_stop_percent_level',
	setter_identifier = 'ptz_soft_limit_stop_percent_level',
	description = 'soft limit stop level percentage',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
PTZ_SOFT_LIMIT_STOP_PERCENT_VERT = SystemParam \
(
	identifier = 'ptz_soft_limit_stop_percent_vert',
	getter_identifier = 'ptz_soft_limit_stop_percent_vert',
	setter_identifier = 'ptz_soft_limit_stop_percent_vert',
	description = 'soft limit vertical stop percentage',
	constant = False,
	constant_assumed = True,
	getter = 'get_misc.cgi',
	setter = 'set_misc.cgi',
	values = {},
	identifiers = {},
)
RECORD_AUDIO = SystemParam \
(
	identifier = 'record_audio',
	getter_identifier = 'record_audio',
	setter_identifier = 'record_audio',
	description = 'record audio',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = {},
	identifiers = {},
)
RECORD_COVER_ENABLE = SystemParam \
(
	identifier = 'record_cover_enable',
	getter_identifier = 'record_cover_enable',
	setter_identifier = 'record_cover',
	description = 'video overwrite',
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = {},
	identifiers = \
	{
		'get_record.cgi': 'record_cover_enable',
		'set_recordsch.cgi': 'record_cover',
	},
)
RECORD_SCHEDULE_FRI_0 = SystemParam \
(
	identifier = 'record_schedule_fri_0',
	getter_identifier = 'record_schedule_fri_0',
	setter_identifier = 'schedule_fri_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_FRI_1 = SystemParam \
(
	identifier = 'record_schedule_fri_1',
	getter_identifier = 'record_schedule_fri_1',
	setter_identifier = 'schedule_fri_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_FRI_2 = SystemParam \
(
	identifier = 'record_schedule_fri_2',
	getter_identifier = 'record_schedule_fri_2',
	setter_identifier = 'schedule_fri_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_MON_0 = SystemParam \
(
	identifier = 'record_schedule_mon_0',
	getter_identifier = 'record_schedule_mon_0',
	setter_identifier = 'schedule_mon_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_MON_1 = SystemParam \
(
	identifier = 'record_schedule_mon_1',
	getter_identifier = 'record_schedule_mon_1',
	setter_identifier = 'schedule_mon_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_MON_2 = SystemParam \
(
	identifier = 'record_schedule_mon_2',
	getter_identifier = 'record_schedule_mon_2',
	setter_identifier = 'schedule_mon_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SAT_0 = SystemParam \
(
	identifier = 'record_schedule_sat_0',
	getter_identifier = 'record_schedule_sat_0',
	setter_identifier = 'schedule_sat_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SAT_1 = SystemParam \
(
	identifier = 'record_schedule_sat_1',
	getter_identifier = 'record_schedule_sat_1',
	setter_identifier = 'schedule_sat_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SAT_2 = SystemParam \
(
	identifier = 'record_schedule_sat_2',
	getter_identifier = 'record_schedule_sat_2',
	setter_identifier = 'schedule_sat_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SUN_0 = SystemParam \
(
	identifier = 'record_schedule_sun_0',
	getter_identifier = 'record_schedule_sun_0',
	setter_identifier = 'schedule_sun_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SUN_1 = SystemParam \
(
	identifier = 'record_schedule_sun_1',
	getter_identifier = 'record_schedule_sun_1',
	setter_identifier = 'schedule_sun_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_SUN_2 = SystemParam \
(
	identifier = 'record_schedule_sun_2',
	getter_identifier = 'record_schedule_sun_2',
	setter_identifier = 'schedule_sun_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_THU_0 = SystemParam \
(
	identifier = 'record_schedule_thu_0',
	getter_identifier = 'record_schedule_thu_0',
	setter_identifier = 'schedule_thu_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_THU_1 = SystemParam \
(
	identifier = 'record_schedule_thu_1',
	getter_identifier = 'record_schedule_thu_1',
	setter_identifier = 'schedule_thu_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_THU_2 = SystemParam \
(
	identifier = 'record_schedule_thu_2',
	getter_identifier = 'record_schedule_thu_2',
	setter_identifier = 'schedule_thu_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_TUE_0 = SystemParam \
(
	identifier = 'record_schedule_tue_0',
	getter_identifier = 'record_schedule_tue_0',
	setter_identifier = 'schedule_tue_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_TUE_1 = SystemParam \
(
	identifier = 'record_schedule_tue_1',
	getter_identifier = 'record_schedule_tue_1',
	setter_identifier = 'schedule_tue_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_TUE_2 = SystemParam \
(
	identifier = 'record_schedule_tue_2',
	getter_identifier = 'record_schedule_tue_2',
	setter_identifier = 'schedule_tue_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_WED_0 = SystemParam \
(
	identifier = 'record_schedule_wed_0',
	getter_identifier = 'record_schedule_wed_0',
	setter_identifier = 'schedule_wed_0',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_WED_1 = SystemParam \
(
	identifier = 'record_schedule_wed_1',
	getter_identifier = 'record_schedule_wed_1',
	setter_identifier = 'schedule_wed_1',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_SCHEDULE_WED_2 = SystemParam \
(
	identifier = 'record_schedule_wed_2',
	getter_identifier = 'record_schedule_wed_2',
	setter_identifier = 'schedule_wed_2',
	description = ('Week deployment plan, 24hours per day, 15 mins as a time period, one hour '
 'divide into four periods. bit0-95: other value indicate the recording time. '
 'indicate the recording planin this time period'),
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = \
	{
		-1: 'record 8 hours',
                0: 'Don’t record in this period',
                1: 'record in this period'},
	identifiers = {},
)
RECORD_TIME_ENABLE = SystemParam \
(
	identifier = 'record_time_enable',
	getter_identifier = 'record_time_enable',
	#setter_identifier = 'record_time',
	description = 'scheduled recording plan',
	constant = False,
	constant_assumed = True,
	getter = 'get_record.cgi',
	setter = 'set_recordsch.cgi',
	values = {},
	identifiers = \
	{
		'get_record.cgi': 'record_time_enable',
		#'set_recordsch.cgi': 'record_time',
		'set_recordsch.cgi': 'time_schedule_enable',
	}
)
"""
RTSPENABLE = SystemParam \
(
	identifier = 'rtspenable',
	getter_identifier = 'rtspenable',
	setter_identifier = 'rtspenable',
	description = 'whether to enable RTSP',
	constant = False,
	constant_assumed = True,
	getter = 'get_rtsp.cgi',
	setter = 'set_rtsp.cgi',
	values = {0: 'disableRTSP service', 1: 'enable RTSP service'},
	identifiers = {},
)
"""
RTSPPORT = SystemParam \
(
	identifier = 'rtspport',
	getter_identifier = 'rtspport',
	setter_identifier = 'rtspport',
	description = 'RTSP port number',
	constant = False,
	constant_assumed = True,
	getter = 'get_rtsp.cgi',
	setter = 'set_rtsp.cgi',
	values = {},
	identifiers = {},
)
RTSPPWD = SystemParam \
(
	identifier = 'rtsppwd',
	getter_identifier = 'rtsppwd',
	setter_identifier = 'rtsppwd',
	description = 'access RTSP password (reserve)',
	constant = False,
	constant_assumed = True,
	getter = 'get_rtsp.cgi',
	setter = 'set_rtsp.cgi',
	values = {},
	identifiers = \
	{
		'get_params.cgi': 'rtsp_pwd',
                'get_rtsp.cgi': 'rtsppwd',
                'set_rtsp.cgi': 'rtsppwd'},
)
RTSPUSER = SystemParam \
(
	identifier = 'rtspuser',
	getter_identifier = 'rtspuser',
	setter_identifier = 'rtspuser',
	description = 'access RTSP account (reserve)',
	constant = False,
	constant_assumed = True,
	getter = 'get_rtsp.cgi',
	setter = 'set_rtsp.cgi',
	values = {},
	identifiers = \
	{
		'get_params.cgi': 'rtsp_user',
                'get_rtsp.cgi': 'rtspuser',
                'set_rtsp.cgi': 'rtspuser'},
)
RTSP_AUTH_ENABLE = SystemParam \
(
	identifier = 'rtsp_auth_enable',
	getter_identifier = 'rtsp_auth_enable',
	setter_identifier = 'rtspenable',
	description = 'Whether to enable RTSP. RTSP stream certificate. RTSP status',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_rtsp.cgi',
	values = {0: 'disableRTSP service', 1: 'enable RTSP service'},
	identifiers = \
	{
		'get_params.cgi': 'rtsp_auth_enable',
		'set_rtsp.cgi': 'rtspenable',
		'get_rtsp.cgi': 'rtspenable',
	},
)
SUB_ENC_BITRATE = SystemParam \
(
	identifier = 'sub_enc_bitrate',
	getter_identifier = 'sub_enc_bitrate',
	setter_identifier = 'sub_enc_bitrate',
	description = 'secondary stream rate',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
SUB_ENC_FRAMERATE = SystemParam \
(
	identifier = 'sub_enc_framerate',
	getter_identifier = 'sub_enc_framerate',
	setter_identifier = 'sub_enc_framerate',
	description = 'secondary stream frame rate',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
SUB_ENC_KEYFRAME = SystemParam \
(
	identifier = 'sub_enc_keyframe',
	getter_identifier = 'sub_enc_keyframe',
	setter_identifier = 'sub_enc_keyframe',
	description = 'secondary stream key frame',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
SUB_ENC_QUANT = SystemParam \
(
	identifier = 'sub_enc_quant',
	getter_identifier = 'sub_enc_quant',
	setter_identifier = 'sub_enc_quant',
	description = 'secondary stream picture quality',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {},
	identifiers = {},
)
SUB_ENC_RATEMODE = SystemParam \
(
	identifier = 'sub_enc_ratemode',
	getter_identifier = 'sub_enc_ratemode',
	setter_identifier = 'sub_enc_ratemode',
	description = 'secondary stream stream mode',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {0: 'means CBR', 1: 'means VBR'},
	identifiers = {},
)
SUB_ENC_SIZE = SystemParam \
(
	identifier = 'sub_enc_size',
	getter_identifier = 'sub_enc_size',
	setter_identifier = 'sub_enc_size',
	description = 'consistent with resolutionsub',
	constant = False,
	constant_assumed = True,
	getter = 'get_camera_params.cgi',
	setter = 'set_media.cgi',
	values = {0: '1/2', 1: '1/4'},
	identifiers = {},
)
SYSVER = SystemParam \
(
	identifier = 'sysver',
	getter_identifier = 'sysver',
	setter_identifier = 'sysver',
	description = 'First field of the version number',
	constant = False,
	constant_assumed = True,
	getter = 'get_pnp_server.cgi',
	setter = 'set_pnp_server.cgi',
	values = {},
	identifiers = {},
)
TIME_ZONE = SystemParam \
(
	identifier = 'time_zone',
	getter_identifier = 'tz',
	setter_identifier = 'tz',
	description = 'Device current time zone settings and deviation seconds with standard GMT',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_datetime.cgi',
	values = {},
	identifiers = {},
)
TZ = SystemParam \
(
	identifier = 'tz',
	getter_identifier = 'tz',
	setter_identifier = 'tz',
	description = 'Device current time zone settings and deviation seconds with standard GMT',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_datetime.cgi',
	values = {},
	identifiers = {},
)
UPNP_ENABLE = SystemParam \
(
	identifier = 'upnp_enable',
	getter_identifier = 'upnp_enable',
	setter_identifier = 'enable',
	description = 'UPNP mapping function',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_upnp.cgi',
	values = {0: 'disable upnp mapping', 1: 'allow upnp mapping'},
	identifiers = {},
)
USER1_NAME = SystemParam \
(
	identifier = 'user1_name',
	getter_identifier = 'user1_name',
	setter_identifier = 'user1',
	description = 'User name<visitor>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
USER1_PWD = SystemParam \
(
	identifier = 'user1_pwd',
	getter_identifier = 'user1_pwd',
	setter_identifier = 'pwd1',
	description = 'password<visitor>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
USER2_NAME = SystemParam \
(
	identifier = 'user2_name',
	getter_identifier = 'user2_name',
	setter_identifier = 'user2',
	description = 'User name<operator>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
USER2_PWD = SystemParam \
(
	identifier = 'user2_pwd',
	getter_identifier = 'user2_pwd',
	setter_identifier = 'pwd2',
	description = 'password<operator>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
USER3_NAME = SystemParam \
(
	identifier = 'user3_name',
	getter_identifier = 'user3_name',
	setter_identifier = 'user3',
	description = 'User name<manager>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
USER3_PWD = SystemParam \
(
	identifier = 'user3_pwd',
	getter_identifier = 'user3_pwd',
	setter_identifier = 'pwd3',
	description = 'password<manager>',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_users.cgi',
	values = {},
	identifiers = {},
)
WIFIMAC = SystemParam \
(
	identifier = 'wifimac',
	getter_identifier = 'wifimac',
	setter_identifier = 'wifimac',
	description = 'wireless MAC address',
	constant = False,
	constant_assumed = True,
	getter = 'get_status.cgi',
	setter = 'set_factory_param.cgi',
	values = {},
	identifiers = {},
)
WIFI_AUTHTYPE = SystemParam \
(
	identifier = 'wifi_authtype',
	getter_identifier = 'wifi_authtype',
	setter_identifier = 'authtype',
	description = '',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = \
	{
		0: 'disable certificate',
                1: 'wep',
                2: 'wpa-psk/aes',
                3: 'wpa-psk/tkip',
                4: 'wpa2-psk/aes',
                5: 'wpa2-psk/tkip'},
	identifiers = {},
)
WIFI_CHANNEL = SystemParam \
(
	identifier = 'wifi_channel',
	getter_identifier = 'wifi_channel',
	setter_identifier = 'channel',
	description = 'wireless channel number',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_DEFKEY = SystemParam \
(
	identifier = 'wifi_defkey',
	getter_identifier = 'wifi_defkey',
	setter_identifier = 'defkey',
	description = 'WEP key choose(below 1-4 key)',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_ENABLE = SystemParam \
(
	identifier = 'wifi_enable',
	getter_identifier = 'wifi_enable',
	setter_identifier = 'enable',
	description = 'Enable/disable wifi function',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: 'disable wifi function', 1: 'Enable wifi function'},
	identifiers = {},
)
WIFI_ENCRYPT = SystemParam \
(
	identifier = 'wifi_encrypt',
	getter_identifier = 'wifi_encrypt',
	setter_identifier = 'encrypt',
	description = 'wep verify mode',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: 'open', 1: 'share'},
	identifiers = {},
)
WIFI_KEY1 = SystemParam \
(
	identifier = 'wifi_key1',
	getter_identifier = 'wifi_key1',
	setter_identifier = 'key1',
	description = 'WEP key1',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_KEY1_BITS = SystemParam \
(
	identifier = 'wifi_key1_bits',
	getter_identifier = 'wifi_key1_bits',
	setter_identifier = 'key1_bits',
	description = 'WEP key 1 length',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: '64 bits', 1: '128 bits'},
	identifiers = {},
)
WIFI_KEY2 = SystemParam \
(
	identifier = 'wifi_key2',
	getter_identifier = 'wifi_key2',
	setter_identifier = 'key2',
	description = 'WEP key2',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_KEY2_BITS = SystemParam \
(
	identifier = 'wifi_key2_bits',
	getter_identifier = 'wifi_key2_bits',
	setter_identifier = 'key2_bits',
	description = 'WEP key 2 length',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: '64 bits', 1: '128 bits'},
	identifiers = {},
)
WIFI_KEY3 = SystemParam \
(
	identifier = 'wifi_key3',
	getter_identifier = 'wifi_key3',
	setter_identifier = 'key3',
	description = 'WEP key3',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_KEY3_BITS = SystemParam \
(
	identifier = 'wifi_key3_bits',
	getter_identifier = 'wifi_key3_bits',
	setter_identifier = 'key3_bits',
	description = 'WEP key 3 length',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: '64 bits', 1: '128 bits'},
	identifiers = {},
)
WIFI_KEY4 = SystemParam \
(
	identifier = 'wifi_key4',
	getter_identifier = 'wifi_key4',
	setter_identifier = 'key4',
	description = 'WEP key4',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_KEY4_BITS = SystemParam \
(
	identifier = 'wifi_key4_bits',
	getter_identifier = 'wifi_key4_bits',
	setter_identifier = 'key4_bits',
	description = 'WEP key 4 length',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: '64 bits', 1: '128 bits'},
	identifiers = {},
)
WIFI_KEYFORMAT = SystemParam \
(
	identifier = 'wifi_keyformat',
	getter_identifier = 'wifi_keyformat',
	setter_identifier = 'keyformat',
	description = 'WEP key format',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: '16 hexadecimal numbers', 1: 'ascii character'},
	identifiers = {},
)
WIFI_MODE = SystemParam \
(
	identifier = 'wifi_mode',
	getter_identifier = 'wifi_mode',
	setter_identifier = 'mode',
	description = 'Wifi mode',
	constant = False,
	constant_assumed = False,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {0: 'Infra mode', 1: 'Ad hoc mode'},
	identifiers = {},
)
WIFI_SSID = SystemParam \
(
	identifier = 'wifi_ssid',
	getter_identifier = 'wifi_ssid',
	setter_identifier = 'ssid',
	description = 'WIFI SSID',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
WIFI_WPA_PSK = SystemParam \
(
	identifier = 'wifi_wpa_psk',
	getter_identifier = 'wifi_wpa_psk',
	setter_identifier = 'wpa_psk',
	description = 'wpa psk key',
	constant = False,
	constant_assumed = True,
	getter = 'get_params.cgi',
	setter = 'set_wifi.cgi',
	values = {},
	identifiers = {},
)
