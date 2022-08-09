import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"
PATTERN = re.compile(r'[a-z]+')

def encrypt(plaintext, key=3):
	# See https://docs.python.org/3/library/re.html#re.Pattern.fullmatch.
	if PATTERN.fullmatch(plaintext) is None:
		raise ValueError("illegal input")

	ciphertext = ""
	for letter in list(plaintext):
		# Shift index forward in the alphabet.
		index = ALPHABET.index(letter) + key
		if (index >= len(ALPHABET)): # Wrap back to beginning of alphabet.
			index = index - len(ALPHABET)
		ciphertext += ALPHABET[index]

	return ciphertext

def decrypt(ciphertext, key=3):
	if PATTERN.fullmatch(ciphertext) is None:
		raise ValueError("illegal input")
	plaintext = ""
	for letter in list(ciphertext):
		# Shift index backward in the alphabet.
		index = ALPHABET.index(letter) - key
		plaintext += ALPHABET[index]

	return plaintext
