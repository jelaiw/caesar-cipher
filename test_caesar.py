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

	def test_decrypt_shift_wraps(self):
		self.assertEqual(caesar.decrypt("crr"), "zoo")

	def test_decrypt_shift_wraps_2(self):
		self.assertEqual(caesar.decrypt("bar"), "yxo")

	def test_decrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.decrypt("audb"), "xray")
