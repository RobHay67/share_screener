
import streamlit as st


from widgets.active import edit_active
from widgets.number import edit_number
from widgets.ohlcv import edit_ohlcv



def render_rsi(scope):
	st.markdown('##### Relative Strength Index (RSI)')
	expander = 'rsi'
	config_name = 'charts'

	edit_active(scope, config_name, expander)
	edit_ohlcv(scope, config_name, expander )
	edit_number(scope, config_name, expander, 'lookback_days' )
	st.markdown("""---""")


