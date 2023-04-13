




def replace_page_df(scope, page, ticker, app_row_limit):
	# Replace the page df if requested

	if scope.tickers[ticker][page]['replace_df'] == True:
		ticker_df = scope.tickers[ticker]['df'].copy()
		# limit no of rows for the page df (speeds up page rendering)	
		ticker_df = ticker_df.head(app_row_limit)
		
		# Cache the ticker dataframe to be utilised by this page/page
		scope.tickers[ticker][page]['df'] = ticker_df

		if ticker not in scope.pages[page]['tickers_used_by_page']:
		# add ticker to the loaded_ticker list
			scope.pages[page]['tickers_used_by_page'].append(ticker)
		
		# Set the status to false to prevent refreshing unnecesarily
		scope.tickers[ticker][page]['replace_df'] = False