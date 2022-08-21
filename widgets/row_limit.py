
import streamlit as st

from tickers.events.edit_row_limit import edit_row_limit_event


def edit_row_limit(scope):

	previous_selection = int(scope.apps['row_limit'])
	display_name = 'No of Rows for Analysis & Charts'
	widget_key = 'widget_row_limit'

	st.sidebar.number_input( 	
								label		=display_name,
								min_value	=100, 
								value		=previous_selection,
								on_change	=on_change_row_limit,
								args		=(scope, widget_key, ),
								key			=widget_key,
								)  


def on_change_row_limit(scope:dict, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.apps['row_limit'] = changed_value

	# update the app data refresh status
	edit_row_limit_event(scope)
	
