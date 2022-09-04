import streamlit as st

from tickers.events.edit_column_adder import edit_column_adder_event


def edit_sma_direction(scope, type_config, column_adder ):
	widget_key = 'widget_direction_' + type_config + '_' + column_adder
	display_name =  '' + ('Direction for ' + scope[type_config][column_adder]['name'] )
	previous_selection = scope[type_config][column_adder]['add_columns']['trend']
	pos_for_previous = scope.trial_config['sma_directions'].index(previous_selection)	
	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.trial_config['sma_directions'],
					index		=pos_for_previous, 
					on_change	=on_change_sma_selection,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_sma_selection(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns']['trend'] = changed_value	

	# update the app data renew status
	edit_column_adder_event(scope, column_adder)
	