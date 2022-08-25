import streamlit as st
import caesar

def encrypt_handler(plaintext, key):
	ciphertext = caesar.encrypt(plaintext, key)
	st.session_state.plaintext = plaintext
	st.session_state.ciphertext = ciphertext

def decrypt_handler(ciphertext, key):
	plaintext = caesar.decrypt(ciphertext, key)
	st.session_state.plaintext = plaintext
	st.session_state.ciphertext = ciphertext

st.title("Fun with Caesar Ciphers")
st.markdown("*Dedicated to my curious, intrepid, and hard-working kiddos, AWP and AC. With much love, Dad. Have fun learning!!*")

st.header("Overview")
st.subheader("The Basics")
with open("basics.md", "r") as f:
	st.markdown(f.read())
st.latex(r'C = \bold{E}(K, P)')

st.markdown("Similarly, for decryption:")
st.latex(r'P = \bold{D}(K, C)')

st.subheader("Classic Caesar Cipher")
with open("book_quote.md", "r") as f:
	st.markdown(f.read())
st.image("fig_1-2.png", width=512, caption="Figure 1: The Caesar cipher")

st.subheader("ROT13")
with open("rot13.md", "r") as f:
	st.markdown(f.read())
st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/ROT13.png", width=384, caption="Figure 2: ROT13 example")

st.header("Try it!")

st.sidebar.subheader("Settings")
key_setting = st.sidebar.selectbox("Select a Key", ('Caesar', 'ROT13', 'Custom'))
key = 3
if key_setting == 'ROT13':
	key = 13
elif key_setting == 'Custom':
	key = st.sidebar.slider("Custom Key", 1, 25, 3)

col1, col2 = st.columns(2)
with col1:
	previous_plaintext = ""
	if 'plaintext' in st.session_state:
		previous_plaintext = st.session_state.plaintext
	st.markdown("**Plaintext**")
	plaintext = st.text_area("Text to encrypt", value=previous_plaintext)
	st.button("Encrypt", on_click=encrypt_handler, args=(plaintext, key, ))

with col2:
	previous_ciphertext = ""
	if 'ciphertext' in st.session_state:
		previous_ciphertext = st.session_state.ciphertext
	st.markdown("**Ciphertext**")
	ciphertext = st.text_area("Text to decrypt", value=previous_ciphertext)
	st.button("Decrypt", on_click=decrypt_handler, args=(ciphertext, key, ))

st.markdown("Key = **{0}**".format(key))

st.header("References")
with open("references.md", "r") as f:
	st.markdown(f.read())
