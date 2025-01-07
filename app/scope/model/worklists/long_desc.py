


def refresh_worklist_long_description(scope):
	# Cloud Errors over-ride local error. If we 
	# cant download from cloud, there probably wont be
	# a local file anyway.

	page = scope.config['display']
	work_list_dropdown = []

	for ticker in scope.page[page]['worklist']:

		ticker_name = scope.config['ticker_search'][ticker]
		
		ticker_length = len(ticker)
		padding = 10 - ticker_length
		pad_string = '-'*padding
		ticker_status = ticker + pad_string

		print('refresh_worklist_long_description > ', scope.tickers_missing['cloud'])

		if ticker in scope.tickers_missing['cloud']:
			ticker_status =  ticker_status + scope.tickers_missing['errors'][ticker]['yf']
		elif ticker in scope.tickers_missing['local']:
			ticker_status = ticker_status + scope.tickers_missing['errors'][ticker]['load']
		else:
			if ticker in list(scope.tickers.keys()): 
				ticker_df = scope.tickers[ticker]['df']

				no_of_rows = ' (' + str(len(ticker_df)) +') '
				# Date Range
				min_date = ticker_df['date'].min()
				max_date = ticker_df['date'].max()
				min_date = str(min_date.strftime("%d-%b-%Y"))
				max_date = str(max_date.strftime("%d-%b-%Y"))

				ticker_status = ticker_status + min_date + ' < > ' + max_date + no_of_rows + ' rows ---' + ' ' + ticker_name
			else:
				ticker_status = ticker_status + 'not loaded'
		
		work_list_dropdown.append(ticker_status)
	
	work_list_dropdown.insert(0, 'Show/Hide Data')

	scope.page[page]['worklist_long_desc'] = work_list_dropdown

	