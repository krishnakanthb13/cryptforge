from logics.base import EncryptionLogic
import base64
import urllib.parse


class Base32Logic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "base32"

    @property
    def description(self) -> str:
        return "Base32 encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return base64.b32encode(data)

    def decrypt(self, data: bytes, password: str) -> bytes:
        return base64.b32decode(data)


class Base64Logic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "base64"

    @property
    def description(self) -> str:
        return "Base64 encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return base64.b64encode(data)

    def decrypt(self, data: bytes, password: str) -> bytes:
        return base64.b64decode(data)


class Ascii85Logic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "ascii85"

    @property
    def description(self) -> str:
        return "ASCII85 (Base85) encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return base64.a85encode(data)

    def decrypt(self, data: bytes, password: str) -> bytes:
        return base64.a85decode(data)


class UrlEncodingLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "url"

    @property
    def description(self) -> str:
        return "URL (percent) encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return urllib.parse.quote(data.decode('utf-8', errors='replace')).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        return urllib.parse.unquote(data.decode('utf-8', errors='replace')).encode('utf-8')


class UnicodeCodePointsLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "unicode"

    @property
    def description(self) -> str:
        return "Unicode code points (U+XXXX)"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace')
        return ' '.join(f'U+{ord(c):04X}' for c in text).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        parts = data.decode('utf-8', errors='replace').split()
        result = []
        for p in parts:
            if p.startswith('U+'):
                try:
                    result.append(chr(int(p[2:], 16)))
                except ValueError:
                    result.append(p)
            else:
                result.append(p)
        return ''.join(result).encode('utf-8')


class IntegerEncodingLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "integer"

    @property
    def description(self) -> str:
        return "Decimal byte values"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return ' '.join(str(b) for b in data).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        parts = data.decode('utf-8', errors='replace').split()
        return bytes(int(p) for p in parts if p.isdigit())


class HexEncodingLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "hex"

    @property
    def description(self) -> str:
        return "Hexadecimal encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        return data.hex().encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        return bytes.fromhex(data.decode('utf-8', errors='replace'))


class BaudotCodeLogic(EncryptionLogic):
    ITA2 = {
        'A': '11000', 'B': '10011', 'C': '01110', 'D': '10010', 'E': '10000',
        'F': '10110', 'G': '01011', 'H': '00101', 'I': '01100', 'J': '11010',
        'K': '11110', 'L': '01001', 'M': '00111', 'N': '00110', 'O': '00011',
        'P': '01101', 'Q': '11101', 'R': '01010', 'S': '10100', 'T': '00001',
        'U': '11100', 'V': '01111', 'W': '11001', 'X': '10111', 'Y': '10101',
        'Z': '10001', ' ': '00100', '\r': '00010', '\n': '00010'
    }
    ITA2_REV = {v: k for k, v in ITA2.items()}

    @property
    def name(self) -> str:
        return "baudot"

    @property
    def description(self) -> str:
        return "Baudot code (ITA2) binary strings"

    def encrypt(self, data: bytes, password: str) -> bytes:
        text = data.decode('utf-8', errors='replace').upper()
        res = []
        for c in text:
            # Simple handling: only map known chars, ignore others
            code = self.ITA2.get(c)
            if code:
                res.append(code)
        return ' '.join(res).encode('utf-8')

    def decrypt(self, data: bytes, password: str) -> bytes:
        bits = data.decode('utf-8', errors='replace').split()
        res = []
        for b in bits:
             c = self.ITA2_REV.get(b)
             if c: res.append(c)
        return ''.join(res).encode('utf-8')


class PunycodeLogic(EncryptionLogic):
    @property
    def name(self) -> str:
        return "punycode"

    @property
    def description(self) -> str:
        return "Punycode (IDNA) encoding"

    def encrypt(self, data: bytes, password: str) -> bytes:
        try:
             text = data.decode('utf-8')
             return text.encode('punycode')
        except Exception:
             return b""

    def decrypt(self, data: bytes, password: str) -> bytes:
        try:
            return data.decode('ascii').decode('punycode').encode('utf-8')
        except Exception:
             return b""


class BootstringLogic(EncryptionLogic):
     @property
     def name(self) -> str:
         return "bootstring"

     @property
     def description(self) -> str:
         return "Bootstring encoding (Same as Punycode)"

     def encrypt(self, data: bytes, password: str) -> bytes:
         try:
             text = data.decode('utf-8')
             return text.encode('punycode')
         except:
             return b""

     def decrypt(self, data: bytes, password: str) -> bytes:
         try:
             return data.decode('ascii').decode('punycode').encode('utf-8')
         except:
             return b""

