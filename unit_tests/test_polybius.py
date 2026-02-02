import unittest
from logics.polybius import (
    PolybiusSquareLogic, TapCodeLogic, BifidCipherLogic,
    TrifidCipherLogic, ADFGXCipherLogic, NihilistCipherLogic
)

class TestPolybius(unittest.TestCase):
    def _test_logic(self, logic, data, password):
        encrypted = logic.encrypt(data, password)
        decrypted = logic.decrypt(encrypted, password)
        # Normalize: Remove spaces, upper case
        p_norm = data.decode().upper().replace('J', 'I').replace(' ', '')
        d_norm = decrypted.decode().upper().replace(' ', '')
        # Special case for TapCode which replaces K with C
        if logic.name == 'tapcode':
            p_norm = p_norm.replace('K', 'C')
        
        self.assertEqual(d_norm, p_norm, f"Logic {logic.name} failed cycle.")

    def test_polybius_square(self):
        self._test_logic(PolybiusSquareLogic(), b"HELLOWORLD", "")

    def test_tap_code(self):
        self._test_logic(TapCodeLogic(), b"HELLOWORLD", "")

    def test_bifid(self):
        self._test_logic(BifidCipherLogic(), b"HELLOWORLD", "")

    def test_trifid(self):
        # Trifid uses CUBE with '+'
        self._test_logic(TrifidCipherLogic(), b"HELLOWORLD", "")

    def test_adfgx(self):
        self._test_logic(ADFGXCipherLogic(), b"HELLOWORLD", "PHALANX")
        with self.assertRaises(ValueError):
            ADFGXCipherLogic().encrypt(b"HELLO", "")

    def test_nihilist(self):
        self._test_logic(NihilistCipherLogic(), b"HELLOWORLD", "KEY")
        with self.assertRaises(ValueError):
            NihilistCipherLogic().encrypt(b"HELLO", "")

if __name__ == "__main__":
    unittest.main()
