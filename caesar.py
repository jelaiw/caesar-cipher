def encrypt(plaintext):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	key = 3
	ciphertext = ""
	for letter in list(plaintext):
		# Shift index forward in the alphabet.
		index = alphabet.index(letter) + key
		if (index >= len(alphabet)): # Wrap back to beginning of alphabet.
			index = index - len(alphabet)
		ciphertext += alphabet[index]

	return ciphertext
