from logics.base import EncryptionLogic
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class AESLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "aes"

    @property
    def description(self) -> str:
        return "AES-256-GCM (Production Grade)"

    def _derive_key(self, password: str, salt: bytes) -> bytes:
        """Derives a 256-bit key from the password using PBKDF2."""
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        return kdf.derive(password.encode('utf-8'))

    def encrypt(self, data: bytes, password: str) -> bytes:
        # Generate a random salt
        salt = os.urandom(16)
        # Derive key
        key = self._derive_key(password, salt)
        # Generate a random nonce for GCM
        nonce = os.urandom(12)
        
        # Encrypt
        aesgcm = AESGCM(key)
        ciphertext = aesgcm.encrypt(nonce, data, None)
        
        # Combine salt + nonce + ciphertext
        # We need salt to derive key for decryption
        # We need nonce for GCM decryption
        return salt + nonce + ciphertext

    def decrypt(self, data: bytes, password: str) -> bytes:
        try:
            if len(data) < 28: # 16 salt + 12 nonce
                raise ValueError("Invalid encrypted data format")
            
            salt = data[:16]
            nonce = data[16:28]
            ciphertext = data[28:]
            
            key = self._derive_key(password, salt)
            
            aesgcm = AESGCM(key)
            return aesgcm.decrypt(nonce, ciphertext, None)
        except Exception as e:
            raise ValueError("Decryption failed. Wrong password or corrupted file.") from e
