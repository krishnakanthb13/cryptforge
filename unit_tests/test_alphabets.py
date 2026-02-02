import unittest
from logics.alphabets import MorseCodeLogic, SpellingAlphabetLogic

class TestAlphabets(unittest.TestCase):
    def test_morse_code(self):
        logic = MorseCodeLogic()
        data = b"HELLO WORLD"
        encrypted = logic.encrypt(data, "")
        decrypted = logic.decrypt(encrypted, "")
        self.assertEqual(decrypted.decode().upper(), data.decode().upper())

    def test_nato_alphabet(self):
        logic = SpellingAlphabetLogic()
        data = b"HELLO WORLD"
        encrypted = logic.encrypt(data, "")
        decrypted = logic.decrypt(encrypted, "")
        self.assertEqual(decrypted.decode().upper(), data.decode().upper())

if __name__ == "__main__":
    unittest.main()
