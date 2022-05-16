

import streamlit as st


from widgets.search import ticker_button


def render_search_results(scope):

	page = scope.pages['display_page']

	search_results = scope.pages[page]['search_results']

	if len(search_results) > 0:
		
		for ticker, company_name in search_results.items():
			col1,col2,col3=st.columns([0.3,0.3,5])
			
			with col1: ticker_button(scope, page, ticker)
			with col2: st.write(ticker)
			with col3: st.write(company_name)
			