import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
PATTERN = re.compile(r'[a-z]+')

# Check that plaintext (or ciphertext) input is part of defined alphabet.
def check_input(text):
	# See https://docs.python.org/3/library/re.html#re.Pattern.fullmatch.
	if PATTERN.fullmatch(text) is None:
		raise ValueError("illegal input")

def encrypt(plaintext, key=3):
	check_input(plaintext)

	ciphertext = ""
	for letter in list(plaintext):
		# Shift index forward in the alphabet.
		index = ALPHABET.index(letter) + key
		if (index >= len(ALPHABET)): # Wrap back to beginning of alphabet.
			index = index - len(ALPHABET)
		ciphertext += ALPHABET[index]

	return ciphertext

def decrypt(ciphertext, key=3):
	check_input(ciphertext)

	plaintext = ""
	for letter in list(ciphertext):
		# Shift index backward in the alphabet.
		index = ALPHABET.index(letter) - key
		plaintext += ALPHABET[index]

	return plaintext
