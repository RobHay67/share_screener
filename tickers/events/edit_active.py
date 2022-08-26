
def edit_active_event(scope, type_col_adder, column_adder, status):
	
	# This event is triggered when a column adder is set
	# to either Active (True) or Inactive (False)
	# Column Adder requires a refresh for every ticker


	# Only column adders that have been activated will require refreshing
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']: 
			
			# if the activated column adder is used by this page then change the refresh status
			if column_adder in scope.tickers[ticker][app]['column_adders'].keys():
				scope.tickers[ticker][app]['column_adders'][column_adder] = status

				
	# Take this opportunity to update the shortcut lists
	#  - column_adders - list of trials that add columns to a dataframe
	#  - active_trials - list of trials that are currently active

	if type_col_adder == 'trials':
		type_config = 'trial_config'

	if type_col_adder == 'charts':
		type_config = 'chart_config'
	
	if column_adder in scope[type_col_adder].keys():
		# restict to functions that add columns
		if scope[type_col_adder][column_adder]['add_columns'] != None:
			scope[type_config]['column_adders'][column_adder] = status

	if status == True:
		scope[type_config]['active_list'].append(column_adder)
	else:
		if column_adder in scope[type_config]['active_list']:
			scope[type_config]['active_list'].remove(column_adder)
