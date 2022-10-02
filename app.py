import streamlit as st
import caesar
from textutil import disguise_text
import random

# See https://discuss.streamlit.io/t/how-to-add-emoji-to-a-button/15513/2.
# This seemed fun. :-D
def random_emoji():
	st.session_state.emoji = random.choice(emojis)

if "emoji" not in st.session_state:
	st.session_state.emoji = "👈"

emojis = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼"]

def button_handler(text, cipher_mode, key):
	if cipher_mode == 'Encryption':
		text = caesar.encrypt(text, key)
	elif cipher_mode == 'Decryption':
		text = caesar.decrypt(text, key)
	else:
		raise ValueError(cipher_mode)
	st.session_state.text = text
	random_emoji()

st.title("Fun with Caesar Ciphers")

st.header("Overview")
st.subheader("The Basics")
with open("basics.md", "r") as f:
	st.markdown(f.read())
st.latex(r'C = \bold{E}(K, P)')

st.markdown("Similarly, for decryption function **D**:")
st.latex(r'P = \bold{D}(K, C)')

st.subheader("Classic Caesar Cipher")

st.markdown("The Caesar cipher ... encrypts a message by shifting each of the letters down three positions in the alphabet, wrapping back around to A if the shift reaches Z [1].")
st.image("fig_1-2.png", width=512, caption="Figure 1: The Caesar cipher")

st.subheader("ROT13")
with open("rot13.md", "r") as f:
	st.markdown(f.read())
st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/ROT13.png", width=384, caption="Figure 2: ROT13 example")

st.header("Try it!")

st.sidebar.subheader("Settings")
cipher_mode = st.sidebar.radio("Cipher mode", ('Encryption', 'Decryption'))
key_setting = st.sidebar.selectbox("Key", ('Caesar', 'ROT13', 'Custom'))
key = 3
if key_setting == 'ROT13':
	key = 13
elif key_setting == 'Custom':
	key = st.sidebar.slider("Custom Key", 1, 25, 3)

disguise = st.sidebar.checkbox("Disguise word boundaries", help="Removes punctuation and spaces. Rewrites text into fixed length blocks.")

col1, col2 = st.columns(2)
with col1:
	previous_text = ""
	if 'text' in st.session_state:
		previous_text = st.session_state.text
	text = st.text_area("Type or paste in text to encrypt or decrypt", help="What happens when you encrypt twice with ROT13?", value=previous_text, max_chars=280)
	if disguise:
		text = disguise_text(text)

st.button(f"Click Me {st.session_state.emoji}", on_click=button_handler, args=(text, cipher_mode,key, ))
st.markdown("Key = **{0}**".format(key))

st.header("References")
with open("references.md", "r") as f:
	st.markdown(f.read())
