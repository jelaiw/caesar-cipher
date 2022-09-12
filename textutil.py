import string
import textwrap

# Disguise text by omitting punctuation and spaces and re-writing in blocks of fixed length (five character groups).
# See https://en.wikipedia.org/wiki/Substitution_cipher for further context.
def disguise_text(text, blocksize=5):
	text = remove_whitespace(text)
	text = remove_punctuation(text)

	# See https://docs.python.org/3.8/library/textwrap.html#textwrap.wrap.
	# Credit to https://stackoverflow.com/a/21351295 for lead on textwrap.
	return " ".join(textwrap.wrap(text, blocksize))

def remove_whitespace(text):
	return "".join(text.split())

# See https://docs.python.org/3/library/string.html#string.punctuation.
# See https://stackoverflow.com/a/60725620.
def remove_punctuation(text):
	return text.translate(str.maketrans("", "", string.punctuation))
