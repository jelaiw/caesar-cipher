import unittest
import caesar

class TestCipherMethods(unittest.TestCase):
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

	def test_check_input_uppercase(self):
		with self.assertRaises(ValueError) as context_manager:
			caesar.check_input("CAESAR")
		# Unpack args tuple to expected message (first argument).
		msg = context_manager.exception.args[0]
		self.assertEqual("illegal input", msg)

	def test_check_input_with_spaces(self):
		with self.assertRaises(ValueError) as cm:
			caesar.check_input("hello world")
		self.assertEqual("illegal input", cm.exception.args[0])

	def test_check_input_mixed_case(self):
		with self.assertRaises(ValueError) as cm:
			caesar.check_input("fDhVdU")
		self.assertEqual("illegal input", cm.exception.args[0])
