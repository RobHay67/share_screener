

# ==============================================================================================================================================================
# Ticker List for Multi Ticker Analysis : Construct and Quick Show
# ==============================================================================================================================================================
def update_multi_ticker_list(scope):
	
	ticker_list = []
	relevant_industries = []
	
	# ################################################################################
	# Most detailed takes precedence
	# ################################################################################

	# Selected a ticker or tickers
	if len(scope.tickers_multi) != 0:
		for ticker in scope.tickers_multi:
			ticker_list.append(ticker)
			relevant_industries = ['random_tickers']
		pass
	# Selected an Industry
	elif len(scope.tickers_industries) != 0:
		for industry in scope.tickers_industries:
			tickers_in_industry_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			relevant_industries.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.tickers_market != 'select entire market':
		tickers_in_market = scope.ticker_index_file.index.values.tolist()
		ticker_list = tickers_in_market
		relevant_industries = ( list(scope.ticker_index_file['industry_group'].unique() ))
	
	scope.ticker_list['multi'] = ticker_list
	scope.download_industries = relevant_industries