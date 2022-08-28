


import streamlit as st

from widgets.drill import drill_website_button
from widgets.drill import drill_app_button


def render_app_navigation(scope):

	col1,col2,col3,col4,col5,col6,col7,col8,col9,col10 = st.columns([1,1,1,1,1,1,1,1,1,1])

	app = scope.apps['display_app']
	show_quick_link_navigation = True

	if app == 'screener':
		if len(scope.apps[app]['worklist']) == 1:
			ticker = scope.apps[app]['worklist'][0]
		else:
			show_quick_link_navigation = False
	else:
		ticker = scope.apps[app]['selectors']['ticker']


	if show_quick_link_navigation:
		with col1 : st.write('Quick Links')
		
		if app != 'single':
			with col2:
				drill_app_button(scope, 'single', ticker)
		if app != 'intraday':
			with col3:
				drill_app_button(scope, 'intraday', ticker)
		if app != 'volume':
			with col4: 
				drill_app_button(scope, 'volume', ticker)
		if app != 'research':
			with col5:
				drill_app_button(scope, 'research', ticker)
		if app != 'screener':
			with col6:
				drill_app_button(scope, 'screener', ticker)
		
		with col7 : drill_website_button(scope, 'asx', ticker)
		with col8 : drill_website_button(scope, 'google', ticker)
		with col9 : drill_website_button(scope, 'yahoo', ticker)
		with col10 : drill_website_button(scope, 'marketindex', ticker)