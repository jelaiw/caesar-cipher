import streamlit as st
import caesar
from textutil import disguise_text
from decoder_ring import render_compact_table, render_decoder_ring

# Note, apparently this must be the first Streamlit command used in your app.
# See https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config.
st.set_page_config(page_title="Fun with Caesar ciphers")

def button_handler(text, cipher_mode, key):
	if cipher_mode == 'Encrypt text':
		text = caesar.encrypt(text, key)
	elif cipher_mode == 'Decrypt text':
		text = caesar.decrypt(text, key)
	st.session_state.text = text

st.title("Fun with Caesar ciphers")

st.header("Overview")
tab1, tab2, tab3 = st.tabs(['Caesar cipher', 'ROT13', 'The Basics'])

with tab1:
    st.subheader("Caesar cipher")
    st.markdown("\"The Caesar cipher ... encrypts a message by shifting each of the letters down three positions in the alphabet, wrapping back around to A if the shift reaches Z\" (Aumasson 2018).")
    st.image("assets/fig_1-2.png", width=384, caption="Figure 1: Caesar cipher example")

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
visual_mode = st.sidebar.radio("Visualization mode", ('Compact mapping', 'Decoder ring', 'None'))
key_setting = st.sidebar.selectbox("Shift key", ('Caesar', 'ROT13', 'Custom'))
key = 3
if key_setting == 'ROT13':
	key = 13
elif key_setting == 'Custom':
	key = st.sidebar.slider("Custom Key", 1, 25, 3)

force_upper = st.sidebar.checkbox("Force uppercase", value=True, help="Force text to uppercase.")
disguise = st.sidebar.checkbox("Disguise word boundaries", help="Rewrite text into fixed length blocks.")

# make the left column wider so the text area has more space
col1, col2 = st.columns([2, 1])
with col1:
    MAX_CHARS = 280
    previous_text = ""
    if 'text' in st.session_state:
        previous_text = st.session_state.text
    text = st.text_area("Type or paste in text to encrypt or decrypt",
                        help=f"Limit of {MAX_CHARS} characters.",
                        value=previous_text, max_chars=MAX_CHARS)
    if disguise:
        text = disguise_text(text)
    if force_upper:
        text = text.upper()

    # small spacer so the buttons don't butt directly against the text area
    st.write("")  

    # place buttons side-by-side beneath the text area so they're visually aligned
    btn_c1, btn_c2 = st.columns([1, 1])
    with btn_c1:
        st.button("Encrypt 🔐", on_click=button_handler, args=(text, 'Encrypt text', key))
    with btn_c2:
        st.button("Decrypt 🔓", on_click=button_handler, args=(text, 'Decrypt text', key))

with col2:
    # keep the right column available for visualization/output
    # (you can add previews, hints, or controls here)
    st.empty()

# Render the decoder ring visualization for the currently selected key
if visual_mode == 'Decoder ring':
    render_decoder_ring(key)
elif visual_mode == 'Compact mapping':
    render_compact_table(key)

st.markdown("Key = **{0}**".format(key))

st.header("References")
with open("references.md", "r") as f:
	st.markdown(f.read())
