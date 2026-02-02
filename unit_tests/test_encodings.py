import unittest
from logics.encodings import (
    Base32Logic, Base64Logic, Ascii85Logic, 
    UrlEncodingLogic, UnicodeCodePointsLogic, IntegerEncodingLogic,
    HexEncodingLogic, BaudotCodeLogic, PunycodeLogic, BootstringLogic
)

class TestEncodings(unittest.TestCase):
    def _test_logic(self, logic, data):
        encrypted = logic.encrypt(data, "")
        decrypted = logic.decrypt(encrypted, "")
        self.assertEqual(decrypted, data, f"Logic {logic.name} failed cycle.")

    def test_base32(self):
        self._test_logic(Base32Logic(), b"hello world")

    def test_base64(self):
        self._test_logic(Base64Logic(), b"hello world")

    def test_ascii85(self):
        self._test_logic(Ascii85Logic(), b"hello world")

    def test_url(self):
        self._test_logic(UrlEncodingLogic(), b"hello world & spaces")

    def test_unicode(self):
        self._test_logic(UnicodeCodePointsLogic(), b"hello world")

    def test_integer(self):
        self._test_logic(IntegerEncodingLogic(), b"hello world")

    def test_hex(self):
        self._test_logic(HexEncodingLogic(), b"hello world")

    def test_baudot(self):
        # Baudot is limited to uppercase and some chars
        self._test_logic(BaudotCodeLogic(), b"HELLO WORLD")

    def test_punycode(self):
        self._test_logic(PunycodeLogic(), b"hello-world")

    def test_bootstring(self):
        self._test_logic(BootstringLogic(), b"hello-world")

if __name__ == "__main__":
    unittest.main()
