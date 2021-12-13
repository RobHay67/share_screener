import streamlit as st



def edit_trend(scope, schema, key ):

	display_name = scope[schema][key]['name']
	
	previous_trend = scope[schema][key]['trend']

	selected_trend = st.selectbox ( 
									label=('Direction for ' + display_name), 
									options=scope.screener_trends,
									index=scope.screener_trends.index(previous_trend), 
									key=key,
									) 
	scope[schema][key]['trend'] = selected_trend


