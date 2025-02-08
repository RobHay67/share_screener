import logging


def replace_page_df(scope, page, ticker, app_row_limit):
	logging.warning(f"replace_page_df {page=}{ticker=}")
	# Shorcut reference
	scope_ticker_page = scope.tickers[ticker][page]
	# logging.critical(f"{scope_ticker_page=}")

	# Replace the page df if requested
	if scope_ticker_page['replace_df'] == True:

		# print('Replacing the ticker[df] for > ', ticker)

		# take a copy of the original ticker dataframe
		ticker_df = scope.tickers[ticker]['df'].copy()

		# limit no of rows for the page df (speeds up page rendering)	
		ticker_df = ticker_df.head(app_row_limit)
		
		# Cache the ticker dataframe to be utilised by this page/page
		scope_ticker_page['df'] = ticker_df

		# add ticker to the loaded_ticker list
		if ticker not in scope.page[page]['list_loaded_tickers']:
			scope.page[page]['list_loaded_tickers'].append(ticker)
			scope.page[page]['replace_worklist'] = True
		
		# Set the status to false to prevent refreshing unnecesarily
		scope_ticker_page['replace_df'] = False