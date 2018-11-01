"""
Imports:
    .firmware_files
    .firmware_files.*

Constants defined here:
    FILES - List of all files
    file_libs - Tuple of file libraries
"""

from . import firmware_files
from .firmware_files import *

file_libs = \
(
    firmware_files,
)

FILES = []

for file_lib in file_libs:
    for attribute in dir(file_lib):
        if attribute.startswith('_') or not attribute.isupper():
            continue

        FILES.append(getattr(file_lib, attribute))
