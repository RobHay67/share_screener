import streamlit as st



def edit_colour(scope, config_name, col_adder ):
	
	widget_key = 'widget_colour_' + config_name + '_' + col_adder
	display_name =  ('Colour for ' + scope[config_name][col_adder]['name'])
	previous_selection = scope[config_name][col_adder]['plot']['colour']
	pos_for_previous = scope.charts['colours'].index(previous_selection)	
	


	st.selectbox ( 
					label		=display_name, 
					options		=scope.charts['colours'],
					index		=pos_for_previous, 
					on_change	=on_change_colour_selection,
					args		=(scope, config_name, col_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_colour_selection(scope:dict, config_name:str, col_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_name][col_adder]['plot']['colour'] = changed_value	

	# update the app data renew status
	# does not require a set_refresh_ticker_df to be set to TRUE
