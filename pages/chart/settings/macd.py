
import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlc import edit_ohlc



def render_macd(scope):
	
	config_key_name = 'macd'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key_name)
	with col2:edit_ohlc  (scope, config_group, config_key_name)
	with col3:edit_number(scope, config_group, config_key_name, 'long' )
	with col4:edit_number(scope, config_group, config_key_name, 'short' )
	with col5:edit_number(scope, config_group, config_key_name, 'signal' )


