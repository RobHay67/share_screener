import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event


def edit_ohlcv(scope, config_group, config_key ):
	widget_key = 'widget_' + config_group + '_' + config_key
	display_name =  ('This value')
	previous_selection = scope[config_group]['config'][config_key]['add_columns']['column']
	pos_for_previous = scope.pages['dropdowns']['ohlcv_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.pages['dropdowns']['ohlcv_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlcv,
					args		=(scope, config_group, config_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlcv(scope:dict, config_group:str, config_key:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_group]['config'][config_key]['add_columns']['column'] = changed_value	

	# update the page data renew status
	edit_column_adder_event(scope, config_key)

