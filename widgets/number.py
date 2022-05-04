
import streamlit as st

from pages.data.status import set_replace_col_status_for_col_adder
	


def edit_number(scope, config_name, col_adder, measure ):

	widget_key = 'widget_' + config_name + '_' + col_adder + '_' + measure
	display_name = measure.capitalize() + ' for ' + scope.config[config_name][col_adder]['name']
	previous_selection = int(scope.config[config_name][col_adder]['add_columns'][measure])	

	st.number_input( 	
					label		=display_name, 
					min_value	=1,
					step		=1, 
					value		=previous_selection,
					on_change	=on_change_number,
					args		=(scope, config_name, col_adder, measure, widget_key, ),
					key			=widget_key,
					)  


def on_change_number(scope:dict, config_name:str, col_adder:str, measure:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][col_adder]['add_columns'][measure] = changed_value

	# update the page data renew status
	set_replace_col_status_for_col_adder(scope, col_adder, new_status=True)
