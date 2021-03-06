import streamlit as st

import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc




def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	col_adder = 'macd'
	config_name = 'charts'

	edit_active(scope, config_name, col_adder)
	edit_ohlc  (scope, config_name, col_adder)
	edit_number(scope, config_name, col_adder, 'long' )
	edit_number(scope, config_name, col_adder, 'short' )
	edit_number(scope, config_name, col_adder, 'signal' )
	st.markdown("""---""")


