from logics.base import EncryptionLogic
import itertools

class XorLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "xor"

    @property
    def description(self) -> str:
        return "Simple XOR encryption (WEAK - For testing only)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return self._xor(data, password)

    def decrypt(self, data: bytes, password: str) -> bytes:
        return self._xor(data, password)

    def _xor(self, data: bytes, password: str) -> bytes:
        if not password:
            raise ValueError("Password cannot be empty")
        
        # Cycle through password bytes
        password_bytes = password.encode('utf-8')
        return bytes(a ^ b for a, b in zip(data, itertools.cycle(password_bytes)))
