import streamlit as st

from tickers.events.edit_column_adder import set_data_status


def edit_ohlcv(scope, type_config, column_adder ):
	
	widget_key = 'widget_' + type_config + '_' + column_adder
	display_name =  ('Column for ' + scope[type_config][column_adder]['name'])
	previous_selection = scope[type_config][column_adder]['add_columns']['column']
	pos_for_previous = scope.config['dropdowns']['ohlcv_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['ohlcv_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlcv,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlcv(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns']['column'] = changed_value	

	# update the app data renew status
	set_data_status(scope, column_adder)

