import streamlit as st


from config.model.set_chart_refresh import set_refresh_charts_for_all_pages


def edit_active(scope, chart ):

	display_name =  '' + scope.charts[chart]['name']
	
	previous_active_status = scope.charts[chart]['active']
	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								)
	scope.charts[chart]['active'] = new_active_status

	if new_active_status != previous_active_status : 
		set_refresh_charts_for_all_pages(scope)