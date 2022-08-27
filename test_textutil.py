import unittest
from textutil import remove_whitespace
from textutil import remove_punctuation

class TestTextUtilMethods(unittest.TestCase):
	def test_remove_whitespace_happypath(self):
		self.assertEqual(remove_whitespace("we the people"), "wethepeople")

	def test_remove_punctuation_happypath(self):
		self.assertEqual(remove_punctuation("we.the people!"), "wethe people")
