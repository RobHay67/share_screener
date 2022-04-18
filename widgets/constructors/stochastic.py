import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	expander = 'stochastic'
	config_name = 'charts'

	edit_active(scope, config_name, expander)
	edit_number(scope, config_name, expander, 'lookback_days' )
	edit_number(scope, config_name, expander, 'slow' )
	edit_number(scope, config_name, expander, 'signal' )
	st.markdown("""---""")


