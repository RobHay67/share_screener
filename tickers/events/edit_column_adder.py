




def edit_column_adder_event(scope, column_adder):

	# Event is called when one of the column adders has its
	# criteria changed - i.e. sma_days changed from 5 to 10
	# Column Adder requires a refresh for every ticker

	# default to refresh as we dont know what has been changed
	# so we should just recalculate the column adder to be sure
	status = True

	# Update where this column adder is being used
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']: 
			
			# if column adder is used by this app then change the refresh status to True
			if column_adder in scope.tickers[ticker][app]['column_adders'].keys():
				scope.tickers[ticker][app]['column_adders'][column_adder] = status


