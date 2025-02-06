


import logging
import streamlit as st

from page.navigation.links import website_hyperlink
from page.navigation.button import button_page_link


def add_quick_links(scope):
	logging.debug("add_quick_links")
	col1,col2,col3,col4,col5,col6,col7,col8,col9,col10,col11 = st.columns([1.0,   0.5, 0.5, 0.5, 0.5,   0.5, 0.5, 0.5, 0.5, 0.5,    1.0])

	page = scope.display['page']
	if page != 'screener':
		ticker = scope.page[page]['selectors']['ticker']

		with col1 : st.write('Quick Links :')
		with col2:button_page_link(scope, 'chart', ticker)
		with col3:button_page_link(scope, 'intraday', ticker)
		with col4:button_page_link(scope, 'volume', ticker)
		with col5:button_page_link(scope, 'research', ticker)
		# dont link to screener - too complicated
		with col6 :website_hyperlink(scope, 'asx', ticker)
		with col7 :website_hyperlink(scope, 'google', ticker)
		with col8 :website_hyperlink(scope, 'yahoo', ticker)
		with col9 :website_hyperlink(scope, 'market index', ticker)
		with col10:website_hyperlink(scope, 'hot copper', ticker)
		with col11:website_hyperlink(scope, 'market watch', ticker)
	