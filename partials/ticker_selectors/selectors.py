import streamlit as st

from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers
from widgets.download import download_button

from partials.ticker_selectors.ticker_list import update_ticker_list
from tickers.download.controller import download_tickers


def render_ticker_selectors(scope):

	col1,col2,col3,col4,col5 = st.columns([2.0, 3.0, 2.0, 3.0, 2.0])
	
	app = scope.apps['display_app']

	if app != 'screener':
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay

		with col1:
			select_a_ticker(scope)
		with col5:
			download_button(scope)

	
	if app == 'screener':	
		# Screener app (Potentially Multiple Tickers depending on the dropdown selections)
		
		with col1: 
			select_tickers(scope)
		with col2: 
			select_industries(scope)
		with col3: 
			select_a_market(scope)
		with col5:
			download_ticker_data = download_button(scope)

	with col4: 
		search_ticker_by_name(scope)

	if download_ticker_data:download_tickers(scope)

	we_have_selected_tickers = update_ticker_list(scope)

	return we_have_selected_tickers
