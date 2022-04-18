import streamlit as st



def edit_colour(scope, config_name, expander ):
	
	widget_key = 'widget_' + config_name + '_' + expander
	display_name =  ('Colour for ' + scope.config[config_name][expander]['name'])
	previous_selection = scope.config[config_name][expander]['plot']['colour']
	pos_for_previous = scope.config['charts']['colours'].index(previous_selection)	
	


	st.selectbox ( 
					label		=display_name, 
					options		=scope.config['charts']['colours'],
					index		=pos_for_previous, 
					on_change	=on_change_colour_selection,
					args		=(scope, config_name, expander, widget_key, ),
					key			=widget_key,
					) 


def on_change_colour_selection(scope:dict, config_name:str, expander:str, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config[config_name][expander]['plot']['colour'] = changed_value	

	# update the page data renew status
	# does not require a set_refresh_ticker_df to be set to TRUE
