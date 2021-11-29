


from config.initial_scope.markets import markets




def update_dropdowns(scope):
	print ( '\033[91m' + 'Dropdown Lists have been repopulated' + '\033[0m' )

	scope.dropdown_ohlcv_columns 	= ['open', 'high', 'low', 'close', 'volume']
	scope.dropdown_price_columns 	= ['open', 'high', 'low', 'close' 			]


	
	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, 'select entire market')
	scope.dropdown_markets = list_of_markets
	
	list_of_industries = scope.ticker_index['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.dropdown_industries = list_of_industries
	
	list_of_tickers = scope.ticker_index.index.values.tolist()
	scope.dropdown_tickers = list_of_tickers

	alt_ticker_list = scope.ticker_index.index.values.tolist()
	alt_ticker_list.insert(0, 'select a ticker')
	scope.dropdown_ticker = alt_ticker_list
	
	# ---------------------------------------------------------------------------------------
	# Prevent executing this function again (until changes have been made to the share index)
	scope.dropdown_lists_need_updating = False
	

