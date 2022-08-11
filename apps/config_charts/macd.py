import streamlit as st

import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc




def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	column_adder = 'macd'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_ohlc  (scope, type_config, column_adder)
	edit_number(scope, type_config, column_adder, 'long' )
	edit_number(scope, type_config, column_adder, 'short' )
	edit_number(scope, type_config, column_adder, 'signal' )
	st.markdown("""---""")


