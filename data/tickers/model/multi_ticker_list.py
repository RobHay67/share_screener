






# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# Multi Page - Ticker List Constructor
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def update_multi_ticker_list(scope):
	
	ticker_list = []
	relevant_industries = []
	
	# ################################################################################
	# Most detailed takes precedence
	# ################################################################################

	# Selected a ticker or tickers
	if len(scope.pages['screener']['tickers']) != 0:
		for ticker in scope.pages['screener']['tickers']:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.pages['screener']['industries']) != 0:
		for industry in scope.pages['screener']['industries']:
			tickers_in_industry_df = scope.data['ticker_index'][scope.data['ticker_index']['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.pages['screener']['market'] != 'select entire market':
		tickers_in_market = scope.data['ticker_index'].index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.data['ticker_index']['industry_group'].unique() ))
	
	scope.pages['screener']['ticker_list'] = ticker_list
	scope.data['download']['industries'] = relevant_industries




