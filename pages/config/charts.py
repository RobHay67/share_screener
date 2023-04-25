import streamlit as st


from pages.config.three_cols import three_cols


def view_charts_config(scope):
	st.subheader('Charts Configuration - Raw Configuration Dictionaries')
	three_cols( 'Charts Configuration stored in', {}, "scope.charts['config']", widget_type='string' )
	
	st.write('---')
	for chart in scope.charts['config'].keys():
		three_cols( chart, scope.charts['config'][chart], "scope.charts['config']["+chart+"]", widget_type='string' )
