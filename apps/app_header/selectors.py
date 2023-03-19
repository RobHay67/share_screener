import streamlit as st

from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers
from widgets.download import download_button

from apps.app_header.worklist import update_app_worklist
from tickers.download.controller import download_tickers


def selector_title(scope):
	button = st.button(
						label='Ticker(s) Selectors', 
						use_container_width=True, 
						disabled=True,
						)
	return button


def render_ticker_selectors(scope):

	download_ticker_data = None
	col1,col2,col3,col4,col5,col6 = st.columns([1.5, 2.0, 2.0, 2.0, 3.0, 1.5])
	
	app = scope.apps['display_app']

	if app == 'screener':
		with col1:selector_title(scope)
		with col2:select_tickers(scope)
		with col3:select_industries(scope)
		with col4:select_a_market(scope)
		with col5:search_ticker_by_name(scope)

	if app in ['chart', 'intraday', 'volume', 'research']:
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay
		with col1:selector_title(scope)
		with col2:select_a_ticker(scope)
		with col5:search_ticker_by_name(scope)

	# if app == 'websites':
	#	selectors not applicable for this page
	
	# if app == 'index':
	#	selectors not applicable for this page
	
		

	we_have_selected_tickers = update_app_worklist(scope)
	
	if we_have_selected_tickers:
		with col6:		
			download_ticker_data = download_button(scope)

	if download_ticker_data:
		download_tickers(scope)

	
	return we_have_selected_tickers