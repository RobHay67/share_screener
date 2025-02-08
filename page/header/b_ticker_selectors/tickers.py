import logging
import streamlit as st



def select_tickers(scope):
	logging.debug("select_tickers")
	page = scope.display['page']
	
	widget_key = 'widget_' + page + '_select_tickers'
	previous_selection = scope.page[page]['selectors']['tickers']
	display_name = 'Ticker(s)'

	st.multiselect ( 
				label		=display_name,
				options		=scope.config['dropdowns']['tickers'],
				default		=previous_selection, 
				help		='Select a ticker, or multiple tickers from the dropdown. Start typing to jump within list',
				on_change	=changed_tickers_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def changed_tickers_selection(scope, page, widget_key):
	logging.warning("changed_tickers_selection")
	selected_tickers = scope[widget_key]
	# store the selection
	scope.page[page]['selectors']['ticker'] = None
	scope.page[page]['selectors']['tickers'] = selected_tickers
	scope.page[page]['selectors']['industries'] = []
	scope.page[page]['selectors']['market'] = None
	scope.page[page]['search_results'] = {}

	# Update the selected_tickers list
	tickers_list = []
	for ticker in selected_tickers:
		tickers_list.append(ticker)
	tickers_list.sort()
	scope.page[page]['list_selected_tickers'] = tickers_list

	# update the list of tickers to load
	scope.page[page]['list_load_tickers'] = []
	already_loaded_list = list(scope.tickers.keys())
	if ticker not in already_loaded_list:
		if ticker not in scope.ticker_schema['missing']['local']: # Tried and failed to load this one
			scope.page[page]['list_load_tickers'].append(ticker)