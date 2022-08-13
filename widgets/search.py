import streamlit as st


def search_ticker_by_name(scope):

	app = scope.apps['display_app']

	widget_key = 'widget_' + app + '_search'
	previous_selection = ''
	display_name = 'Search by Company Name'

	st.text_input(
					label		=display_name,
					value		=previous_selection,
					on_change	=search_for_ticker,
					args		=(scope, app, widget_key, ),
					key			=widget_key,
	)

	print(scope[widget_key])

def search_for_ticker(scope, app, widget_key):

	print('Triggeres search_for_ticker')

	changed_value = scope[widget_key].upper()

	# Set other selectors to their defualt values
	scope.apps[app]['selectors']['tickers'] = []
	scope.apps[app]['selectors']['industries'] = []
	scope.apps[app]['selectors']['market'] = 'select entire market'

	# Search through the ticker index for this term in the company name
	search_results = {}
	counter = 0

	for ticker, company_name in scope.ticker_search.items():
		if changed_value in company_name:
			counter += 1
			search_results[ticker] = company_name
			if counter > 9:break

	# Cache search_results
	if len(search_results) > 0:
		print('search_results = ', search_results)
		scope.apps[app]['search_results'] = search_results
		# Reset the search_ticker_by_name to blank for next search
		scope[widget_key] = ''
	else:	# No search Results
		scope.apps[app]['search_results'] = {}


def ticker_button(scope, app, ticker):

	widget_key = ticker + '_button'

	st.button(
				label='Choose', 
				key=widget_key,
				on_click=select_search_result_ticker,
				args=(scope, app, ticker, widget_key)
				)


def select_search_result_ticker(scope, app, ticker, widget_key):

	# set selected ticker as the target for the page
	if app == 'screener':
		scope.apps[app]['selectors']['tickers'] = [ticker]
	else:
		scope.apps[app]['selectors']['ticker'] = ticker

	# Clear Search Results
	scope.apps[app]['search_results'] = {}


