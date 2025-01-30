

import streamlit as st


from app.views.header.i_search.button_search import seach_for_ticker_button


def show_search_results(scope):
	
	page = scope.display['page']

	search_results = scope.page[page]['search_results']

	if len(search_results) > 0:
		st.write('First 10 Search Results')
		for ticker, company_name in search_results.items():
			col1,col2,col3=st.columns([0.3,0.3,5])
			
			with col1: seach_for_ticker_button(scope, page, ticker)
			with col2: st.write(ticker)
			with col3: st.write(company_name)

			