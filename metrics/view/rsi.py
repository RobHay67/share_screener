
import streamlit as st


from metrics.model.set_active import edit_active
from metrics.model.set_number import edit_number
from metrics.model.set_ohlcv import edit_ohlcv



def render_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	metric = 'rsi'
	config_name = 'charts'

	edit_active(scope, config_name, metric)
	edit_ohlcv(scope, config_name, metric )
	edit_number(scope, config_name, metric, 'lookback_days' )
	st.markdown("""---""")


