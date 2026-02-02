from logics.base import EncryptionLogic

class ReverseLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "reverse"

    @property
    def description(self) -> str:
        return "Reverses the byte sequence"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return data[::-1]

    def decrypt(self, data: bytes, password: str) -> bytes:
        return data[::-1]


class CaseTransformLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "case"

    @property
    def description(self) -> str:
        return "Swaps uppercase and lowercase characters"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return data.swapcase()

    def decrypt(self, data: bytes, password: str) -> bytes:
        return data.swapcase()


class BitwiseXorLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "bitwise"

    @property
    def description(self) -> str:
        return "Bitwise XOR with password (repeating key)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        key = password.encode('utf-8')
        return bytes(b ^ key[i % len(key)] for i, b in enumerate(data))

    def decrypt(self, data: bytes, password: str) -> bytes:
        return self.encrypt(data, password)  # XOR is symmetric


class ReplaceLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "replace"

    @property
    def description(self) -> str:
        return "Replaces text (format: 'old:new' in password)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        if ':' not in password:
            return data
        old, new = password.split(':', 1)
        text = data.decode('utf-8', errors='replace')
        return text.replace(old, new).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        if ':' not in password:
            return data
        old, new = password.split(':', 1)
        text = data.decode('utf-8', errors='replace')
        # To decrypt, we reverse the replacement (new -> old)
        # Note: This is not perfect if 'new' contains 'old' or overlaps occur
        return text.replace(new, old).encode('utf-8')


class NumeralSystemLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "numeral"

    @property
    def description(self) -> str:
        return "Convert to base N string (password=base, e.g. 2, 8, 16)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        try:
            base = int(password)
        except ValueError:
            base = 2  # Default to binary
            
        if base not in (2, 8, 10, 16):
            # Fallback for unsupported bases or implement generic if needed
            # For now, support standard computer bases
            if base == 16:
                return data.hex().encode('utf-8')
            elif base == 10:
                 return ' '.join(str(b) for b in data).encode('utf-8')
        
        result = []
        for byte in data:
            if base == 2:
                result.append(f"{byte:08b}")
            elif base == 8:
                result.append(f"{byte:03o}")
            elif base == 16: # explicit handling
                result.append(f"{byte:02x}")
            else:
                # Generic base conversion (simple)
                result.append(self._base_repr(byte, base))
                
        return ' '.join(result).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        try:
            base = int(password)
        except ValueError:
            base = 2

        text = data.decode('utf-8', errors='replace')
        parts = text.split() if ' ' in text else [text[i:i+2] for i in range(0, len(text), 2)] if base==16 else text.split()
        
        # If split failed (e.g. no spaces in hex), handle hex specifically or assume spaces
        if base == 16 and ' ' not in text:
             try:
                 return bytes.fromhex(text)
             except:
                 pass
                 
        result = bytearray()
        for p in parts:
            try:
                val = int(p, base)
                result.append(val)
            except ValueError:
                pass 
        return bytes(result)

    def _base_repr(self, number: int, base: int) -> str:
        """Helper to convert int to string in given base."""
        if number == 0:
            return '0'
        digits = []
        while number:
            digits.append(str(number % base))
            number //= base
        return ''.join(digits[::-1])

