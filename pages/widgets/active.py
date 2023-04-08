
import streamlit as st

from tickers.events.edit_active import edit_active_event



def edit_active(scope, type_config, column_adder ):

	widget_key = 'widget_active_' + type_config + '_' + column_adder
	display_name =  '' + scope[type_config][column_adder]['name']
	previous_selection = scope[type_config][column_adder]['active']
	add_columns = scope[type_config][column_adder]['add_columns']
	
	if add_columns != None:
		# add some space above active for charts/trials that have colume config
		st.write(' ')
	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, type_config, column_adder, widget_key, ),
				key			=widget_key,
				)




def on_change_active_status(scope:dict, type_config:str, column_adder:str, widget_key:str):
	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['active'] = changed_value

	# update the page data renew status
	edit_active_event(scope, type_config, column_adder, changed_value)


