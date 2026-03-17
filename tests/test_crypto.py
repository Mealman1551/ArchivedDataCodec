from adc.crypto import derive_key_from_password
import base64

def test_derive_key_from_password():
    password = "passwd"
    salt = b"1234567890123456"
    key = derive_key_from_password(password, salt)
    
    assert isinstance(key, bytes)
    decoded = base64.urlsafe_b64decode(key)
    assert len(decoded) == 32