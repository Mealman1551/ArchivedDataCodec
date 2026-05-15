# ADC Archiver - Package
# (c) 2026 Mealman1551


from libadc.constants import APP_NAME, VERSION, COPYRIGHT
from libadc.archive import create_adc_archive, extract_adc_archive

__version__ = VERSION
__author__ = "Mealman1551"
__copyright__ = COPYRIGHT

__all__ = [
    "create_adc_archive",
    "extract_adc_archive",
    "APP_NAME",
    "VERSION",
    "COPYRIGHT",
]
