
def set_data_status(scope, type_col_adder, column_adder, status):

	
	# This event is triggered when a column adder is set
	# to either Active (True) or Inactive (False)
	# Column Adder requires a refresh for every ticker


	# Only column adders that have been activated require refreshing
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']: 
			
			# if the activated column adder is used by this page then change the refresh status
			if column_adder in scope.tickers[ticker]['apps'][app]['column_adders'].keys():
				scope.tickers[ticker]['apps'][app]['column_adders'][column_adder] = status

				
	# Take this opportunity to update the default column adder lists (used when adding new Tickers)
	if column_adder in scope[type_col_adder].keys():
		scope[type_col_adder]['column_adders'][column_adder] = status

