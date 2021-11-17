






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
	if len(scope.selected['multi']['tickers']) != 0:
		for ticker in scope.selected['multi']['tickers']:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.selected['multi']['industries']) != 0:
		for industry in scope.selected['multi']['industries']:
			tickers_in_industry_df = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.selected['multi']['market'] != 'select entire market':
		tickers_in_market = scope.ticker_index.index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.ticker_index['industry_group'].unique() ))
	
	scope.selected['multi']['ticker_list'] = ticker_list
	scope.download_industries = relevant_industries




