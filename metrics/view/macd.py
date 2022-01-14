import streamlit as st

import streamlit as st


from metrics.model.set_active import edit_active
from metrics.model.set_number import edit_number
from metrics.model.set_ohlcv import edit_ohlc




def render_macd(scope):
	st.markdown('##### Moving Average, Convergence, Divergence (MACD)')
	metric = 'macd'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlc  (scope, config_name, metric)
	edit_number(scope, config_name, metric, 'long' )
	edit_number(scope, config_name, metric, 'short' )
	edit_number(scope, config_name, metric, 'signal' )
	st.markdown("""---""")


