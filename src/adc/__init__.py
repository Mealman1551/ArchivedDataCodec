# ADC Archiver 1.4.4 LTS Package
# This code is based on Aurora 2025.09.1 code and is licensed under the GNU General Public License v3.0.

"""
ADC Archiver 1.4.4 "Grand Canyon" LTS - A multi-format archive tool with encryption support.

This package provides functionality for creating and extracting archives
in ADC (custom) and ZIP formats, with optional password-based encryption.

ADC 1.4.4 is considered stable and production ready.
ADC 1.4.4 is LTS (Long Term Support) and will receive updates for a long time.

Modules:
    - constants: Color codes and configuration values
    - ascii_art: ASCII art banner for Linux/POSIX systems
    - crypto: Cryptography functions for password-based encryption
    - compression: Compression/decompression using zlib
    - archive: Archive creation and extraction functions
    - ui: User interface file dialog functions
    - updater: Update checking and notification system
    - __main__: Command-line interface entry point

License:
    GNU General Public License v3.0
    Based on Aurora 2025.09.1 code
"""

from .constants import (
    APP_NAME,
    VERSION,
    VERSION_CODENAME,
    COPYRIGHT,
    LICENSE,
    GITHUB_URL,
    EMAIL,
)
from .archive import create_adc_archive, extract_adc_archive
from .ascii_art import print_banner
from .updater import check_and_show_update

__version__ = VERSION
__version_codename__ = VERSION_CODENAME
__author__ = "Mealman1551"
__email__ = EMAIL
__copyright__ = COPYRIGHT
__license__ = LICENSE

__all__ = [
    "create_adc_archive",
    "extract_adc_archive",
    "print_banner",
    "check_and_show_update",
    "APP_NAME",
    "VERSION",
    "VERSION_CODENAME",
    "COPYRIGHT",
    "LICENSE",
]
