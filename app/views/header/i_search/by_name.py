import streamlit as st


def search_ticker_by_name(scope):

	page = scope.display['page']

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
	scope.page[page]['selectors']['tickers'] = []
	scope.page[page]['selectors']['industries'] = []
	scope.page[page]['selectors']['market'] = 'select market'

	# Search through the ticker index for this string in the company name
	search_results = {}
	counter = 0

	for ticker, company_name in scope.config['ticker_search'].items():
		if search_string in company_name:
			counter += 1
			search_results[ticker] = company_name
			if counter > 9:break

	# Cache search_results
	if len(search_results) > 0:
		scope.page[page]['search_results'] = search_results
		# Reset the search_ticker_by_name to blank for next search
		scope[widget_key] = ''
	else:	# No search Results
		scope.page[page]['search_results'] = {}