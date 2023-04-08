from trials.remove_test_result import remove_test_result_column



def edit_active_event(scope, type_col_adder, column_adder, status):
	
	# This event is triggered when a column adder is set
	# to either Active (True) or Inactive (False)
	# Column Adder requires a refresh for every ticker
	# Only column adders that have been activated will require refreshing
	
	for ticker in scope.tickers.keys():
		for page in scope.pages['page_list']: 
			# if the activated column adder is used by this page then change the refresh status
			if column_adder in scope.tickers[ticker][page]['column_adders'].keys():
				scope.tickers[ticker][page]['column_adders'][column_adder] = status
				# for the screener page, remove the test result 
				# if the users has deactivated this test
				if page == 'screener' and status == False:
					remove_test_result_column(scope, ticker, column_adder)


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
