import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number




def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	column_adder = 'vol_osssy'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'fast' )
	edit_number(scope, type_config, column_adder, 'slow' )
	st.markdown("""---""")
