
import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlcv import edit_ohlcv



def render_rsi(scope):
	
	config_key = 'rsi'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:edit_ohlcv(scope, config_group, config_key )
	with col3:edit_number(scope, config_group, config_key, 'lookback_days' )
	

