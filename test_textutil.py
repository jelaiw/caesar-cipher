import unittest
from textutil import remove_whitespace

class TestTextUtilMethods(unittest.TestCase):
	def test_remove_whitespace_happypath(self):
		self.assertEqual(remove_whitespace("we the people"), "wethepeople")
