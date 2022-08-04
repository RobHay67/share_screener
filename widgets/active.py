
import streamlit as st

from apps.data.status import set_replace_col_status_for_col_adder




def edit_active(scope, config_name, col_adder ):

	print(config_name)
	print(col_adder)

	widget_key = 'widget_active_' + config_name + '_' + col_adder
	display_name =  '' + scope[config_name][col_adder]['name']
	previous_selection = scope[config_name][col_adder]['active']
	

	st.checkbox( 
				label		=display_name, 
				value		=previous_selection,
				on_change	=on_change_active_status,
				args		=(scope, config_name, col_adder, widget_key, ),
				key			=widget_key,
				)



def on_change_active_status(scope:dict, config_name:str, col_adder:str, widget_key:str):
	changed_value = scope[widget_key]

	# store the selection
	scope[config_name][col_adder]['active'] = changed_value

	# update the app data renew status
	set_replace_col_status_for_col_adder(scope, col_adder, new_status=True)

	# Because this widget can turn on or off charts and trials, we need to
	# also update the templates with the latest status
	scope.apps['templates'][config_name][col_adder] = changed_value
