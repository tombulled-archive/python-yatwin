from .. import constants

"""
Imports:
    ..constants

Contains:
    scale_ptz_patrol_rate
    scale_brightness
    scale_contrast
    scale_hue
    generate_preset
"""

def scale_ptz_patrol_rate(rate):
    """
    Scale the PTZ patrol rate
    """

    return rate * constants.SCALAR_PTZ_PATROL_RATE

def scale_brightness(brightness):
    """
    Scale the brightness
    """

    return brightness * constants.SCALAR_BRIGHTNESS

def scale_contrast(contrast):
    """
    Scale the contrast
    """

    return contrast * constants.SCALAR_CONTRAST

def scale_hue(hue):
    """
    Scale the hue
    """

    return hue * constants.SCALAR_HUE

def generate_preset(preset, set=True):
    """
    Generate the preset value based on the preset index
    ... and whether it's being set/retrieved
    """

    return 30 + 2 * (preset - 1) + int(not bool(set))
