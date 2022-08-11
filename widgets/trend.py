import streamlit as st

from tickers.status.edit_column_adder import set_data_status


def edit_trend_direction(scope, type_config, column_adder ):

	widget_key = 'widget_direction_' + type_config + '_' + column_adder
	display_name =  '' + ('Direction for ' + scope[type_config][column_adder]['name'] )
	previous_selection = scope[type_config][column_adder]['add_columns']['trend']
	pos_for_previous = scope.trial_config['trends'].index(previous_selection)	
	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.trial_config['trends'],
					index		=pos_for_previous, 
					on_change	=on_change_trend_selection,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_trend_selection(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['add_columns']['trend'] = changed_value	

	# update the app data renew status
	set_data_status(scope, column_adder)
	