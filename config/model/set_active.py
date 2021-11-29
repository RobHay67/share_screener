
import streamlit as st


from config.model.set_chart_refresh import set_refresh_charts_for_all_pages

def edit_active(scope, schema, key ):

	print(key)

	display_name =  '' + scope[schema][key]['name']
	
	previous_active_status = scope[schema][key]['active']

	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								key=key
								)

	scope[schema][key]['active'] = new_active_status

	if new_active_status != previous_active_status : 
		if schema == 'charts':
			set_refresh_charts_for_all_pages(scope)


