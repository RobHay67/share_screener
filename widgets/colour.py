import streamlit as st



def edit_colour(scope, type_config, column_adder ):
	
	widget_key = 'widget_colour_' + type_config + '_' + column_adder
	display_name =  ('Colour for ' + scope[type_config][column_adder]['short_name'])
	previous_selection = scope[type_config][column_adder]['plot']['colour']
	pos_for_previous = scope.chart_config['colours'].index(previous_selection)	
	


	st.selectbox ( 
					label		=display_name, 
					options		=scope.chart_config['colours'],
					index		=pos_for_previous, 
					on_change	=on_change_colour_selection,
					args		=(scope, type_config, column_adder, widget_key, ),
					key			=widget_key,
					) 


def on_change_colour_selection(scope:dict, type_config:str, column_adder:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[type_config][column_adder]['plot']['colour'] = changed_value	

	# update the page data renew status
	# does not require a set_refresh_ticker_df to be set to TRUE
