import unittest
import caesar

class TestCipherMethods(unittest.TestCase):
	def test_encrypt_happypath(self):
		self.assertEqual(caesar.encrypt("caesar"), "fdhvdu")

	def test_encrypt_shift_wraps(self):
		self.assertEqual(caesar.encrypt("zoo"), "crr")

