

import streamlit as st


def search_ticker_by_name(scope):

	app = scope.apps['display_app']
	widget_key = 'widget_' + app + '_search'

	st.text_input(
					label		='Search by Company Name',
					value		='',
					on_change	=search_for_ticker,
					args		=(scope, app, widget_key, ),
					key			=widget_key,
	)


def search_for_ticker(scope, app, widget_key):

	scope.apps[app]['selectors']['ticker'] = 'select a ticker'


	search_value = scope[widget_key].upper()

	search_results = {}
	counter = 0

	for ticker, company_name in scope.ticker_search.items():
		if search_value in company_name:
			counter += 1
			search_results[ticker] = company_name
			if counter > 9: break

	if len(search_results) > 0:
		scope.apps[app]['search_results'] = search_results
	else:
		scope.apps[app]['search_results'] = {}


def ticker_button(scope, app, ticker):

	widget_key = ticker + '_button'

	select_this_ticker = st.button(
									label='Choose', 
									key=widget_key,
									on_click=choose_ticker,
									args=(scope, app, ticker, widget_key)
									)


def choose_ticker(scope, app, ticker, widget_key):

	if app == 'screener':
		scope.apps[app]['selectors']['tickers'] = [ticker]
	else:
		scope.apps[app]['selectors']['ticker'] = ticker
	
	scope.apps[app]['search_results'] = {}

	# search_box = 'widget_' + app + '_search'
	# scope.search_box = None
	# print(scope.widget_single_search)



