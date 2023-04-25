
import streamlit as st

from tickers.events.edit_active import edit_active_event



def edit_active(scope, config_group, config_key ):

	widget_key = 'widget_active_' + config_group + '_' + config_key
	display_name =  '' + scope[config_group]['config'][config_key]['name']
	previous_selection = scope[config_group]['config'][config_key]['active']
	add_columns = scope[config_group]['config'][config_key]['add_columns']
	
	if add_columns != None:
		# add some space above active for charts/trials that have colume config
		st.write(' ')
		
	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, config_group, config_key, widget_key, ),
				key			=widget_key,
				)




def on_change_active_status(scope:dict, config_group:str, config_key:str, widget_key:str):
	changed_value = scope[widget_key]

	# store the selection
	scope[config_group]['config'][config_key]['active'] = changed_value

	# update the page data renew status
	edit_active_event(scope, config_group, config_key, changed_value)


