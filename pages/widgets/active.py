
import streamlit as st

from tickers.events.edit_active import edit_active_event



def edit_active(scope, config_group, config_key_name ):

	widget_key = 'widget_active_' + config_group + '_' + config_key_name
	display_name =  '' + scope[config_group][config_key_name]['name']
	previous_selection = scope[config_group][config_key_name]['active']
	add_columns = scope[config_group][config_key_name]['add_columns']
	
	if add_columns != None:
		# add some space above active for charts/trials that have colume config
		st.write(' ')
	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, config_group, config_key_name, widget_key, ),
				key			=widget_key,
				)




def on_change_active_status(scope:dict, config_group:str, config_key_name:str, widget_key:str):
	changed_value = scope[widget_key]

	# store the selection
	scope[config_group][config_key_name]['active'] = changed_value

	# update the page data renew status
	edit_active_event(scope, config_group, config_key_name, changed_value)


