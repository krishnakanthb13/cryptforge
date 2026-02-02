import unittest
from logics.xor import XorLogic

class TestXor(unittest.TestCase):
    def test_xor_cycle(self):
        logic = XorLogic()
        data = b"hello world"
        password = "secret_key"
        encrypted = logic.encrypt(data, password)
        self.assertNotEqual(encrypted, data)
        decrypted = logic.decrypt(encrypted, password)
        self.assertEqual(decrypted, data)

    def test_xor_empty_password(self):
        logic = XorLogic()
        with self.assertRaises(ValueError):
            logic.encrypt(b"hello", "")

if __name__ == "__main__":
    unittest.main()
