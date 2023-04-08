
import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event


def edit_number(scope, type_config, column_adder, measure ):

	widget_key = 'widget_' + type_config + '_' + column_adder + '_' + measure
	display_name = measure.capitalize()
	if display_name == 'Timespan':display_name = display_name + '  (of last x days)'
	previous_selection = int(scope[type_config][column_adder]['add_columns'][measure])	

	st.number_input( 	
					label		=display_name, 
					min_value	=1,
					step		=1, 
					value		=previous_selection,
					on_change	=on_change_number,
					args		=(scope, type_config, column_adder, measure, widget_key, ),
					key			=widget_key,
					)  


def on_change_number(scope:dict, type_config:str, column_adder:str, measure:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns'][measure] = changed_value

	# update the page data renew status
	edit_column_adder_event(scope, column_adder)
