import streamlit as st

from pages.header.widgets.format import md_for_header
from pages.header.widgets.ticker import select_a_ticker
from pages.header.widgets.tickers import select_tickers
from pages.header.widgets.industries import select_industries
from pages.header.widgets.market import select_a_market
from pages.header.widgets.search import search_ticker_by_name
from page.worklist import update_page_worklist
from markets.schema import markets


def selectors_layer(scope):

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
	update_page_worklist(scope)
	

def refresh_dropdown_lists(scope):
	# Repopulate the scope with the latest information for the dropdown lists
	# THis function only needs running after the ticker index has been loaded/downloaded

	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select market')
	scope.pages['dropdowns']['markets'] = list_of_markets
	
	list_of_industries = scope.ticker_index['df']['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.pages['dropdowns']['industries'] = list_of_industries
	
	#
	list_of_tickers = scope.ticker_index['df'].index.values.tolist()
	scope.pages['dropdowns']['tickers'] = list_of_tickers.copy()

	list_of_tickers.insert(0, 'select a ticker')
	scope.pages['dropdowns']['ticker'] = list_of_tickers.copy()


def refresh_ticker_dropdown_for_config(scope):
	list_of_loaded_tickers = list(scope.tickers.keys())
	list_of_loaded_tickers.insert(0, 'select a ticker')
	scope.pages['dropdowns']['config_ticker'] = list_of_loaded_tickers.copy()
	
	