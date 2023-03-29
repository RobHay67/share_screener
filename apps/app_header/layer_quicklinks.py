


import streamlit as st

from widgets.links import website_hyperlink
from widgets.links import link_to_app_button


def quick_links_layer(scope):

	col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11 = st.columns([1.0,   0.5, 0.5, 0.5, 0.5,   0.5, 0.5, 0.5, 0.5, 0.5,    1.0])

	app = scope.apps['display_app']
	
	if app == 'screener':
		# multi tickers possible, so quicklinks rendered against each selection
		show_links = False
	else:
		ticker = scope.apps[app]['selectors']['ticker']
		show_links = True if ticker != 'select a ticker' else False

	if show_links:
		with col1 : st.write('Quick Links :')
		
		with col2:
			link_to_app_button(scope, 'chart', ticker)
		with col3:
			link_to_app_button(scope, 'intraday', ticker)
		with col4: 
			link_to_app_button(scope, 'volume', ticker)
		with col5:
			link_to_app_button(scope, 'research', ticker)
		# dont link to screener - too complicated
		
		with col6 :website_hyperlink(scope, 'asx', ticker)
		with col7 :website_hyperlink(scope, 'google', ticker)
		with col8 :website_hyperlink(scope, 'yahoo', ticker)
		with col9 :website_hyperlink(scope, 'market index', ticker)
		with col10:website_hyperlink(scope, 'hot copper', ticker)
		with col11:website_hyperlink(scope, 'market watch', ticker)