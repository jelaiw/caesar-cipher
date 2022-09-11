import string
import re

# Disguise text by omitting punctuation and spaces and re-writing in blocks of fixed length (five character groups).
# See https://en.wikipedia.org/wiki/Substitution_cipher for further context.
def disguise_text(text):
	text = remove_whitespace(text)
	text = remove_punctuation(text)

	BLOCK_SIZE = 5
	if len(text) <= BLOCK_SIZE:
		return text

	BLOCKS = re.compile(".....?").findall # See https://stackoverflow.com/a/65245113.
	return " ".join(BLOCKS(text))

def remove_whitespace(text):
	return "".join(text.split())

# See https://docs.python.org/3/library/string.html#string.punctuation.
# See https://stackoverflow.com/a/60725620.
def remove_punctuation(text):
	return text.translate(str.maketrans("", "", string.punctuation))
