from logics.base import EncryptionLogic
import hashlib
import hmac
import os


class RC4Logic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "rc4"

    @property
    def description(self) -> str:
        return "RC4 stream cipher"

    def _rc4(self, data: bytes, key: bytes) -> bytes:
        S = list(range(256))
        j = 0
        for i in range(256):
            j = (j + S[i] + key[i % len(key)]) % 256
            S[i], S[j] = S[j], S[i]
        
        i = j = 0
        result = []
        for byte in data:
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            result.append(byte ^ S[(S[i] + S[j]) % 256])
        return bytes(result)

    def encrypt(self, data: bytes, password: str) -> bytes:
        return self._rc4(data, password.encode('utf-8'))

    def decrypt(self, data: bytes, password: str) -> bytes:
        return self._rc4(data, password.encode('utf-8'))


class HashFunctionLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "hash"

    @property
    def description(self) -> str:
        return "SHA-256 hash (one-way)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return hashlib.sha256(data).hexdigest().encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        raise ValueError("Hash functions are one-way and cannot be decrypted")


class HMACLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "hmac"

    @property
    def description(self) -> str:
        return "HMAC-SHA256 (keyed hash)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        mac = hmac.new(password.encode('utf-8'), data, hashlib.sha256)
        return mac.hexdigest().encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        raise ValueError("HMAC is a keyed hash and cannot be decrypted")


class BlowfishLogic(EncryptionLogic):
    """Simple Blowfish-like implementation for demonstration."""
    
    @property
    def name(self) -> str:
        return "blowfish"

    @property
    def description(self) -> str:
        return "Blowfish-style block cipher (simplified)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        # Use cryptography library for real Blowfish if available
        try:
            from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
            from cryptography.hazmat.backends import default_backend
            
            # Pad data to 8-byte blocks
            pad_len = 8 - (len(data) % 8)
            padded = data + bytes([pad_len] * pad_len)
            
            # Derive key (Blowfish accepts 4-56 bytes)
            key = hashlib.sha256(password.encode()).digest()[:16]
            iv = os.urandom(8)
            
            cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded) + encryptor.finalize()
            
            return iv + ciphertext
        except ImportError:
            raise ValueError("Blowfish requires 'cryptography' library")

    def decrypt(self, data: bytes, password: str) -> bytes:
        try:
            from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
            from cryptography.hazmat.backends import default_backend
            
            if len(data) < 8:
                raise ValueError("Invalid data")
            
            iv = data[:8]
            ciphertext = data[8:]
            
            key = hashlib.sha256(password.encode()).digest()[:16]
            
            cipher = Cipher(algorithms.Blowfish(key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded = decryptor.update(ciphertext) + decryptor.finalize()
            
            # Remove padding
            pad_len = padded[-1]
            return padded[:-pad_len]
        except ImportError:
            raise ValueError("Blowfish requires 'cryptography' library")
