import string

def remove_whitespace(text):
	return "".join(text.split())

# See https://docs.python.org/3/library/string.html#string.punctuation.
# See https://stackoverflow.com/a/60725620.
def remove_punctuation(text):
	return text.translate(str.maketrans("", "", string.punctuation))
