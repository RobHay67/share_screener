import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_stochastic(scope):
	st.markdown('##### Stochastic Oscillator')
	col_adder = 'stochastic'
	config_name = 'charts'

	edit_active(scope, config_name, col_adder)
	edit_number(scope, config_name, col_adder, 'lookback_days' )
	edit_number(scope, config_name, col_adder, 'slow' )
	edit_number(scope, config_name, col_adder, 'signal' )
	st.markdown("""---""")


