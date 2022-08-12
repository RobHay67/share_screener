

import streamlit as st


from widgets.search import ticker_button


def render_search_results(scope):
	
	app = scope.apps['display_app']

	search_results = scope.apps[app]['search_results']

	print('search results = ', search_results)

	if len(search_results) > 0:
		st.write('First 10 Search Results')
		for ticker, company_name in search_results.items():
			col1,col2,col3=st.columns([0.3,0.3,5])
			
			with col1: ticker_button(scope, app, ticker)
			with col2: st.write(ticker)
			with col3: st.write(company_name)
	else:
		st.write('No Search Results')
			