import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number


def render_stochastic(scope):
	
	st.markdown('##### Stochastic Oscillator')
	column_adder = 'stochastic'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'lookback_days' )
	edit_number(scope, type_config, column_adder, 'slow' )
	edit_number(scope, type_config, column_adder, 'signal' )
	st.markdown("""---""")


