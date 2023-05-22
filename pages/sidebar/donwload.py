import streamlit as st
from y_finance.config import set_yf_period


def edit_download_days(scope):

	previous_selection = int(scope.pages['download_days'])
	display_name = 'Days to Download (recent)'
	widget_key = 'widget_download_days'

	st.sidebar.number_input( 	
							label		=display_name, 
							min_value	=7, 
							value		=previous_selection,
							on_change	=on_change_download_days,
							args		=(scope, widget_key, ),
							key			=widget_key,
							)  


def on_change_download_days(scope:dict, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.pages['download_days'] = changed_value

	# update the yf download days
	set_yf_period(scope)