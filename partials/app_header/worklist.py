
def update_app_worklist(scope):
	
	# Create a ticker list based on the selectors
	# most detailed takes precedence ie a single ticker is used, even if a user has also selected an industry

	app = scope.apps['display_app']
	ticker_list = []
	we_have_selected_tickers = False

	# default industry group for y_finance downloading - random_tickers = special code is run
	list_of_industries = ['random_tickers']

	if app != 'screener':
		# one of the single ticker pages
		
		selected_ticker = scope.apps[app]['selectors']['ticker']

		if selected_ticker != 'select a ticker' :
			we_have_selected_tickers = True		
			ticker_list = [selected_ticker]
	
	else:
		# Screener app has multiple selectors

		# Selected a ticker or tickers
		if len(scope.apps['screener']['selectors']['tickers']) != 0:
			we_have_selected_tickers = True
			for ticker in scope.apps['screener']['selectors']['tickers']:
				ticker_list.append(ticker)
			pass

		# Selected an Industry
		elif len(scope.apps['screener']['selectors']['industries']) != 0:
			we_have_selected_tickers = True
			list_of_industries = []
			for industry in scope.apps['screener']['selectors']['industries']:
				tickers_in_industry_df = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
				tickers_in_industry = tickers_in_industry_df.index.tolist()
				ticker_list += tickers_in_industry 
				list_of_industries.append(industry)
			pass
		
		# Selected an entire share market
		elif scope.apps['screener']['selectors']['market'] != 'select entire market':
			we_have_selected_tickers = True
			tickers_in_market = scope.ticker_index.index.values.tolist()
			ticker_list = tickers_in_market
			list_of_industries = ( list(scope.ticker_index['industry_group'].unique() ))
		
	# Store the ticker_list and list_of_industries variables
	ticker_list.sort()
	scope.apps[app]['worklist'] = ticker_list
	scope.download['yf_download_these_industries'] = list_of_industries

	return we_have_selected_tickers