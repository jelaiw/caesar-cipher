import unittest
import caesar

class TestCipherMethods(unittest.TestCase):
	def test_encrypt_happypath(self):
		self.assertEqual(caesar.encrypt("caesar"), "fdhvdu")

	def test_encrypt_shift_wraps(self):
		self.assertEqual(caesar.encrypt("zoo"), "crr")

	def test_encrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.encrypt("xray"), "audb")

	def test_decrypt_happypath(self):
		self.assertEqual(caesar.decrypt("fdhvdu"), "caesar")

