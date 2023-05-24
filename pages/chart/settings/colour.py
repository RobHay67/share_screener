import streamlit as st



def edit_colour(scope, config_group, config_key ):
	
	widget_key = 'widget_colour_' + config_group + '_' + config_key
	display_name =  ('Colour for ' + scope[config_group]['config'][config_key]['short_name'])
	previous_selection = scope[config_group]['config'][config_key]['plot']['colour']
	pos_for_previous = scope.charts['colours'].index(previous_selection)	
	


	st.selectbox ( 
					label		=display_name, 
					options		=scope.charts['colours'],
					index		=pos_for_previous, 
					on_change	=on_change_colour_selection,
					args		=(scope, config_group, config_key, widget_key, ),
					key			=widget_key,
					) 


def on_change_colour_selection(scope:dict, config_group:str, config_key:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope[config_group]['config'][config_key]['plot']['colour'] = changed_value	

	# update the page data renew status
	# does not require a set_refresh_ticker_df to be set to TRUE