



def create_ticker_list(scope, ticker):

	# Store the selected ticker in the ticker_list for the page
	
	page = scope.pages['display_page']
	
	
	if ticker not in scope.pages[page]['ticker_list']:
		scope.pages[page]['ticker_list'].append(ticker)		

	# used for y_finance downloading
	# TODO - Rob to flesh this bit out - seems like a quick fix for the downloader
	scope.data['download']['industries'] = ['random_tickers']

				



def create_screener_ticker_list(scope):

	ticker_list = []
	relevant_industries = []

	# print(scope.pages['screener']['industries'])
	
	# ################################################################################
	# Most detailed takes precedence
	# ################################################################################

	# Selected a ticker or tickers
	if len(scope.pages['screener']['selectors']['tickers']) != 0:
		for ticker in scope.pages['screener']['selectors']['tickers']:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.pages['screener']['selectors']['industries']) != 0:
		for industry in scope.pages['screener']['selectors']['industries']:
			tickers_in_industry_df = scope.data['ticker_index'][scope.data['ticker_index']['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.pages['screener']['selectors']['market'] != 'select entire market':
		tickers_in_market = scope.data['ticker_index'].index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.data['ticker_index']['industry_group'].unique() ))
	
	
	scope.pages['screener']['ticker_list'] = ticker_list
	scope.data['download']['industries'] = relevant_industries


