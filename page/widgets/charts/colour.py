import logging
import streamlit as st



def edit_colour(scope, schema_group, schema_key ):
	logging.debug("edit_colour")
	widget_key = 'widget_colour_' + schema_group + '_' + schema_key
	display_name =  ('Colour for ' + scope[schema_group]['user_config'][schema_key]['short_name'])
	previous_selection = scope[schema_group]['user_config'][schema_key]['plot']['colour']
	pos_for_previous = scope.charts['colours'].index(previous_selection)	
	


	st.selectbox ( 
					label		=display_name, 
					options		=scope.charts['colours'],
					index		=pos_for_previous, 
					on_change	=changed_colour_selection,
					args		=(scope, schema_group, schema_key, widget_key, ),
					key			=widget_key,
					) 


def changed_colour_selection(scope:dict, schema_group:str, schema_key:str, widget_key:str):
	logging.warning("on_change_colour_selection")
	changed_value = scope[widget_key]

	# store the selection
	scope[schema_group]['user_config'][schema_key]['plot']['colour'] = changed_value	

	# update the page data renew status
	# does not require a set_refresh_ticker_df to be set to TRUE
