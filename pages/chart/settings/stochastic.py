import streamlit as st


from pages.widgets.active import edit_active
from pages.widgets.number import edit_number


def render_stochastic(scope):
	
	config_key = 'stochastic'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:edit_number(scope, config_group, config_key, 'lookback_days' )
	with col3:edit_number(scope, config_group, config_key, 'slow' )
	with col4:edit_number(scope, config_group, config_key, 'signal' )


