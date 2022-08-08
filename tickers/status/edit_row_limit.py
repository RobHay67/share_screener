



def set_data_status(scope):

	# This event is triggered when the user sets a new row limit for
	# every app - there is only a global limit
	# App dataframes will require refreshing
	# Column  adders will require refreshing as well
	print('editing the row limit')
	for ticker in scope.tickers.keys():
		for app in scope.apps['app_list']:

			scope.tickers[ticker]['apps'][app]['replace_df'] = True

			if app == 'single':
				scope.tickers[ticker]['apps'][app]['column_adders'] = scope.charts['column_adders'].copy()

			if app == 'screener':
				scope.tickers[ticker]['apps'][app]['column_adders'] = scope.trials['column_adders'].copy()















# -------------------------------------------------------------
# Set replace_df and col_adder status for ALL tickers
# -------------------------------------------------------------

# def set_replace_df_status_for_all_tickers(scope, new_status):
# 	for app in scope.apps['app_list']:
		
# 		# create new empty dictionary for status
# 		scope.apps[app]['replace_dfs'] = {}

# 		# Create a list of all possible tickers
# 		ticker_list = all_tickers_potentially_being_used_by_page(scope, app)

# 		for ticker in ticker_list:
# 			scope.apps[app]['replace_dfs'][ticker] = new_status

# 			# TODO - delete this later - just for making sure we are not doing unnecesary updates
# 			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
# 			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )


# # TODO - does not look like this one is ever called - might be easier to delete it

# def set_replace_cols_status_for_all_tickers(scope, new_status):
# 	for app in scope.apps['app_list']:
		
# 		# create new empty dictionary for status
# 		scope.apps[app]['replace_cols'] = {}

# 		# retrieve the appropriate list of col_adders
# 		config_group = 'trials' if app == 'screener' else 'charts'
# 		col_adder_template = scope.apps['templates'][config_group].copy()

# 		# Create a list of all possible tickers
# 		ticker_list = all_tickers_potentially_being_used_by_page(scope, app)

# 		for ticker in ticker_list:

# 			# add the ticker with an the template dictionary of col_adders
# 			scope.apps[app]['replace_cols'][ticker] = col_adder_template

# 			# TODO - delete this later - just for making sure we are not doing unnecesary updates
# 			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
# 			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(col_adder_template) )





def all_tickers_potentially_being_used_by_page(scope, app):
	ticker_list = []
	
	# current app working list of tickers
	for ticker in scope.apps[app]['ticker_list']:
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	# tickers in the replace_df already
	for ticker in list(scope.apps[app]['replace_dfs'].keys()):
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	# tickers in the loaded dfs for the app
	for ticker in list(scope.apps[app]['dfs'].keys()):
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	return ticker_list







