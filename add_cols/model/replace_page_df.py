




def replace_page_df(scope, page, ticker, app_row_limit):
	
	# Shorcut reference
	ticker_for_page = scope.tickers[ticker][page]

	# Replace the page df if requested
	if ticker_for_page['replace_df'] == True:

		# take a copy of the original ticker dataframe
		ticker_df = scope.tickers[ticker]['df'].copy()

		# limit no of rows for the page df (speeds up page rendering)	
		ticker_df = ticker_df.head(app_row_limit)
		
		# Cache the ticker dataframe to be utilised by this page/page
		ticker_for_page['df'] = ticker_df

		# add ticker to the loaded_ticker list
		if ticker not in scope.page[page]['loaded_ticker_list']:
			scope.page[page]['loaded_ticker_list'].append(ticker)
		
		# Set the status to false to prevent refreshing unnecesarily
		ticker_for_page['replace_df'] = False