import streamlit as st

from pages.widgets.active import edit_active
from pages.widgets.number import edit_number
from pages.widgets.ohlc import edit_ohlc

def render_line_chart(scope):
	
	config_group = 'charts'
	config_key_name = 'line'
	

	col1,col2,col3,col4,col5,col6 = st.columns([2,1,1,1,1,1])

	with col1:edit_active(scope, config_group, config_key_name)
	# with col2:edit_
	# with col2:edit_ohlc  (scope, config_group, config_key_name)
	# with col3:edit_number(scope, config_group, config_key_name, 'long' )
	# with col4:edit_number(scope, config_group, config_key_name, 'short' )
	# with col5:edit_number(scope, config_group, config_key_name, 'signal' )


# config_group - either charts or trials  is it setting_type or config_type or	
# 			or group or config_group or 
# config_name
# config_type
# config_group


# def edit_active(scope, config_group, config_key_name ):
# widget_key = 'widget_active_' + config_group + '_' + config_key_name
# display_name =  '' + scope[config_group][config_key_name]['name']
# previous_selection = scope[config_group][config_key_name]['active']
# add_columns = scope[config_group][config_key_name]['add_columns']