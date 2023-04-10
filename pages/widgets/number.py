
import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event


def edit_number(scope, config_group, config_key_name, measure ):

	widget_key = 'widget_' + config_group + '_' + config_key_name + '_' + measure
	display_name = measure.capitalize()
	if display_name == 'Timespan':display_name = display_name + '  (of last x days)'
	previous_selection = int(scope[config_group][config_key_name]['add_columns'][measure])	

	st.number_input( 	
					label		=display_name, 
					min_value	=1,
					step		=1, 
					value		=previous_selection,
					on_change	=on_change_number,
					args		=(scope, config_group, config_key_name, measure, widget_key, ),
					key			=widget_key,
					)  


def on_change_number(scope:dict, config_group:str, config_key_name:str, measure:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_group][config_key_name]['add_columns'][measure] = changed_value

	# update the page data renew status
	edit_column_adder_event(scope, config_key_name)
