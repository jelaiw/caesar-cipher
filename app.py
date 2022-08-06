import streamlit as st
import caesar

st.title("The Caesar Cipher")

plaintext = st.text_area("Plaintext")

if st.button("Encrypt"):
	ciphertext = caesar.encrypt(plaintext)
	st.text_area("Ciphertext", ciphertext)
