import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlc import edit_ohlc




def render_bollinger_bands(scope):
	column_adder = 'bollinger_bands'
	type_config = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, type_config, column_adder)
	with col1:st.write('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	with col2:edit_ohlc(scope, type_config, column_adder )
	with col3:edit_number(scope, type_config, column_adder, 'length' )
	with col4:edit_number(scope, type_config, column_adder, 'shift_up' )
	with col5:edit_number(scope, type_config, column_adder, 'shift_down' )
	
