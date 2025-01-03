import streamlit as st

from app.views.header.controller import show_page_header

# Page Configuration
page = 'intraday'
page_title = 'Intra Day Analysis'
page_icon = '🌤️'
# -----------------------------
scope = st.session_state
scope.pages['display'] = page


show_page_header(scope, page_title, page_icon)

if scope.users['logged_in']:
	
	ticker = scope.pages[page]['selectors']['ticker']

	st.error('TODO render_intraday_page')

	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.tickers.keys()):

			st.error('TODO render_intraday_page')
