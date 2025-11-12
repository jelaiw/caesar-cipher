import streamlit as st
import math

# Credit to Copilot for this first pass implementation of a "decoder ring" visualization.
def render_compact_table(key: int):
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

def render_decoder_ring(key: int):
    """
    Render a circular decoder ring SVG showing the standard alphabet on the outer ring
    and the shifted alphabet on the inner ring, with lines connecting each letter to its
    shifted counterpart. Colors are tuned for Streamlit dark theme.

    Fixed: connector lines now target the inner-letter positions so the visual mapping
    matches the chosen key.
    """
    ALPH = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key % len(ALPH)
    shifted = ALPH[key:] + ALPH[:key]

    N = len(ALPH)
    r_outer = 140
    r_inner = 90
    pad = 12
    cx = cy = r_outer + pad
    angle_step = 2 * math.pi / N
    start_angle = -math.pi / 2  # start at top

    # Build SVG elements
    lines = []
    outer_text = []
    inner_text = []

    for i in range(N):
        ang = start_angle + i * angle_step
        x_out = cx + r_outer * math.cos(ang)
        y_out = cy + r_outer * math.sin(ang)
        x_in = cx + r_inner * math.cos(ang)
        y_in = cy + r_inner * math.sin(ang)

        # Draw line from outer letter i to the inner letter at the same angular position.
        # The inner letter at this position represents the shifted character for ALPH[i].
        lines.append(
            f'<line x1="{x_out:.1f}" y1="{y_out:.1f}" x2="{x_in:.1f}" y2="{y_in:.1f}" '
            f'stroke="#60a5fa" stroke-opacity="0.28" stroke-width="1.6" />'
        )

        # outer (original) letters - light text
        outer_text.append(
            f'<text x="{x_out:.1f}" y="{y_out:.1f}" font-family="monospace" font-size="14" '
            f'text-anchor="middle" dominant-baseline="middle" fill="#E6EEF6" font-weight="700">{ALPH[i]}</text>'
        )

        # inner (shifted) letters - soft green; positioned at same angle so radial lines match mapping
        inner_text.append(
            f'<text x="{x_in:.1f}" y="{y_in:.1f}" font-family="monospace" font-size="13" '
            f'text-anchor="middle" dominant-baseline="middle" fill="#BBF7D0" font-weight="700">{shifted[i]}</text>'
        )

    svg_width = svg_height = (cx + pad) * 2

    svg = f'''
    <div style="display:flex;align-items:left;justify-content:left;padding:6px">
      <svg width="{svg_width:.0f}" height="{svg_height:.0f}" viewBox="0 0 {svg_width:.0f} {svg_height:.0f}" xmlns="http://www.w3.org/2000/svg">
        <!-- outer and inner rings -->
        <circle cx="{cx}" cy="{cy}" r="{r_outer}" fill="none" stroke="#0f1720" stroke-width="2" />
        <circle cx="{cx}" cy="{cy}" r="{r_inner}" fill="none" stroke="#0f1720" stroke-width="1.2" />
        <!-- connector lines -->
        {''.join(lines)}
        <!-- letters -->
        {''.join(outer_text)}
        {''.join(inner_text)}
      </svg>
    </div>
    '''
    st.markdown(svg, unsafe_allow_html=True)
