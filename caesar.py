import re

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def encrypt(plaintext, key=3):
	ciphertext = ""
	for ch in list(plaintext):
		index = ALPHABET.find(ch)
		if index == -1:
			ciphertext += ch # Not in alphabet, so pass through.
		else:
			# Shift index forward in the alphabet.
			index = ALPHABET.index(ch) + key
			if (index >= len(ALPHABET)): # Wrap back to beginning of alphabet.
				index = index - len(ALPHABET)
			ciphertext += ALPHABET[index]

	return ciphertext

def decrypt(ciphertext, key=3):
	plaintext = ""
	for ch in list(ciphertext):
		index = ALPHABET.find(ch)
		if index == -1:
			plaintext += ch # Not in alphabet, so pass through.
		else:
			# Shift index backward in the alphabet.
			index = ALPHABET.index(ch) - key
			plaintext += ALPHABET[index]

	return plaintext
