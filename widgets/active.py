
import streamlit as st

from pages.data.status import set_replace_col_status_for_col_adder




def edit_active(scope, config_name, col_adder ):

	widget_key = 'widget_' + config_name + '_' + col_adder
	display_name =  '' + scope.config[config_name][col_adder]['name']
	previous_selection = scope.config[config_name][col_adder]['active']
	

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
	scope.config[config_name][col_adder]['active'] = changed_value

	# update the page data renew status
	set_replace_col_status_for_col_adder(scope, col_adder, new_status=True, caller='on_change_active_status')

	#TODO - need to redo the page templates at this point - or maybe just before we need to use the page templates
