import streamlit as st


def search_ticker_by_name(scope):

	page = scope.pages['display']

	widget_key = 'widget_' + page + '_search'
	previous_selection = ''
	display_name = 'Search by Company Name'

	st.text_input(
					label		=display_name,
					value		=previous_selection,
					on_change	=search_for_ticker,
					args		=(scope, page, widget_key, ),
					key			=widget_key,
					help		='Enter name or part of a name and be presented with a table of companies that contain that search term',
	)


def search_for_ticker(scope, page, widget_key):

	search_string = scope[widget_key].upper()

	# Set other selectors to their defualt values
	scope.pages[page]['selectors']['tickers'] = []
	scope.pages[page]['selectors']['industries'] = []
	scope.pages[page]['selectors']['market'] = 'select market'

	# Search through the ticker index for this string in the company name
	search_results = {}
	counter = 0

	for ticker, company_name in scope.pages['ticker_search'].items():
		if search_string in company_name:
			counter += 1
			search_results[ticker] = company_name
			if counter > 9:break

	# Cache search_results
	if len(search_results) > 0:
		scope.pages[page]['search_results'] = search_results
		# Reset the search_ticker_by_name to blank for next search
		scope[widget_key] = ''
	else:	# No search Results
		scope.pages[page]['search_results'] = {}


def ticker_button(scope, page, ticker):

	widget_key = ticker + '_button'

	st.button(
				label='Choose', 
				key=widget_key,
				on_click=select_search_result_ticker,
				args=(scope, page, ticker, widget_key)
				)


def select_search_result_ticker(scope, page, ticker, widget_key):

	# set selected ticker as the target for the page
	if page == 'screener':
		scope.pages[page]['selectors']['tickers'] = [ticker]
	else:
		scope.pages[page]['selectors']['ticker'] = ticker

	# Clear Search Results
	scope.pages[page]['search_results'] = {}


