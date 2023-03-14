
import streamlit as st

from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc



def render_macd(scope):
	
	column_adder = 'macd'
	type_config = 'charts'

	# with col1:st.markdown('##### Moving Average, Convergence, Divergence (MACD)')

	col1,col2,col3,col4,col5,col6 = st.columns([1,1,1,1,1,1])

	with col1:st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	with col1:edit_active(scope, type_config, column_adder)
	with col2:edit_ohlc  (scope, type_config, column_adder)
	with col3:edit_number(scope, type_config, column_adder, 'long' )
	with col4:edit_number(scope, type_config, column_adder, 'short' )
	with col5:edit_number(scope, type_config, column_adder, 'signal' )
	
	st.markdown("""---""")


