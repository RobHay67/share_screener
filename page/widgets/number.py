
import logging
import streamlit as st

from add_cols.events.edit_column_adder import edit_column_adder_event


def edit_number(scope, schema_group, schema_key, measure ):
	logging.warning("edit_number")
	widget_key = 'widget_' + schema_group + '_' + schema_key + '_' + measure
	display_name = measure.capitalize()
	if display_name == 'Duration':
		display_name =  'at least this many days'
	elif display_name == 'Timespan':
		display_name = 'of the last x days'
	previous_selection = int(scope[schema_group]['user_config'][schema_key]['function'][measure])	

	st.number_input( 	
					label		=display_name, 
					min_value	=1,
					step		=1, 
					value		=previous_selection,
					on_change	=on_change_number,
					args		=(scope, schema_group, schema_key, measure, widget_key, ),
					key			=widget_key,
					)  


def on_change_number(scope:dict, schema_group:str, schema_key:str, measure:str, widget_key:str):
	logging.warning("on_change_number")
	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['function'][measure] = changed_value

	# update the page data renew status
	edit_column_adder_event(scope, schema_key)
