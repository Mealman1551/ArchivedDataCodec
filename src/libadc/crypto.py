# ADC Archiver - Cryptography Module
# This code is licensed under the GNU General Public License v3.0.

import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from .constants import PBKDF2_ITERATIONS


def derive_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Derive a Fernet-compatible encryption key from a password using PBKDF2.
    
    Args:
        password: The password string to derive from
        salt: The salt bytes for the KDF
        
    Returns:
        A base64-encoded 32-byte key suitable for Fernet encryption
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
