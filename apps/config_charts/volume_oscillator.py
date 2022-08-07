import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number




def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	col_adder = 'vol_osssy'
	config_name = 'charts'

	edit_active(scope, config_name, col_adder)
	edit_number(scope, config_name, col_adder, 'fast' )
	edit_number(scope, config_name, col_adder, 'slow' )
	st.markdown("""---""")
