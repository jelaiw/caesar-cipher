import unittest
from textutil import remove_whitespace
from textutil import remove_punctuation
from textutil import disguise_text

class TestTextUtilMethods(unittest.TestCase):
	def test_remove_whitespace_happypath(self):
		self.assertEqual(remove_whitespace("we the people"), "wethepeople")

	def test_remove_punctuation_happypath(self):
		self.assertEqual(remove_punctuation("we.the people!"), "wethe people")

	def test_disguise_text_happypath(self):
		# Borrow example from https://en.wikipedia.org/wiki/Substitution_cipher.
		self.assertEqual(disguise_text("SIAA ZQ LKBA. VA ZOA RFPBLUAOAR!"), "SIAAZ QLKBA VAZOA RFPBL UAOAR")
