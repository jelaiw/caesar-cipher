def encrypt(plaintext):
	alphabet = "abcdefghijklmnopqrstuvwxyz"
	key = 3
	ciphertext = ""
	for letter in list(plaintext):
		shift_index = alphabet.index(letter) + key
		if (shift_index > len(alphabet)):
			shift_index = shift_index - len(alphabet)
		ciphertext += alphabet[shift_index]

	return ciphertext
