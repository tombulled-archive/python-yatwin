"""
Library which contains Constants

These are variable constants, in that they can be changed by the user
... during program execution, but are intended to be constant throughout
... program execution

Contains 'constants' in upper-case, using underscores (_) to seperate words

These constants are used by *_control.cgi methods
"""

PTZ_UP = 0
PTZ_UP_STOP = 1
PTZ_DOWN = 2
PTZ_DOWN_STOP = 3
PTZ_LEFT = 4
PTZ_LEFT_STOP = 5
PTZ_RIGHT = 6
PTZ_RIGHT_STOP = 7
PTZ_LEFT_UP = 90
PTZ_RIGHT_UP = 91
PTZ_LEFT_DOWN = 92
PTZ_RIGHT_DOWN = 93
PTZ_STOP = 1

CENTER = 25
VPATROL = 26
VPATROL_STOP = 27
HPATROL = 28
HPATROL_STOP = 29

IO_ON = 94
IO_OFF = 95

PARAM_VMIRROR = 5
VAL_VMIRROR_ON = 2
VAL_VMIRROR_OFF = 0

PARAM_HMIRROR = 5
VAL_HMIRROR_ON = 1
VAL_HMIRROR_OFF = 0

PARAM_IR = 14
VAL_IR_ON = 1
VAL_IR_OFF = 0

VAL_VGA640X360 = 0
VAL_QVGA320X180 = 1

PARAM_BRIGHTNESS = 1
PARAM_CONTRAST = 2
PARAM_SATURATION = 8
PARAM_HUE = 9
PARAM_RESOLUTION = 15
PARAM_FRAMERATE = 12
