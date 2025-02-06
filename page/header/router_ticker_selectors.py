import logging
import streamlit as st

from page.header.b_ticker_selectors.ticker import select_a_ticker
from page.header.b_ticker_selectors.tickers import select_tickers
from page.header.b_ticker_selectors.industries import select_industries
from page.header.b_ticker_selectors.market import select_a_market
from page.header.i_search_results.by_name import search_ticker_by_name
from page.scope.model.worklists.builder import build_list_of_selected_tickers_for_page



def row_ticker_selectors(scope):
	logging.info("row_ticker_selectors")
	col1,col2,col3,col4 = st.columns([2.0, 2.0, 2.0, 6.0])  #12
	
	page = scope.display['page']
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
	# the list of selected ticker for this page
	build_list_of_selected_tickers_for_page(scope)
	


	
	