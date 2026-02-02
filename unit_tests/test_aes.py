import unittest
from logics.aes import AESLogic

class TestAESLogic(unittest.TestCase):
    def setUp(self):
        self.logic = AESLogic()
        self.password = "strong_password_123"
        self.data = b"Hello, CryptForge!"

    def test_happy_path(self):
        """Standard encrypt/decrypt cycle."""
        encrypted = self.logic.encrypt(self.data, self.password)
        self.assertNotEqual(encrypted, self.data)
        
        decrypted = self.logic.decrypt(encrypted, self.password)
        self.assertEqual(decrypted, self.data)

    def test_edge_case_empty_data(self):
        """Encrypting empty bytes."""
        empty_data = b""
        encrypted = self.logic.encrypt(empty_data, self.password)
        decrypted = self.logic.decrypt(encrypted, self.password)
        self.assertEqual(decrypted, b"")

    def test_error_wrong_password(self):
        """Decryption with incorrect password should fail."""
        encrypted = self.logic.encrypt(self.data, self.password)
        with self.assertRaises(ValueError):
            self.logic.decrypt(encrypted, "wrong_password")

    def test_error_corrupted_data(self):
        """Decryption of corrupted data should fail."""
        encrypted = self.logic.encrypt(self.data, self.password)
        corrupted = encrypted[:-5] + b"XXXXX"
        with self.assertRaises(ValueError):
            self.logic.decrypt(corrupted, self.password)

if __name__ == "__main__":
    unittest.main()
