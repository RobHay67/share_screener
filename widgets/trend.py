import streamlit as st

from apps.data.status import set_replace_col_status_for_col_adder


def edit_trend_direction(scope, config_name, col_adder ):

	widget_key = 'widget_direction_' + config_name + '_' + col_adder
	display_name =  '' + ('Direction for ' + scope.config[config_name][col_adder]['name'] )
	previous_selection = scope.config[config_name][col_adder]['add_columns']['trend']
	pos_for_previous = scope.config['tests']['trends'].index(previous_selection)	
	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['tests']['trends'],
					index		=pos_for_previous, 
					on_change	=on_change_trend_selection,
					args		=(scope, config_name, col_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_trend_selection(scope:dict, config_name:str, col_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][col_adder]['add_columns']['trend'] = changed_value	

	# update the app data renew status
	set_replace_col_status_for_col_adder(scope, col_adder, new_status=True)
	