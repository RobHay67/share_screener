
import streamlit as st




def edit_active(scope, measure ):

	display_name =  '' + scope.analysis[measure]['name']
	
	previous_active_status = scope.analysis[measure]['active']
	new_active_status = st.checkbox( 
								display_name, 
								value=previous_active_status,
								)
	scope.analysis[measure]['active'] = new_active_status




