

import streamlit as st


def search_ticker_by_name(scope):

	page = scope.pages['display_page']
	widget_key = 'widget_' + page + '_search'

	st.text_input(
					label		='Search for Ticker by Company Name',
					value		='',
					on_change	=search_for_ticker,
					args		=(scope, page, widget_key, ),
					key			=widget_key,
	)


def search_for_ticker(scope, page, widget_key):


	scope.pages[page]['selectors']['ticker'] = 'select a ticker'


	search_value = scope[widget_key].upper()

	search_results = {}

	for ticker, company_name in scope.data['ticker_search'].items():
		if search_value in company_name:
			search_results[ticker] = company_name

	if len(search_results) > 0:
		scope.pages[page]['search_results'] = search_results


def ticker_button(scope, page, ticker):

	widget_key = ticker + '_button'

	select_this_ticker = st.button(
									label='Choose', 
									key=widget_key,
									on_click=choose_ticker,
									args=(scope, page, ticker, widget_key)
									)


def choose_ticker(scope, page, ticker, widget_key):
	scope.pages[page]['selectors']['ticker'] = ticker
	scope.pages[page]['search_results'] = {}

	# search_box = 'widget_' + page + '_search'
	# scope.search_box = None
	# print(scope.widget_single_search)



