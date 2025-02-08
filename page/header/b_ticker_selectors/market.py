import logging
import streamlit as st





def select_a_market(scope):
	logging.debug("select_a_market")
	page = scope.display['page']
	
	widget_key = 'widget_' + page + '_select_market'
	previous_selection = scope.page[page]['selectors']['market']
	if previous_selection != None:
		pos_for_previous = scope.config['dropdowns']['markets'].index(previous_selection)	
	else:
		pos_for_previous = None

	st.selectbox ( 
				label		='Market',
				options		=scope.config['dropdowns']['markets'],
				index		=pos_for_previous, 
				help		='Select an Entire Share Market for Analysis',
				on_change	=changed_market_selection,
				args		=(scope, page, widget_key, ),
				key			=widget_key,
				) 


def changed_market_selection(scope, page, widget_key):
	logging.warning("on_change_market_selection")
	stock_market = scope[widget_key]

	# store the selection
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = []
	scope.page[page]['selectors']['market'] = stock_market
	scope.page[page]['search_results'] = {}

	# Selected an entire share market
	tickers_in_market = scope.ticker_index['df'].index.values.tolist()
	tickers_in_market.sort()
	scope.page[page]['list_selected_tickers'] = tickers_in_market

	logging.error("changed_market_selection have not updated the list of tickers to download")