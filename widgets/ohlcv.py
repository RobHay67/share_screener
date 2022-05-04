import streamlit as st


from pages.data.status import set_replace_col_status_for_col_adder


def edit_ohlcv(scope, config_name, col_adder ):
	
	widget_key = 'widget_' + config_name + '_' + col_adder
	display_name =  ('Column for ' + scope.config[config_name][col_adder]['name'])
	previous_selection = scope.config[config_name][col_adder]['add_columns']['column']
	pos_for_previous = scope.config['dropdowns']['ohlcv_columns'].index(previous_selection)	

	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['dropdowns']['ohlcv_columns'],
					index		=pos_for_previous, 
					on_change	=on_change_ohlcv,
					args		=(scope, config_name, col_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_ohlcv(scope:dict, config_name:str, col_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][col_adder]['add_columns']['column'] = changed_value	

	# update the page data renew status
	set_replace_col_status_for_col_adder(scope, col_adder, new_status=True)

