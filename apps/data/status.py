# from audit import audit_replace_df_status


# Set the Refresh Status for 
# 	scope.apps[app][replace_df][ticker]  True = replace the entire dataframe
# 	scope.apps[app][column_adders][ticker][col_adder] True = re-run this col adder function 
# The actual df is contained in
# 	scope.apps[app][dfs]


# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE TICKER and a SINGLE app
# -------------------------------------------------------------

def set_replace_df_status_for_ticker_and_page(scope, app, ticker, new_status=False):
	scope.apps[app]['replace_dfs'][ticker] = new_status
	
	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )


def set_replace_col_adder_status_for_ticker_and_page(scope, app, ticker, col_adder, new_status):
	scope.apps[app]['replace_cols'][ticker][col_adder] = new_status

	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )




# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE ticker
# -------------------------------------------------------------

def set_replace_df_status_for_ticker(scope, ticker, new_status=True):
	# For every app, set the update_df status for this ticker
	
	# If the ticker is not in the replace_status dictionary, then add it first
	# Only attempt to do the update if the status has changed. This ensures we
	# are not doing unncesasary update

	# status is usually true exept where a share data load has failed or
	# after the ticker has actually been replaced in the app dfs object and we
	# want to prevent further updates)

	for app in scope.apps['app_list']:
		
		ticker_list = list(scope.apps[app]['replace_dfs'].keys())

		current_status = replace_df_status(scope, app, ticker_list, ticker)

		if current_status != new_status:

			# only change the status if its different to the existing status

			scope.apps[app]['replace_dfs'][ticker] = new_status

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )


def set_replace_col_status_for_ticker(scope, ticker, new_status):
	# We know which ticker needs to have its status set
	# we need a list of col_adders for this ticker on this app
	# We dont know if the ticker is in the replace_cols yet so
	# we should check for that and add a default record

	for app in scope.apps['app_list']:
		
		ticker_list = list(scope.apps[app]['replace_cols'].keys())
		config_group = 'tests' if app == 'screener' else 'charts'
		col_adder_template = scope.apps['templates'][config_group].copy()
		col_adder_list = col_adder_template.keys()

		if ticker in ticker_list:
			# col_adder_list = list(scope.apps[app]['replace_cols'][ticker].keys())

			for col_adder in col_adder_list:
				# Only change the status if the col_adder is active
				if col_adder_template[col_adder]:
					scope.apps[app]['replace_cols'][ticker][col_adder] = new_status
				else:
					# Ensure it is not active
					scope.apps[app]['replace_cols'][ticker][col_adder] = False
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )
		else:
			# add the ticker with the template dictionary of col_adders
			scope.apps[app]['replace_cols'][ticker] = col_adder_template
			
			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "] = ").ljust(80) + 'not updating')



# -------------------------------------------------------------
# Set replace_df and col_adder status for ALL tickers
# -------------------------------------------------------------

def set_replace_df_status_for_all_tickers(scope, new_status):
	for app in scope.apps['app_list']:
		
		# create new empty dictionary for status
		scope.apps[app]['replace_dfs'] = {}

		# Create a list of all possible tickers
		ticker_list = all_tickers_potentially_being_used_by_page(scope, app)

		for ticker in ticker_list:
			scope.apps[app]['replace_dfs'][ticker] = new_status

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(print_status) )


def set_replace_cols_status_for_all_tickers(scope, new_status):
	for app in scope.apps['app_list']:
		
		# create new empty dictionary for status
		scope.apps[app]['replace_cols'] = {}

		# retrieve the appropriate list of col_adders
		config_group = 'tests' if app == 'screener' else 'charts'
		col_adder_template = scope.apps['templates'][config_group].copy()

		# Create a list of all possible tickers
		ticker_list = all_tickers_potentially_being_used_by_page(scope, app)

		for ticker in ticker_list:

			# add the ticker with an the template dictionary of col_adders
			scope.apps[app]['replace_cols'][ticker] = col_adder_template

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((" - scope.apps[" + app + "]['replace_dfs'][" + ticker + "] = ").ljust(80) + str(col_adder_template) )

				
# -------------------------------------------------------------
# set col_adder status for a SINGLE col_adder function
# -------------------------------------------------------------

def set_replace_col_status_for_col_adder(scope, col_adder, new_status=True):
	# Called when one of the widgets has been changed
	# so this will be the chart or the test col_adder variables
	# we only want to make changes where the test or chart exists

	for app in scope.apps['app_list']:

		ticker_list = list(scope.apps[app]['replace_cols'].keys())

		for ticker in ticker_list:

			col_adder_list = list(scope.apps[app]['replace_cols'][ticker].keys())

			if col_adder in col_adder_list:
				status = scope.apps[app]['replace_cols'][ticker][col_adder]

			# current_status = replace_cols_status(scope, app, ticker, col_adder_list, col_adder)

				if status != new_status:
					# only change the status if its different to the existing status

					scope.apps[app]['replace_cols'][ticker][col_adder] = new_status

					# TODO - delete this later - just for making sure we are not doing unnecesary updates
					print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
					print((" - scope.apps[" + app + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(80) + str(print_status) )


# -------------------------------------------
# Helpers
# -------------------------------------------

# def replace_cols_status(scope, app, ticker, col_adder_list, col_adder):
	
# 	status = None
# 	# we know the ticker is in the replace_cols ticker_list, 
# 	# we dont know if the col_adder is in the 
# 	# ticker dictionary or whats its status currently is
# 	print( app, ticker, col_adder)
# 	print(col_adder_list)

# 	print(scope.apps[app]['replace_cols'])

# 	if col_adder in col_adder_list: 
# 		# return the status for this col_adder
# 		status = scope.apps[app]['replace_cols'][ticker][col_adder]
# 	else:
# 		# add a column adder for this ticker
# 		scope.apps[app]['replace_cols'][ticker] = [col_adder]
# 		# add set the default status
# 		scope.apps[app]['replace_cols'][ticker][col_adder] = True

# 	return status


def replace_df_status(scope, app, ticker_list, ticker):
	status = None

	if ticker in ticker_list:
		status = scope.apps[app]['replace_dfs'][ticker]
	else:
		# add a status record for this ticker
		scope.apps[app]['replace_dfs'][ticker] = status
	
	return status


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








