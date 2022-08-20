
import streamlit as st

from tickers.events.edit_active import set_data_status



def edit_active(scope, type_config, column_adder ):

	widget_key = 'widget_active_' + type_config + '_' + column_adder
	display_name =  '' + scope[type_config][column_adder]['name']
	previous_selection = scope[type_config][column_adder]['active']
	

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

	# update the app data renew status
	set_data_status(scope, type_config, column_adder, changed_value)


