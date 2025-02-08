import logging
import streamlit as st

from page.header.controller import controller_page_header


# Page Configuration
scope = st.session_state
page = 'intraday'
scope.display['page'] = page
logging.info(f"{page=}")

controller_page_header(scope)

if scope.users['logged_in']:
	
	ticker = scope.page[page]['selectors']['ticker']

	st.error('render_intraday_page')
	logging.critical("render_intraday_page > page yet to be configures")
	
	
	if ticker != None :
		if ticker in list(scope.tickers.keys()):
			st.error('render_intraday_page')
