ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Note, plaintext is expected to be lowercase.
def encrypt(plaintext):
	key = 3
	# See https://docs.python.org/3/library/stdtypes.html#str.lower.
	plaintext = plaintext.lower()
	ciphertext = ""
	for letter in list(plaintext):
		# Shift index forward in the alphabet.
		index = ALPHABET.index(letter) + key
		if (index >= len(ALPHABET)): # Wrap back to beginning of alphabet.
			index = index - len(ALPHABET)
		ciphertext += ALPHABET[index]

	return ciphertext

def decrypt(ciphertext):
	key = 3
	ciphertext = ciphertext.lower()
	plaintext = ""
	for letter in list(ciphertext):
		# Shift index backward in the alphabet.
		index = ALPHABET.index(letter) - key
		plaintext += ALPHABET[index]

	return plaintext
