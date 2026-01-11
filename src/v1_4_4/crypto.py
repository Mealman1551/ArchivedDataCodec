# ADC Archiver 1.4.4 LTS - Cryptography Module
# This code is licensed under the GNU General Public License v3.0.

"""
Cryptography functions for password-based encryption/decryption.
Uses PBKDF2 for key derivation and Fernet for symmetric encryption.
"""

import base64
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from .constants import PBKDF2_ITERATIONS


def derive_key_from_password(password: str, salt: bytes) -> bytes:
    """
    Derives a cryptographic key from a password using PBKDF2.
    
    Args:
        password: The password string to derive key from
        salt: Random salt bytes for key derivation
        
    Returns:
        Base64 encoded key suitable for Fernet encryption
    """
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))
