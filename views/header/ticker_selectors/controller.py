import streamlit as st

from views.header.format import md_for_header
from views.header.ticker_selectors.ticker import select_a_ticker
from views.header.ticker_selectors.tickers import select_tickers
from views.header.ticker_selectors.industries import select_industries
from views.header.ticker_selectors.market import select_a_market
from views.header.search.by_name import search_ticker_by_name
from app.worklists.builder import refresh_page_worklist



def render_ticker_selectors(scope):

	col1,col2,col3,col4,col5 = st.columns([1.5, 2.0, 2.0, 2.0, 4.5])  #12
	
	page = scope.pages['display']
	layer_title = 'Ticker(s) Selectors'

	if page == 'screener':
		with col1:md_for_header(layer_title)
		with col2:select_tickers(scope)
		with col3:select_industries(scope)
		with col4:select_a_market(scope)
		with col5:search_ticker_by_name(scope)

	if page in ['chart', 'intraday', 'volume', 'research']:
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay
		with col1:md_for_header(layer_title)
		with col2:select_a_ticker(scope)
		with col5:search_ticker_by_name(scope)

	# After making selections (or not) we need to update
	# the worklist (targeted tickers) for this page
	refresh_page_worklist(scope)
	


	
	