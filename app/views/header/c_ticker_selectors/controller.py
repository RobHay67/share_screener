import streamlit as st

from app.views.header.c_ticker_selectors.ticker import select_a_ticker
from app.views.header.c_ticker_selectors.tickers import select_tickers
from app.views.header.c_ticker_selectors.industries import select_industries
from app.views.header.c_ticker_selectors.market import select_a_market
from app.views.header.i_search.by_name import search_ticker_by_name
from app.worklists.builder import refresh_page_worklist



def show_ticker_selectors(scope):

	col1,col2,col3,col4 = st.columns([2.0, 2.0, 2.0, 6.0])  #12
	
	page = scope.pages['display']
	layer_title = 'Ticker(s) Selectors'

	if page == 'screener':
		with col1:select_tickers(scope)
		with col2:select_industries(scope)
		with col3:select_a_market(scope)
		with col4:search_ticker_by_name(scope)

	if page in ['chart', 'intraday', 'volume', 'research']:
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay
		with col1:select_a_ticker(scope)
		with col4:search_ticker_by_name(scope)

	# After making selections (or not) we need to update
	# the worklist (targeted tickers) for this page
	refresh_page_worklist(scope)
	


	
	