from audit import audit_replace_df_status


#
# Set the Refresh Status for 
# 	scope.pages[page][replace_df][ticker]  True = replace the entire dataframe
# 	scope.pages[page][column_adders][ticker][col_adder] True = re-run this col adder function 
# The actual df is contained in
# 	scope.pages[page][dfs]


# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE TICKER and a SINGLE PAGE
# -------------------------------------------------------------

def set_replace_df_status_for_ticker_and_page(scope, page, ticker, new_status=False, caller='unknown'):

	scope.pages[page]['replace_df'][ticker] = new_status
	
	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((caller + " - scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(print_status) )


def set_replace_col_adder_status_for_ticker_and_page(scope, page, ticker, col_adder, new_status, caller='unknown'):

	scope.pages[page]['replace_cols'][ticker][col_adder] = new_status
	# TODO - delete this later - just for making sure we are not doing unnecesary updates
	print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
	print((caller + " - scope.pages[" + page + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )




# -------------------------------------------------------------
# Set replace_df and col_adder status for a SINGLE ticker
# -------------------------------------------------------------

def set_replace_df_status_for_ticker(scope, ticker, new_status=True, caller='unknown'):
	
	# For every page, set the update_df status for this ticker
	
	# If the ticker is not in the replace_status dictionary, then add it first
	# Only attempt to do the update if the status has changed. This ensures we
	# are not doing unncesasary update

	# status is usually true exept where a share data load has failed or
	# after the ticker has actually been replaced in the page dfs object and we
	# want to prevent further updates)

	for page in scope.pages['page_list']:
		
		ticker_list = list(scope.pages[page]['replace_df'].keys())

		current_status = replace_df_status(scope, page, ticker_list, ticker)

		if current_status != new_status:

			# only change the status if its different to the existing status

			scope.pages[page]['replace_df'][ticker] = new_status

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((caller + " - scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(print_status) )


# def set_replace_col_adder_status_for_ticker(scope, page, ticker, new_status, caller='unknown'):
def set_replace_col_adder_status_for_ticker(scope, ticker, new_status, caller='unknown'):

	# We know which ticker needs to have its status set
	# we need a list of col_adders for this ticker on this page
	# We dont know if the ticker is in the replace_cols yet so
	# we should check for that and add a default record

	for page in scope.pages['page_list']:
		
		ticker_list = list(scope.pages[page]['replace_cols'].keys())

		if ticker in ticker_list:
			col_adder_list = list(scope.pages[page]['replace_cols'][ticker].keys())

			for col_adder in col_adder_list:
				scope.pages[page]['replace_cols'][ticker][col_adder] = new_status

			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((caller + " - scope.pages[" + page + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )
		else:
			# add the ticker with an the template dictionary of col_adders
			config_group = 'tests' if page == 'screener' else 'charts'
			col_adder_template = scope.pages['templates'][config_group].copy()
			scope.pages[page]['replace_cols'][ticker] = col_adder_template
			
			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print((caller + " - scope.pages[" + page + "]['replace_cols'][" + ticker + "] = ").ljust(90) + str(col_adder_template) )





# -------------------------------------------------------------
# Set replace_df and col_adder status for ALL tickers
# -------------------------------------------------------------

def set_replace_df_status_for_all_tickers(scope, new_status, caller='unknown'):
	for page in scope.pages['page_list']:
		
		# create new empty dictionary for status
		scope.pages[page]['replace_df'] = {}

		# Create a list of all possible tickers
		ticker_list = all_tickers_potentially_being_used_by_page(scope, page)

		for ticker in ticker_list:
			scope.pages[page]['replace_df'][ticker] = new_status

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((caller + " - scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(print_status) )


def set_replace_cols_status_for_all_tickers(scope, new_status, caller='unknown'):
	for page in scope.pages['page_list']:
		
		# create new empty dictionary for status
		scope.pages[page]['replace_cols'] = {}

		# retrieve the appropriate list of col_adders
		config_group = 'tests' if page == 'screener' else 'charts'
		col_adder_template = scope.pages['templates'][config_group].copy()

		# Create a list of all possible tickers
		ticker_list = all_tickers_potentially_being_used_by_page(scope, page)

		for ticker in ticker_list:

			# add the ticker with an the template dictionary of col_adders
			scope.pages[page]['replace_cols'][ticker] = col_adder_template

			# TODO - delete this later - just for making sure we are not doing unnecesary updates
			print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
			print((caller + " - scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(col_adder_template) )

				
# -------------------------------------------------------------
# set col_adder status for a SINGLE col_adder function
# -------------------------------------------------------------

def set_replace_col_status_for_col_adder(scope, col_adder, new_status=True, caller='unknown'):


	for page in scope.pages['page_list']:

		ticker_list = list(scope.pages[page]['replace_cols'].keys())

		for ticker in ticker_list:

			col_adder_list = list(scope.pages[page]['replace_cols']['ticker'].keys())

			current_status = replace_cols_status(scope, page, ticker, col_adder_list, col_adder)

			if current_status != new_status:
				# only change the status if its different to the existing status

				scope.pages[page]['replace_cols'][ticker][col_adder] = new_status

				# TODO - delete this later - just for making sure we are not doing unnecesary updates
				print_status = '\033[91m' + str(new_status) + '\033[0m' if new_status == True else  '\033[92m' + str(new_status) + '\033[0m'
				print((caller + " - scope.pages[" + page + "]['replace_cols'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )


# -------------------------------------------
# Helpers
# -------------------------------------------

def replace_cols_status(scope, page, ticker, col_adder_list, col_adder):
	
	status = None
	# we know the ticker is in the replace_cols ticker_list, 
	# we dont know if the col_adder is in the 
	# ticker dictionary or whats its status currently is
	
	if col_adder in col_adder_list: 
		# return the status for this col_adder
		status = scope.pages[page]['replace_cols'][ticker][col_adder]
	else:
		# add a column adder for this ticker
		scope.pages[page]['replace_cols'][ticker] = [col_adder]
		# add set the default status
		scope.pages[page]['replace_cols'][ticker][col_adder] = True

	return status


def replace_df_status(scope, page, ticker_list, ticker):

	status = None

	if ticker in ticker_list:
		status = scope.pages[page]['replace_df'][ticker]
	else:
		# add a status record for this ticker
		scope.pages[page]['replace_df'][ticker] = status
	
	return status


def all_tickers_potentially_being_used_by_page(scope, page):
	ticker_list = []
	
	# current page working list of tickers
	for ticker in scope.pages[page]['ticker_list']:
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	# tickers in the replace_df already
	for ticker in list(scope.pages[page]['replace_df'].keys()):
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	# tickers in the loaded dfs for the page
	for ticker in list(scope.pages[page]['dfs'].keys):
		if ticker not in ticker_list:
			ticker_list.append(ticker)

	return ticker_list








