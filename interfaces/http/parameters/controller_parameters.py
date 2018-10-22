from .parameter_types.ControllerParam import ControllerParam

"""
Library containing controller parameters.

These parameters are only retrieved via these identifiers,
... however are able to be edited by a *_controller method

Imports:
	.parameter_types.ControllerParam.ControllerParam
"""

VBRIGHT = ControllerParam \
(
	identifier = 'vbright',
	getter_identifier = 'vbright',
	setter_identifier = None,
	description = 'Means the brightness (value range: 0-255)',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'vbright',
    },
)
VCONTRAST = ControllerParam \
(
	identifier = 'vcontrast',
	getter_identifier = 'vcontrast',
	setter_identifier = None,
	description = 'Means the contrast (value range: 0-255)',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'vcontrast',
    },
)
VHUE = ControllerParam \
(
	identifier = 'vhue',
	getter_identifier = 'vhue',
	setter_identifier = None,
	description = 'Means the chrome (hue) (value range: 0-255)',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'vhue',
    },
)
VSATURATION = ControllerParam \
(
	identifier = 'vsaturation',
	getter_identifier = 'vsaturation',
	setter_identifier = None,
	description = 'Means the saturation (value range: 0-255)',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'vsaturation',
    },
)
FLIP = ControllerParam \
(
	identifier = 'flip',
	getter_identifier = 'flip',
	setter_identifier = None,
	description = 'Means flip and mirror image',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = \
    {
        0: 'normal',
        1: 'mirror',
        2: 'flip',
        3: 'mirror and flip',
    },
	identifiers = \
    {
        'get_camera_params.cgi': 'flip',
    },
)
MODE = ControllerParam \
(
	identifier = 'mode',
	getter_identifier = 'mode',
	setter_identifier = None,
	description = 'Means camera operating voltage',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = \
    {
        0: '50hz',
        1: '60hz',
    },
	identifiers = \
    {
        'get_camera_params.cgi': 'mode',
    },
)
OUTVOLUME = ControllerParam \
(
	identifier = 'outvolume',
	getter_identifier = 'outvolume',
	setter_identifier = None,
	description = 'Means output (talk) volume',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'outvolume',
    },
)
INVOLUME = ControllerParam \
(
	identifier = 'involume',
	getter_identifier = 'involume',
	setter_identifier = None,
	description = 'Mean input (listen) volume',
	constant = False,
	constant_assumed = False,
	getter = 'get_camera_params.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_camera_params.cgi': 'involume',
    },
)
SUB_SUB_ENC_BITRATE = ControllerParam \
(
	identifier = 'sub_sub_enc_bitrate',
	getter_identifier = 'sub_sub_enc_bitrate',
	setter_identifier = None,
	description = 'secondary stream bitrate',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_bitrate',
        'get_camera_params.cgi': 'sub_sub_enc_bitrate',
    },
)
SUB_SUB_ENC_FRAMERATE = ControllerParam \
(
	identifier = 'sub_sub_enc_framerate',
	getter_identifier = 'sub_sub_enc_framerate',
	setter_identifier = None,
	description = 'secondary stream framerate',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_framerate',
        'get_camera_params.cgi': 'sub_sub_enc_framerate',
    },
)
SUB_SUB_ENC_KEYFRAME = ControllerParam \
(
	identifier = 'sub_sub_enc_keyframe',
	getter_identifier = 'sub_sub_enc_keyframe',
	setter_identifier = None,
	description = 'secondary stream keyframe',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_keyframe',
        'get_camera_params.cgi': 'sub_sub_enc_keyframe',
    },
)
SUB_SUB_ENC_QUANT = ControllerParam \
(
	identifier = 'sub_sub_enc_quant',
	getter_identifier = 'sub_sub_enc_quant',
	setter_identifier = None,
	description = 'secondary stream quant',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_quant',
        'get_camera_params.cgi': 'sub_sub_enc_quant',
    },
)
SUB_SUB_ENC_RATEMODE = ControllerParam \
(
	identifier = 'sub_sub_enc_ratemode',
	getter_identifier = 'sub_sub_enc_ratemode',
	setter_identifier = None,
	description = 'secondary stream ratemode',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_ratemode',
        'get_camera_params.cgi': 'sub_sub_enc_ratemode',
    },
)
SUB_SUB_ENC_SIZE = ControllerParam \
(
	identifier = 'sub_sub_enc_size',
	getter_identifier = 'sub_sub_enc_size',
	setter_identifier = None,
	description = 'secondary stream size',
	constant = False,
	constant_assumed = False,
	getter = 'get_record.cgi',
	setter = None,
	values = {},
	identifiers = \
    {
        'get_record.cgi': 'sub_sub_enc_size',
        'get_camera_params.cgi': 'sub_sub_enc_size',
    },
)
