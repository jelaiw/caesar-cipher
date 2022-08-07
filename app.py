import streamlit as st
import caesar

def encrypt_handler(plaintext):
	ciphertext = caesar.encrypt(plaintext)
	st.session_state.plaintext = plaintext
	st.session_state.ciphertext = ciphertext

def decrypt_handler(ciphertext):
	plaintext = caesar.decrypt(ciphertext)
	st.session_state.plaintext = plaintext
	st.session_state.ciphertext = ciphertext

st.title("The Caesar Cipher")

st.header("Overview")
st.subheader("The Basics")
with open("basics.md", "r") as f:
	st.markdown(f.read())
st.latex(r'C = \bold{E}(K, P)')

st.markdown("Similarly, when the cipher is in decryption mode:")
st.latex(r'P = \bold{D}(K, C)')

st.subheader("The Caesar Cipher")
with open("caesar.md", "r") as f:
	st.markdown(f.read())
st.image("fig_1-2.png", width=512, caption="Figure 1-2: The Caesar cipher [1]")

st.header("Try it!")

col1, col2 = st.columns(2)

with col1:
	previous_plaintext = ""
	if 'plaintext' in st.session_state:
		previous_plaintext = st.session_state.plaintext
	plaintext = st.text_area("Plaintext", value=previous_plaintext)
	st.button("Encrypt", on_click=encrypt_handler, args=(plaintext, ))

with col2:
	previous_ciphertext = ""
	if 'ciphertext' in st.session_state:
		previous_ciphertext = st.session_state.ciphertext
	ciphertext = st.text_area("Ciphertext", value=previous_ciphertext)
	st.button("Decrypt", on_click=decrypt_handler, args=(ciphertext, ))

st.header("References")
with open("references.md", "r") as f:
	st.markdown(f.read())
