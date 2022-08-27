import unittest
from textutil import remove_word_boundaries as remove

class TestTextUtilMethods(unittest.TestCase):
	def test_remove_word_boundaries_happypath(self):
		self.assertEqual(remove("we the people"), "wethepeople")
