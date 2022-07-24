
def update_ticker_list(scope):
	
	# Create a ticker list based on the selectors
	# most detailed takes precedence ie a single ticker is used, even if a user has also selected an industry

	page = scope.pages['display_page']
	ticker_list = []
	selected_tickers_status = False

	# default industry group for y_finance downloading - random_tickers = special code is run
	list_of_industries = ['random_tickers']

	if page != 'screener':
		# one of the single ticker pages
		
		selected_ticker = scope.pages[page]['selectors']['ticker']

		if selected_ticker != 'select a ticker' :
			selected_tickers_status = True		
			ticker_list = [selected_ticker]
	
	else:
		# Screener page has multiple selectors

		# Selected a ticker or tickers
		if len(scope.pages['screener']['selectors']['tickers']) != 0:
			selected_tickers_status = True
			for ticker in scope.pages['screener']['selectors']['tickers']:
				ticker_list.append(ticker)
			pass

		# Selected an Industry
		elif len(scope.pages['screener']['selectors']['industries']) != 0:
			selected_tickers_status = True
			list_of_industries = []
			for industry in scope.pages['screener']['selectors']['industries']:
				tickers_in_industry_df = scope.data['ticker_index'][scope.data['ticker_index']['industry_group'] == industry ]
				tickers_in_industry = tickers_in_industry_df.index.tolist()
				ticker_list += tickers_in_industry 
				list_of_industries.append(industry)
			pass
		
		# Selected an entire share market
		elif scope.pages['screener']['selectors']['market'] != 'select entire market':
			selected_tickers_status = True
			tickers_in_market = scope.data['ticker_index'].index.values.tolist()
			ticker_list = tickers_in_market
			list_of_industries = ( list(scope.data['ticker_index']['industry_group'].unique() ))
		
	# Store the ticker_list and list_of_industries variables
	scope.pages[page]['ticker_list'] = ticker_list
	scope.data['download']['industries'] = list_of_industries

	return selected_tickers_status