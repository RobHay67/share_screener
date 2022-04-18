import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlc import edit_ohlc




def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	expander = 'bollinger_bands'
	config_name = 'charts'

	edit_active(scope, config_name, expander)
	edit_ohlc(scope, config_name, expander )
	edit_number(scope, config_name, expander, 'length' )
	edit_number(scope, config_name, expander, 'shift_up' )
	edit_number(scope, config_name, expander, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")

