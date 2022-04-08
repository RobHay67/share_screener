import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number




def render_volume_oscillator(scope):
	st.markdown('##### Volume Oscillator')
	metric = 'vol_osssy'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_number(scope, config_name, metric, 'fast' )
	edit_number(scope, config_name, metric, 'slow' )
	st.markdown("""---""")
