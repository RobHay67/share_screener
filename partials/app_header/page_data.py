import streamlit as st

from partials.app_worklist import render_worklist, render_errors
from widgets.dataframe import dataframe_button
from widgets.clear import clear_messages_button
from widgets.dataframe import reset_page_render








def render_page_data(scope):
	# Render Data Status - whats loaded - what has load or download errors

	app = scope.apps['display_app']

	if app in ['screener', 'chart', 'intraday']:
		
		col1,col2,col3,col4,col5,col6 = st.columns([1.0, 2.5, 2.5, 2.0, 2.0, 2.0])
		
		with col1:
			st.write('Page Data :')
		with col2:
			render_worklist(scope)
		with col3:
			render_errors(scope)
		with col4:
			dataframe_button(scope, 'tickers')
		with col5:
			if app == 'screener':
				dataframe_button(scope, 'trials')
			if app == 'chart':
				dataframe_button(scope, 'charts')		
		with col6:
			reset_page_render(scope)








