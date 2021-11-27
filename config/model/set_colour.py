import streamlit as st



def edit_colour(scope, chart ):
	
	display_name = scope.charts[chart]['name']
	
	previous_colour = scope.charts[chart]['plot']['colour']

	selected_colour = st.selectbox ( 
									label=('Colour for ' + display_name), 
									options=scope.chart_colours,
									index=scope.chart_colours.index(previous_colour), 
									key=chart,
									) 
	scope.charts[chart]['plot']['colour'] = selected_colour

	# does not require a refresh_chart_df to be set to Trueh



