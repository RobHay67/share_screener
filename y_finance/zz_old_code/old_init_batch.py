



def initilize_yf_config(scope, batch_no, industry):

	# Generate some lists and other parameters 
	# for yfinance to utilise during the download process

	# 		scope.yf['batch_type'] 			== 'single_ticker' or 'multiple_tickers'
	# 		scope.yf['batch_ticker_string'] == ['CBA.AX', 'NAB.AX', 'TLS.AX']
	#		scope.yf['batch_no']			== passed in batch_no (iterator)
	# 		scope.yf['batch_industry']		== passed in industry (List set by page)


	# convert an industry into a string of tickers acceptable to y_finance
	# store the batch download params
	scope.yf['batch_no'] = batch_no
	scope.yf['batch_industry'] = industry

	print('Batch Number 	= ', batch_no)
	print('Batch Industry 	= ', industry)
	
	if industry == 'random_tickers':
		# Selected specific tickers rather than by industry group					 
		page = scope.pages['display']
		ticker_list = scope.pages[page]['worklist']
	else:
		# selected a share market, an industry or multiple industries
		industry_tickers = scope.ticker_index['df'][scope.ticker_index['df']['industry_group'] == industry ]
		ticker_list = industry_tickers.index.tolist()

	# Create a readable list of the tickers for Y_Finance
	y_finance_ticker_string = ""
	for ticker in ticker_list:
		if len(y_finance_ticker_string) != 0:
			y_finance_ticker_string += " "
		y_finance_ticker_string =  y_finance_ticker_string + ticker

	scope.yf['batch_ticker_string'] = y_finance_ticker_string

	# Set type of download for y_finance - single or multiple tickers
	if y_finance_ticker_string.count(' ') == 0:
		scope.yf['batch_type'] = 'single_ticker'
	else:
		scope.yf['batch_type'] = 'multiple_tickers'


