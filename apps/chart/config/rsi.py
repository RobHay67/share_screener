
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlcv import edit_ohlcv



def render_rsi(scope):
	
	column_adder = 'rsi'
	type_config = 'charts'

	st.markdown('##### Relative Strength Index (RSI)')
	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)
	with col2:edit_ohlcv(scope, type_config, column_adder )
	with col3:edit_number(scope, type_config, column_adder, 'lookback_days' )
	
	st.markdown("""---""")


