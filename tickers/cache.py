




def cache_ticker_data(scope, ticker, ticker_data):

	# This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information


	page = scope.display_page


	# Sort ticker file into ascending order
	ticker_data.sort_values(by=['date'], inplace=True, ascending=False)	

	# cache the ticker data in the primary object holder
	scope.tickers[ticker]['df'] = ticker_data	
		
	# add Column Adders for the type of page
	#  - type of column adder
	#  - and the current config template (dict of functions) 

	for page in scope.pages['page_list']:

		if page == 'chart':
			scope.tickers[ticker][page]['type_col_adder'] = 'charts'
			scope.tickers[ticker][page]['column_adders'] = scope.chart_config['column_adders'].copy()

		if page == 'screener':
			scope.tickers[ticker][page]['type_col_adder'] = 'trials'
			scope.tickers[ticker][page]['column_adders'] = scope.trial_config['column_adders'].copy()


