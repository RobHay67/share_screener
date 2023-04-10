import streamlit as st


from pages.config.three_cols import three_cols


def view_charts_config(scope):
	st.subheader('Charts Configuration - Raw Configuration Dictionaries')
	three_cols( 'Charts Configuration stored in', {}, 'scope.charts', widget_type='string' )
	for chart in scope.charts.keys():
		three_cols( chart, scope.charts[chart], 'scope.charts['+chart+']', widget_type='string' )
