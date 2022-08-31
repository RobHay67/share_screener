


import streamlit as st

from widgets.drill import drill_website_button
from widgets.drill import drill_app_button


def render_app_navigation(scope):

	col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11 = st.columns([1, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 0.8, 3.8])

	app = scope.apps['display_app']
	show_quick_link_navigation = False

	if app != 'screener':
		ticker = scope.apps[app]['selectors']['ticker']
		show_quick_link_navigation = True


	if show_quick_link_navigation:
		with col1 : st.write('Quick Links :')
		
		with col2:
			drill_app_button(scope, 'single', ticker)
		with col3:
			drill_app_button(scope, 'intraday', ticker)
		with col4: 
			drill_app_button(scope, 'volume', ticker)
		with col5:
			drill_app_button(scope, 'research', ticker)
		# with col6:
		# 	drill_app_button(scope, 'screener', ticker)
		
		with col7 : drill_website_button(scope, 'asx', ticker)
		with col8 : drill_website_button(scope, 'google', ticker)
		with col9 : drill_website_button(scope, 'yahoo', ticker)
		with col10 : drill_website_button(scope, 'marketindex', ticker)