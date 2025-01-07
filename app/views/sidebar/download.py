import streamlit as st


def edit_download_days(scope):
	
	display_name = 'Interval for Download'
	widget_key = 'widget_download_days'
	permitted_options = scope.yf['periods']
	previous_selection = scope.config['download_days']
	pos_for_previous = scope.yf['periods'].index(previous_selection)	

	st.sidebar.selectbox( 	
							label		=display_name, 
							options		=permitted_options,
							index		=pos_for_previous,
							on_change	=on_change_download_days,
							args		=(scope, widget_key, ),
							key			=widget_key,
							) 


def on_change_download_days(scope:dict, widget_key:str):

	changed_value = scope[widget_key]

	# store the selection
	scope.config['download_days'] = changed_value

