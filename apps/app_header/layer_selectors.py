import streamlit as st

from widgets.ticker import select_a_ticker
from widgets.tickers import select_tickers

from widgets.industries import select_industries
from widgets.market import select_a_market
from widgets.search import search_ticker_by_name

from apps.worklist import update_app_worklist
from markets.schema import markets


def selectors_layer(scope):

	col1,col2,col3,col4,col5 = st.columns([1.5, 2.0, 2.0, 2.0, 4.5])  #12
	
	app = scope.apps['display_app']
	layer_title = st.caption('Ticker(s) Selectors')

	if app == 'screener':
		with col1:layer_title
		with col2:select_tickers(scope)
		with col3:select_industries(scope)
		with col4:select_a_market(scope)
		with col5:search_ticker_by_name(scope)

	if app in ['chart', 'intraday', 'volume', 'research']:
		# One of the Single Ticker Pages - Single / Volume / Research or IntraDay
		with col1:layer_title
		with col2:select_a_ticker(scope)
		with col5:search_ticker_by_name(scope)

	# if app == 'websites':
	#	selectors not applicable for this page
	
	# if app == 'index':
	#	selectors not applicable for this page

	# After making selections (or not) we need to update
	# the worklist (targeted tickers) for this page
	update_app_worklist(scope)
	





def refresh_dropdown_lists(scope):
	# Repopulate the scope with the latest information for the dropdown lists
	# THis function only needs running after the ticker index has been loaded/downloaded

	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select market')
	scope.config['dropdowns']['markets'] = list_of_markets
	
	list_of_industries = scope.ticker_index['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.config['dropdowns']['industries'] = list_of_industries
	
	list_of_tickers = scope.ticker_index.index.values.tolist()
	scope.config['dropdowns']['tickers'] = list_of_tickers

	alt_ticker_list = scope.ticker_index.index.values.tolist()
	alt_ticker_list.insert(0, 'select a ticker')
	scope.config['dropdowns']['ticker'] = alt_ticker_list
	
	