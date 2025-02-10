import logging
import streamlit as st
from page.navigation.button import button_page_link
from page.navigation.dropdown_external_links import button_external_link
from page.navigation.dropdown_external_links import choose_default_external_link


def add_quick_links(scope):
	logging.warning("add_quick_links")
	page = scope.display['page']
	ticker = scope.page[page]['selectors']['ticker']
	
	col1,col2,col3,col4,col5,col6,col7 = st.columns([1.0,   0.5, 0.5, 0.5, 0.5,  4.0,1.0])
	with col1 : st.write('Quick Links :')
	with col2:button_page_link(scope, 'chart', ticker)
	with col3:button_page_link(scope, 'intraday', ticker)
	with col4:button_page_link(scope, 'volume', ticker)
	with col5:button_page_link(scope, 'research', ticker)
	with col6:button_external_link(scope, ticker)
	# with col7:choose_default_external_link(scope)
