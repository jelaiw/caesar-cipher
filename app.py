import streamlit as st
import caesar
from textutil import disguise_text
import random

# Note, apparently this must be the first Streamlit command used in your app.
# See https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config.
st.set_page_config(page_title="Fun with Caesar Ciphers")

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
tab1, tab2, tab3 = st.tabs(['Caesar Cipher', 'ROT13', 'The Basics'])

with tab1:
    st.subheader("Caesar Cipher")
    st.markdown("The Caesar cipher ... encrypts a message by shifting each of the letters down three positions in the alphabet, wrapping back around to A if the shift reaches Z [1].")
    st.image("fig_1-2.png", width=384, caption="Figure 1: Caesar cipher example")

with tab2:
    st.subheader("ROT13")
    st.markdown("ROT13 is a special case of the Caesar cipher that replaces a letter with the 13th letter after it in the alphabet [2][3].")
    st.image("https://upload.wikimedia.org/wikipedia/commons/2/2a/ROT13.png", width=384, caption="Figure 2: ROT13 example")

with tab3:
    st.subheader("The Basics")
    with open("basics.md", "r") as f:
        st.markdown(f.read())
    st.latex(r'C = \bold{E}(K, P)')
    st.markdown("Similarly, for decryption function **D**:")
    st.latex(r'P = \bold{D}(K, C)')

st.header("Try it!")

st.sidebar.subheader("Settings")
cipher_mode = st.sidebar.radio("Cipher mode", ('Encryption', 'Decryption'))
key_setting = st.sidebar.selectbox("Shift key", ('Caesar', 'ROT13', 'Custom'))
key = 3
if key_setting == 'ROT13':
	key = 13
elif key_setting == 'Custom':
	key = st.sidebar.slider("Custom Key", 1, 25, 3)

force_upper = st.sidebar.checkbox("Force uppercase", value=True, help="Force text to uppercase.")
disguise = st.sidebar.checkbox("Disguise word boundaries", help="Rewrite text into fixed length blocks.")

col1, col2 = st.columns(2)
with col1:
	MAX_CHARS = 280
	previous_text = ""
	if 'text' in st.session_state:
		previous_text = st.session_state.text
	text = st.text_area("Type or paste in text to encrypt or decrypt", help=f"Limit of {MAX_CHARS} characters.", value=previous_text, max_chars=MAX_CHARS)
	if disguise:
		text = disguise_text(text)
	if force_upper:
		text = text.upper()

st.button(f"Click Me {st.session_state.emoji}", on_click=button_handler, args=(text, cipher_mode,key, ))
st.markdown("Key = **{0}**".format(key))

st.header("References")
with open("references.md", "r") as f:
	st.markdown(f.read())
