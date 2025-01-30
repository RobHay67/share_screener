import streamlit as st

from page.header.controller import show_page_header


# Page Configuration
scope = st.session_state
page = 'intraday'
scope.display['page'] = page


show_page_header(scope)

if scope.users['logged_in']:
	
	ticker = scope.page[page]['selectors']['ticker']

	st.error('TODO render_intraday_page')

	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.tickers.keys()):

			st.error('TODO render_intraday_page')
