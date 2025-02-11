import logging
import streamlit as st
from page.navigation.button_page_link import button_page_link
from page.navigation.button_external_link import button_external_link
from page.navigation.external_links import radio_external_links


def add_quick_links(scope):
	logging.info("add_quick_links")
	page = scope.display['page']
	ticker = scope.page[page]['selectors']['ticker']
	
	col1,col2,col3,col4,col5,col6,col7 = st.columns([1.0,   0.5, 0.5, 0.5, 0.5,  5.0,1.5])
	with col1 : st.write('Quick Links :')
	with col2:button_page_link(scope, 'chart', ticker)
	with col3:button_page_link(scope, 'intraday', ticker)
	with col4:button_page_link(scope, 'volume', ticker)
	with col5:button_page_link(scope, 'research', ticker)
	with col6:radio_external_links(scope, ticker)
	with col7:button_external_link(scope, ticker)