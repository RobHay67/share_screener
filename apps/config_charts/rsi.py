
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlcv import edit_ohlcv



def render_rsi(scope):
	
	st.markdown('##### Relative Strength Index (RSI)')
	column_adder = 'rsi'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_ohlcv(scope, type_config, column_adder )
	edit_number(scope, type_config, column_adder, 'lookback_days' )
	st.markdown("""---""")


