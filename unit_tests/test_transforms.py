import unittest
from logics.transforms import (
    ReverseLogic, CaseTransformLogic, BitwiseXorLogic,
    ReplaceLogic, NumeralSystemLogic
)

class TestTransforms(unittest.TestCase):
    def test_reverse(self):
        logic = ReverseLogic()
        data = b"hello world"
        self.assertEqual(logic.decrypt(logic.encrypt(data, ""), ""), data)
        self.assertEqual(logic.encrypt(data, ""), b"dlrow olleh")

    def test_case_swap(self):
        logic = CaseTransformLogic()
        data = b"Hello World"
        self.assertEqual(logic.encrypt(data, ""), b"hELLO wORLD")
        self.assertEqual(logic.decrypt(b"hELLO wORLD", ""), data)

    def test_bitwise_xor(self):
        logic = BitwiseXorLogic()
        data = b"hello world"
        password = "key"
        self.assertEqual(logic.decrypt(logic.encrypt(data, password), password), data)

    def test_replace(self):
        logic = ReplaceLogic()
        data = b"hello world"
        password = "o:0"
        encrypted = logic.encrypt(data, password)
        self.assertEqual(encrypted, b"hell0 w0rld")
        decrypted = logic.decrypt(encrypted, password)
        self.assertEqual(decrypted, data)

    def test_numeral_system(self):
        logic = NumeralSystemLogic()
        data = b"ABC" # bytes [65, 66, 67]
        # Binary (base 2)
        encrypted = logic.encrypt(data, "2")
        self.assertEqual(encrypted, b"01000001 01000010 01000011")
        self.assertEqual(logic.decrypt(encrypted, "2"), data)
        # Hex (base 16)
        encrypted_hex = logic.encrypt(data, "16")
        self.assertEqual(logic.decrypt(encrypted_hex, "16"), data)

if __name__ == "__main__":
    unittest.main()
