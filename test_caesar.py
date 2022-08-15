import unittest
import caesar

class TestCipherMethods(unittest.TestCase):
	def test_encrypt_rot13_happypath(self):
		self.assertEqual(caesar.encrypt("hello", key=13), "uryyb")

	def test_decrypt_rot13_happypath(self):
		self.assertEqual(caesar.decrypt("uryyb", key=13), "hello")

	def test_encrypt_happypath(self):
		self.assertEqual(caesar.encrypt("caesar"), "fdhvdu")

	def test_decrypt_happypath(self):
		self.assertEqual(caesar.decrypt("fdhvdu"), "caesar")

	def test_encrypt_shift_wraps(self):
		self.assertEqual(caesar.encrypt("zoo"), "crr")

	def test_decrypt_shift_wraps(self):
		self.assertEqual(caesar.decrypt("crr"), "zoo")

	def test_decrypt_shift_wraps_2(self):
		self.assertEqual(caesar.decrypt("bar"), "yxo")

	def test_encrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.encrypt("xray"), "audb")

	def test_decrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.decrypt("audb"), "xray")

	def test_encrypt_input_with_spaces(self):
		self.assertEqual(caesar.encrypt("hello world"), "khoor zruog")

	def test_decrypt_input_with_number_and_symbol(self):
		self.assertEqual(caesar.decrypt("fd3v@u"), "ca3s@r")

	def test_encrypt_uppercase_input(self):
		self.assertEqual(caesar.encrypt("CAESAR"), "FDHVDU")

	def test_decrypt_uppercase_input(self):
		self.assertEqual(caesar.decrypt("fDhVdU"), "cAeSaR")
