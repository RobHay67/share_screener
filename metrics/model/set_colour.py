import streamlit as st



def edit_colour(scope, config_name, metric ):

	display_name = scope[config_name][metric]['name']
	
	previous_colour = scope[config_name][metric]['plot']['colour']

	selected_colour = st.selectbox ( 
									label=('Colour for ' + display_name), 
									options=scope.config['charts']['colours'],
									index=scope.config['charts']['colours'].index(previous_colour), 
									key=metric,
									) 
	scope[config_name][metric]['plot']['colour'] = selected_colour

	# does not require a set_refresh_ticker_df to be set to TRUE



