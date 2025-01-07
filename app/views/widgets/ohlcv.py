import streamlit as st

from add_cols.events.edit_column_adder import edit_column_adder_event


def edit_ohlcv(scope, schema_group, schema_key ):
	widget_key = 'widget_' + schema_group + '_' + schema_key
	display_name =  ('This ticker metric')
	previous_selection = scope[schema_group]['user_config'][schema_key]['add_columns']['column']
	pos_for_previous = scope.config['dropdowns']['ohlcv_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['ohlcv_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlcv,
					args		=(scope, schema_group, schema_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlcv(scope:dict, schema_group:str, schema_key:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['add_columns']['column'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, schema_key)

