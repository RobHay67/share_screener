
def update_page_worklist(scope):
	
	# Create a ticker list based on the selectors
	# most detailed takes precedence ie a single ticker is used, even if a user has also selected an industry

	page = scope.pages['display']
	ticker_list = []

	# default industry group for y_finance downloading - random_tickers = special code is run
	list_of_industries = ['random_tickers']

	if page != 'screener':
		# one of the single ticker pages
		
		selected_ticker = scope.pages[page]['selectors']['ticker']

		if selected_ticker != 'select a ticker' :
			ticker_list = [selected_ticker]
	
	else:
		# Screener page has multiple selectors

		# Selected a ticker or tickers
		if len(scope.pages['screener']['selectors']['tickers']) != 0:
			for ticker in scope.pages['screener']['selectors']['tickers']:
				ticker_list.append(ticker)
			pass

		# Selected an Industry
		elif len(scope.pages['screener']['selectors']['industries']) != 0:
			list_of_industries = []
			for industry in scope.pages['screener']['selectors']['industries']:
				tickers_in_industry_df = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
				tickers_in_industry = tickers_in_industry_df.index.tolist()
				ticker_list += tickers_in_industry 
				list_of_industries.append(industry)
			pass
		
		# Selected an entire share market
		elif scope.pages['screener']['selectors']['market'] != 'select market':
			tickers_in_market = scope.ticker_index['df'].index.values.tolist()
			ticker_list = tickers_in_market
			list_of_industries = ( list(scope.ticker_index['df']['industry_group'].unique() ))
		
	# Store the ticker_list and list_of_industries variables
	ticker_list.sort()
	scope.pages[page]['worklist'] = ticker_list
	scope.yf['download_these_industries'] = list_of_industries







def build_app_worklist_dropdown(scope):
	# Cloud Errors over-ride local error. If we 
	# cant download from cloud, there probably wont be
	# a local file anyway.

	page = scope.pages['display']
	work_list_dropdown = []

	for ticker in scope.pages[page]['worklist']:

		ticker_name = scope.config['ticker_search'][ticker]
		
		ticker_length = len(ticker)
		padding = 10 - ticker_length
		pad_string = '-'*padding
		ticker_status = ticker + pad_string

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

	scope.pages[page]['worklist_dropdown'] = work_list_dropdown



















