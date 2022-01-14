import streamlit as st


from metrics.model.set_active import edit_active
from metrics.model.set_number import edit_number
from metrics.model.set_ohlcv import edit_ohlc




def render_bollinger_bands(scope):
	# st.markdown('##### Bollinger Bands')
	metric = 'bollinger_bands'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlc(scope, config_name, metric )
	edit_number(scope, config_name, metric, 'length' )
	edit_number(scope, config_name, metric, 'shift_up' )
	edit_number(scope, config_name, metric, 'shift_down' )
	st.subheader('Moving Average Type - Rob to configure')		# TODO - Simple, Weighted, Exponential, Wilders
	st.markdown("""---""")


