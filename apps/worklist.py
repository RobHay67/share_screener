
def update_app_worklist(scope):
	
	# Create a ticker list based on the selectors
	# most detailed takes precedence ie a single ticker is used, even if a user has also selected an industry

	app = scope.apps['display_app']
	ticker_list = []

	# default industry group for y_finance downloading - random_tickers = special code is run
	list_of_industries = ['random_tickers']

	if app != 'screener':
		# one of the single ticker pages
		
		selected_ticker = scope.apps[app]['selectors']['ticker']

		if selected_ticker != 'select a ticker' :
			ticker_list = [selected_ticker]
	
	else:
		# Screener app has multiple selectors

		# Selected a ticker or tickers
		if len(scope.apps['screener']['selectors']['tickers']) != 0:
			for ticker in scope.apps['screener']['selectors']['tickers']:
				ticker_list.append(ticker)
			pass

		# Selected an Industry
		elif len(scope.apps['screener']['selectors']['industries']) != 0:
			list_of_industries = []
			for industry in scope.apps['screener']['selectors']['industries']:
				tickers_in_industry_df = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
				tickers_in_industry = tickers_in_industry_df.index.tolist()
				ticker_list += tickers_in_industry 
				list_of_industries.append(industry)
			pass
		
		# Selected an entire share market
		elif scope.apps['screener']['selectors']['market'] != 'select market':
			tickers_in_market = scope.ticker_index['df'].index.values.tolist()
			ticker_list = tickers_in_market
			list_of_industries = ( list(scope.ticker_index['df']['industry_group'].unique() ))
		
	# Store the ticker_list and list_of_industries variables
	ticker_list.sort()
	scope.apps[app]['worklist'] = ticker_list
	scope.download['yf_download_these_industries'] = list_of_industries







def build_app_worklist_dropdown(scope):
	# Cloud Errors over-ride local error. If we 
	# cant download from cloud, there probably wont be
	# a local file anyway.

	app = scope.apps['display_app']
	work_list_dropdown = []

	for ticker in scope.apps[app]['worklist']:

		ticker_name = scope.config['ticker_search'][ticker]
		
		ticker_length = len(ticker)
		padding = 10 - ticker_length
		pad_string = '-'*padding
		ticker_status = ticker + pad_string

		if ticker in scope.missing_tickers['cloud']:
			ticker_status =  ticker_status + scope.missing_tickers['errors'][ticker]['yf']
		elif ticker in scope.missing_tickers['local']:
			ticker_status = ticker_status + scope.missing_tickers['errors'][ticker]['load']
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

	scope.apps[app]['worklist_dropdown'] = work_list_dropdown



















