import unittest
from logics.ciphers import (
    CaesarCipherLogic, ROT13Logic, A1Z26Logic, 
    VigenereCipherLogic, AffineCipherLogic, RailFenceCipherLogic,
    SubstitutionCipherLogic, BaconCipherLogic, EnigmaMachineLogic
)

class TestCiphers(unittest.TestCase):
    def _test_logic(self, logic, data, password):
        encrypted = logic.encrypt(data, password)
        decrypted = logic.decrypt(encrypted, password)
        # Handle cases where non-alphabetic chars are stripped or modified
        self.assertEqual(decrypted.decode().upper().replace(' ', ''), 
                         data.decode().upper().replace(' ', ''),
                         f"Logic {logic.name} failed cycle.")

    def test_caesar(self):
        logic = CaesarCipherLogic()
        self._test_logic(logic, b"HELLO WORLD", "key")

    def test_rot13(self):
        logic = ROT13Logic()
        self._test_logic(logic, b"HELLO WORLD", "")

    def test_a1z26(self):
        logic = A1Z26Logic()
        self._test_logic(logic, b"HELLOWORLD", "")

    def test_vigenere(self):
        logic = VigenereCipherLogic()
        self._test_logic(logic, b"HELLO WORLD", "KEY")
        with self.assertRaises(ValueError):
            logic.encrypt(b"HELLO", "")

    def test_affine(self):
        logic = AffineCipherLogic()
        self._test_logic(logic, b"HELLO WORLD", "key")

    def test_railfence(self):
        logic = RailFenceCipherLogic()
        self._test_logic(logic, b"HELLO WORLD", "3")

    def test_substitution(self):
        logic = SubstitutionCipherLogic()
        self._test_logic(logic, b"HELLO WORLD", "PASSWORD")

    def test_bacon(self):
        logic = BaconCipherLogic()
        # Bacon usually ignores spaces during decryption if not handled
        self._test_logic(logic, b"HELLOWORLD", "")

    def test_enigma(self):
        logic = EnigmaMachineLogic()
        self._test_logic(logic, b"HELLO WORLD", "AAA")

if __name__ == "__main__":
    unittest.main()
