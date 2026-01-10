# ADC Archiver 1.4.4 LTS - Constants Module
# This code is based on Aurora 2025.09.1 code and is licensed under the GNU General Public License v3.0.
# You can redistribute it and/or modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

"""
Color constants and configuration values for ADC Archiver 1.4.4 LTS.
"""

RED = "\033[31m"
GREEN = "\033[32m"
PURPLE = "\033[35m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
ORANGE = "\033[38;5;208m"
TEAL = "\033[38;5;37m"
WHITE = "\033[37m"
GRAY = "\033[90m"
LIGHT_BLUE = "\033[94m"
LIGHT_GREEN = "\033[92m"
LIGHT_RED = "\033[91m"
LIGHT_PURPLE = "\033[95m"
LIGHT_CYAN = "\033[96m"
LIGHT_YELLOW = "\033[93m"
LIGHT_ORANGE = "\033[38;5;214m"
LIGHT_GRAY = "\033[90m"
LIGHT_TEAL = "\033[38;5;123m"
LIGHT_MAGENTA = "\033[95m"
BLINK = "\033[5m"
UNDERLINE = "\033[4m"
REVERSE = "\033[7m"
BLACK = "\033[30m"
BOLD = "\033[1m"
ITALIC = "\033[3m"
reset = "\033[0m"

# Application metadata
APP_NAME = "ADC Archiver"
VERSION = "1.4.4"
VERSION_CODENAME = "Grand Canyon"
BYTE_KEY = 8
GITHUB_URL = "https://github.com/Mealman1551/ADC"
WEBPAGE_1 = "https://mealman1551.github.io/adc.html"
WEBPAGE_2 = "https://mealman1551.github.io/ADC"
EMAIL = "nathandubuy4+adc@gmail.com"
COPYRIGHT = "(c) 2026 Mealman1551"
LICENSE = "GNU General Public License v3.0"

# Archive header for encrypted ADC files
ADC_HEADER = b"ADCARCH\x00"

# Cryptography settings
PBKDF2_ITERATIONS = 390000
SALT_SIZE = 16

# Update checking
UPDATE_JSON_URL = "https://gitlab.com/adc-project/update-repository/-/raw/main/lts.json?ref_type=heads"
UPDATE_CHECK_TIMEOUT = 5
