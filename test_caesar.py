import unittest
import caesar

class TestCipherMethods(unittest.TestCase):
	def test_encrypt_happypath(self):
		self.assertEqual(caesar.encrypt("caesar"), "fdhvdu")

	def test_encrypt_shift_wraps(self):
		self.assertEqual(caesar.encrypt("zoo"), "crr")

	def test_encrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.encrypt("xray"), "audb")

	def test_encrypt_uppercase_input(self):
		self.assertEqual(caesar.encrypt("CAESAR"), "fdhvdu")

	def test_encrypt_mixed_case_input(self):
		self.assertEqual(caesar.encrypt("Caesar"), "fdhvdu")

	def test_encrypt_input_with_spaces(self):
		with self.assertRaises(ValueError) as context_manager:
			caesar.encrypt("hello world")
		# Unpack args tuple to expected message (first argument).
		msg = context_manager.exception.args[0]
		self.assertEqual("illegal input", msg)

	def test_decrypt_happypath(self):
		self.assertEqual(caesar.decrypt("fdhvdu"), "caesar")

	def test_decrypt_shift_wraps(self):
		self.assertEqual(caesar.decrypt("crr"), "zoo")

	def test_decrypt_shift_wraps_2(self):
		self.assertEqual(caesar.decrypt("bar"), "yxo")

	def test_decrypt_exact_shift_boundary(self):
		self.assertEqual(caesar.decrypt("audb"), "xray")

	def test_decrypt_uppercase_input(self):
		self.assertEqual(caesar.decrypt("FDHVDU"), "caesar")

	def test_decrypt_mixed_case_input(self):
		self.assertEqual(caesar.decrypt("fDhVdU"), "caesar")

	def test_decrypt_input_with_spaces(self):
		with self.assertRaises(ValueError) as context_manager:
			caesar.decrypt("khoor zruog")
		# Unpack args tuple to expected message (first argument).
		msg = context_manager.exception.args[0]
		self.assertEqual("illegal input", msg)
