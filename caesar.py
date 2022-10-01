import re
import string

def encrypt(plaintext, key=3):
	ciphertext = ""
	for ch in list(plaintext):
		alphabet = string.ascii_lowercase
		if ch.isupper():
			alphabet = string.ascii_uppercase

		index = alphabet.find(ch)
		if index == -1:
			ciphertext += ch # Not in alphabet, so pass through.
		else:
			# Shift index forward in the alphabet.
			index = alphabet.index(ch) + key
			if (index >= len(alphabet)): # Wrap back to beginning of alphabet.
				index = index - len(alphabet)
			ciphertext += alphabet[index]

	return ciphertext

def decrypt(ciphertext, key=3):
	plaintext = ""
	for ch in list(ciphertext):
		alphabet = string.ascii_lowercase
		if ch.isupper():
			alphabet = string.ascii_uppercase

		index = alphabet.find(ch)
		if index == -1:
			plaintext += ch # Not in alphabet, so pass through.
		else:
			# Shift index backward in the alphabet.
			index = alphabet.index(ch) - key
			plaintext += alphabet[index]

	return plaintext
