import streamlit as st


from app.views.widgets.active import edit_active
from app.views.widgets.number import edit_number


def stochastic_settings(scope):
	
	config_key = 'stochastic'
	config_group = 'charts'

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key)
	with col2:edit_number(scope, config_group, config_key, 'lookback_days' )
	with col3:edit_number(scope, config_group, config_key, 'slow' )
	with col4:edit_number(scope, config_group, config_key, 'signal' )


