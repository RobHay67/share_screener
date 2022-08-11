import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc




def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	column_adder = 'bollinger_bands'
	type_config = 'charts'

	edit_active(scope, type_config, column_adder)
	edit_ohlc(scope, type_config, column_adder )
	edit_number(scope, type_config, column_adder, 'length' )
	edit_number(scope, type_config, column_adder, 'shift_up' )
	edit_number(scope, type_config, column_adder, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

