import unittest
from logics.modern import RC4Logic, HashFunctionLogic, HMACLogic, BlowfishLogic

class TestModern(unittest.TestCase):
    def test_rc4(self):
        logic = RC4Logic()
        data = b"hello world"
        password = "key"
        encrypted = logic.encrypt(data, password)
        decrypted = logic.decrypt(encrypted, password)
        self.assertEqual(decrypted, data)

    def test_hash_sha256(self):
        logic = HashFunctionLogic()
        data = b"hello world"
        res = logic.encrypt(data, "")
        # SHA256 of "hello world" starts with b94d27...
        self.assertTrue(res.startswith(b"b94d27"))
        with self.assertRaises(ValueError):
            logic.decrypt(res, "")

    def test_hmac_sha256(self):
        logic = HMACLogic()
        data = b"hello world"
        res = logic.encrypt(data, "password")
        self.assertEqual(len(res), 64) # Hex digest of 256 bits
        with self.assertRaises(ValueError):
            logic.decrypt(res, "")

    def test_blowfish(self):
        try:
            import cryptography
            logic = BlowfishLogic()
            data = b"hello world"
            password = "password"
            encrypted = logic.encrypt(data, password)
            decrypted = logic.decrypt(encrypted, password)
            self.assertEqual(decrypted, data)
        except ImportError:
            self.skipTest("cryptography library not installed")

if __name__ == "__main__":
    unittest.main()
