import streamlit as st



def edit_colour(scope, schema, key ):

	display_name = scope[schema][key]['name']
	
	previous_colour = scope[schema][key]['plot']['colour']

	selected_colour = st.selectbox ( 
									label=('Colour for ' + display_name), 
									options=scope.chart_colours,
									index=scope.chart_colours.index(previous_colour), 
									key=key,
									) 
	scope[schema][key]['plot']['colour'] = selected_colour

	# does not require a set_refresh_ticker_df to be set to TRUE



