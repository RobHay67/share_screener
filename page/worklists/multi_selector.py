import logging




def page_with_multiple_selectors(scope, ticker_list):
	logging.debug("_page_with_multiple_selectors")
	
	# Screener page has multiple selectors
	# - most complex selections takes precendence
	#	 ie. market trumps industry selection

	# Selected a ticker or tickers
	if len(scope.page['screener']['selectors']['tickers']) != 0:
		for ticker in scope.page['screener']['selectors']['tickers']:
			ticker_list.append(ticker)
		pass

	# Selected an Industry
	elif len(scope.page['screener']['selectors']['industries']) != 0:
		# industry_list = []
		for industry in scope.page['screener']['selectors']['industries']:
			tickers_in_industry_df = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_df.index.tolist()
			ticker_list += tickers_in_industry 
			# industry_list.append(industry)
		pass
	
	# Selected an entire share market
	elif scope.page['screener']['selectors']['market'] != 'select market':
		tickers_in_market = scope.ticker_index['df'].index.values.tolist()
		ticker_list = tickers_in_market
		# industry_list = ( list(scope.ticker_index['df']['industry_group'].unique() ))
	return ticker_list
