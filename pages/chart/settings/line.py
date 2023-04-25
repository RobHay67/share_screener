import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlc import edit_ohlc, edit_ohlc_active_col

def render_line_chart(scope):
	
	config_group = 'charts'
	config_key = 'line'
	
	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:edit_ohlc_active_col(scope, config_group, config_key, 'open')
	with col3:edit_ohlc_active_col(scope, config_group, config_key, 'high' )
	with col4:edit_ohlc_active_col(scope, config_group, config_key, 'low' )
	with col5:edit_ohlc_active_col(scope, config_group, config_key, 'close' )


