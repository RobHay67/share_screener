import streamlit as st

from widgets.ticker import select_a_ticker
from widgets.search import search_ticker_by_name

from widgets.market import select_a_market
from widgets.industries import select_industries
from widgets.tickers import select_tickers
# from widgets.download import download_button
# from widgets.worklist import render_worklist
from widgets.worklist import render_worklist

from apps.worklist import update_app_worklist
# from tickers.download.controller import download_tickers


def selector_title(scope):
	button = st.button(
						label='Ticker(s) Selectors', 
						use_container_width=True, 
						disabled=True,
						)
	return button


def render_ticker_selectors(scope):

	col1,col2,col3,col4,col5 = st.columns([1.5, 2.0, 2.0, 2.0, 4.5])  #12
	
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

	update_app_worklist(scope)
	
