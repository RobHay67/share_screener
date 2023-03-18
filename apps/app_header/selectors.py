import streamlit as st

from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers
from widgets.download import download_button

from apps.app_header.worklist import update_app_worklist
from tickers.download.controller import download_tickers


def render_ticker_selectors(scope):

	download_ticker_data = None
	col1,col2,col3,col4,col5,col6 = st.columns([1.5, 2.0, 2.0, 2.0, 3.0, 1.5])
	
	app = scope.apps['display_app']

	with col1 : 
		st.button(
				label='Ticker(s) Selection', 
				use_container_width=True, 
				disabled=True,
				)
	if app == 'screener':
		with col2: 
			select_tickers(scope)
		with col3: 
			select_industries(scope)
		with col4: 
			select_a_market(scope)
		with col5: 
			search_ticker_by_name(scope)
	elif app == 'websites':
		# dont provide any search options - we dont have any data
		with col2: 
			st.write('No Need to show selectors')
	else:
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay
		with col2: 
			
			select_a_ticker(scope)
		with col5: 
			search_ticker_by_name(scope)

	we_have_selected_tickers = update_app_worklist(scope)
	
	if we_have_selected_tickers:
		with col6:		
			download_ticker_data = download_button(scope)

	if download_ticker_data:
		download_tickers(scope)

	
	return we_have_selected_tickers
