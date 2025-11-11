import streamlit as st

# Credit to Copilot for this first pass implementation of a "decoder ring" visualization.
def render_decoder_ring(key: int):
    """
    Render a compact mapping table showing the standard alphabet and the alphabet shifted by `key`.
    Colors optimized for Streamlit dark theme.
    """
    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifted = ALPH[key:] + ALPH[:key]

    # Styles tuned for dark backgrounds:
    # - light text for the original alphabet
    # - soft green for shifted alphabet
    # - muted borders and dark cell backgrounds for contrast
    cell_style = (
        "padding:8px;border-right:1px solid #334155;text-align:center;"
        "font-family:monospace;color:#E6EEF6;background:transparent;font-weight:600;"
    )
    shift_style = (
        "padding:8px;border-right:1px solid #334155;text-align:center;"
        "font-family:monospace;color:#BBF7D0;background:#071022;font-weight:600;"
    )

    table_cells = "".join(
        f'<td style="{cell_style}">{ch}</td>' for ch in ALPH
    )
    table_shift = "".join(
        f'<td style="{shift_style}">{ch}</td>' for ch in shifted
    )

    table_html = f'''
        <div style="display:inline-block;padding:6px;border-radius:8px;
                    background:linear-gradient(180deg, rgba(255,255,255,0.01), rgba(255,255,255,0.00));
                    border:1px solid #0f1720;">
            <table style="border-collapse:collapse;margin-bottom:8px">
                <tr>{table_cells}</tr>
                <tr>{table_shift}</tr>
            </table>
        </div>
    '''
    st.markdown(table_html, unsafe_allow_html=True)
