from adc.constants import ADC_HEADER, VERSION

def test_constants():
    assert ADC_HEADER == b"ADCARCH\x00"
    assert VERSION == "1.4.4"