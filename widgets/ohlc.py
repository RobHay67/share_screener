
import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event

def edit_ohlc(scope, type_config, column_adder ):
	
	widget_key = 'widget_' + type_config + '_' + column_adder
	display_name =  ('Column for ' +  scope[type_config][column_adder]['short_name'])
	previous_selection = scope[type_config][column_adder]['add_columns']['column']
	pos_for_previous = scope.config['dropdowns']['price_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['price_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlc,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlc(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns']['column'] = changed_value	

	# update the app data renew status
	edit_column_adder_event(scope, column_adder)
