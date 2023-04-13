
import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number


def render_macd_vol(scope):
	
	config_key = 'macd_vol'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:
		st.write('Column for MACD Vol')
		st.caption('Volume')
	with col3:edit_number(scope, config_group, config_key, 'long' )
	with col4:edit_number(scope, config_group, config_key, 'short' )
	with col5:edit_number(scope, config_group, config_key, 'signal' )
