import logging
import streamlit as st


def select_a_ticker(scope):
	logging.debug("select_a_ticker")
	page = scope.display['page']
	
	widget_key = 'widget_' + page + '_select_ticker'
	display_name = 'Select a Ticker'

	previous_selection = scope.page[page]['selectors']['ticker']
	if previous_selection != None:
		pos_for_previous = scope.config['dropdowns']['ticker'].index(previous_selection)	
	else: 
		pos_for_previous = 0

	st.selectbox ( 
				label		=display_name, 
				options		=scope.config['dropdowns']['ticker'],
				index		=pos_for_previous, 
				help		='Choose a ticker. Start typing to jump down the list',
				on_change	=changed_ticker_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def changed_ticker_selection(scope, page, widget_key):
	ticker = scope[widget_key]
	logging.warning(f"changed_ticker_selection {ticker=}")

	# store the selection
	scope.page[page]['selectors']['ticker'] = ticker
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = []
	scope.page[page]['selectors']['market'] = None
	scope.page[page]['search_results'] = {}

	# Update the selected_tickers list
	if ticker != None :
		logging.critical(f'ticker Not == None {ticker=}')
		scope.page[page]['list_selected_tickers'] = [ticker]
		# update the list of tickers to load
		scope.page[page]['list_load_tickers'] = []
		already_loaded_list = list(scope.tickers.keys())
		logging.critical(already_loaded_list)
		if ticker not in already_loaded_list: 
			logging.critical('ticker NOT IN already loaded list')
			if ticker not in scope.ticker_schema['missing']['local']: # Tried and failed to load this one
				logging.critical('ticker NOT IN missing local list')
				scope.page[page]['list_load_tickers'].append(ticker)








