#TODO - delete later

from audit import audit_replace_df_status

# 	scope.pages[page][dfs]	contains the appropriate dataframes for the page
#
# Set the Refresh Status for 
# - scope.pages[page][replace_df][ticker]  True = replace the entire dataframe
# - scope.pages[page][column_adders][ticker][col_adder] True = re-run this col adder function 


def set_replace_df_status(scope, tickers='all', df_replace_status=True, caller='unknown'):

	for page in scope.pages['page_list']:
		replace_df_keys = list(scope.pages[page]['replace_df'].keys())
		ticker_list = replace_df_keys if tickers == 'all' else [tickers]

		for ticker in ticker_list:
			current_status = None
			if ticker in replace_df_keys:
				current_status = scope.pages[page]['replace_df'][ticker]

			# only change the status if its different to whats already recorded
			# This will prevent unnecesary updates and changes
			if current_status != df_replace_status:
				
				scope.pages[page]['replace_df'][ticker] = df_replace_status

				print_status = '\033[91m' + str(df_replace_status) + '\033[0m' if df_replace_status == True else  '\033[92m' + str(df_replace_status) + '\033[0m'
				print((caller + " - scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(print_status) )

				# set_rerun_col_adder_status(scope, tickers=ticker, column_adders='all', re_run_status=df_replace_status, caller='set_replace_df_status' )
				set_add_cols_for_ticker(scope, ticker, caller='set_replace_df_status')
				# problem here is that



def set_add_cols_for_ticker(scope, ticker, caller='unkown'):
	# For a specific ticker, set all add_cols to the default template active values

	for page in scope.pages['page_list']:
		ticker_list = list(scope.pages[page]['column_adders'].keys())
		config_group = 'tests' if page == 'screener' else 'charts'
		col_adder_template = scope.pages['templates'][config_group].copy()
		col_adder_list = list(col_adder_template.keys())
		existing_col_adders = []

		# Ensure we have a dictionary
		if ticker not in ticker_list:
			scope.pages[page]['column_adders'][ticker] = {}	
		else:
			existing_col_adders = list(scope.pages[page]['column_adders'][ticker].keys())

		for col_adder in col_adder_list:
			current_status = None
			revised_status = col_adder_template[col_adder]
		
			if col_adder in existing_col_adders:
				current_status = scope.pages[page]['column_adders'][ticker][col_adder]

			if current_status != revised_status:

				scope.pages[page]['column_adders'][ticker][col_adder] = revised_status

				print_status = '\033[91m' + str(revised_status) + '\033[0m' if revised_status == True else  '\033[92m' + str(revised_status) + '\033[0m'
				print((caller + " - scope.pages[" + page + "]['column_adders'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )



def set_add_cols_status(scope, column_adder, run_status=True, caller='unknown'):
	# A single column adder has changed and needs its status changed for every instance

	for page in scope.pages['page_list']:
		# dfs_loaded_for_page = list(scope.pages[page]['dfs'].keys())
		ticker_list = list(scope.pages[page]['column_adders'].keys())

		for ticker in ticker_list:
			# CBA
			column_adders_for_ticker = scope.pages[page]['column_adders'][ticker].keys()
			# trend_open

			current_status = None
			if column_adder in column_adders_for_ticker:
				# its already - so whats its stauts
				current_status = scope.pages[page]['column_adders'][ticker][column_adder]

			# only change the status if its different to whats already recorded
			# This will prevent unnecesary updates and changes
			if current_status != run_status:
				scope.pages[page]['column_adders'][ticker][column_adder] = run_status

				print_status = '\033[91m' + str(run_status) + '\033[0m' if run_status == True else  '\033[92m' + str(run_status) + '\033[0m'
				print((caller + " - scope.pages[" + page + "]['column_adders'][" + ticker + "][" + column_adder + "] = ").ljust(90) + str(print_status) )







# def set_rerun_col_adder_status(scope, tickers='all', column_adders='all', re_run_status=True, caller='unknown' ):
# 	# width=70
# 	# print('='*width)
# 	# print('\033[95mset_rerun_col_adder_status\033[0m', '\033[96mcaller = ' + caller + '\033[0m')
# 	print('tickers = ', tickers, 'column_adders = ', column_adders, 're_run_status = ', re_run_status)
# 	# print('-'*width)

# 	# Always update for Every Page
# 	for page in scope.pages['page_list']:

# 		ticker_list = list(scope.pages[page]['column_adders'].keys()) if tickers == 'all' else [tickers]

# 		config_group = 'tests' if page == 'screener' else 'charts'
		
# 		for ticker in ticker_list: 
# 			print(ticker)

# 			# Use the active status template for the config_group (it has the active status)
# 			col_adder_template = scope.pages['templates'][config_group].copy()	
		
# 			if column_adders=='all':
# 				# Every col_adder requires a data refresh																		
# 				scope.pages[page]['column_adders'][ticker] = col_adder_template

# 				for col_adder, status in col_adder_template.items():
# 					print_status = '\033[91m' + str(status) + '\033[0m' if status == True else  '\033[92m' + str(status) + '\033[0m'
# 					print((caller + " - scope.pages[" + page + "]['column_adders'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )
# 			else:
# 				# A single col_adder requires a data refresh
# 				scope.pages[page]['column_adders'][ticker][column_adders] = re_run_status

# 				print_status = '\033[91m' + str(re_run_status) + '\033[0m' if re_run_status == True else  '\033[92m' + str(re_run_status) + '\033[0m'	
# 				print((caller + " - scope.pages[" + page + "]['column_adders'][" + ticker + "][" + column_adders + "] = ").ljust(90) + str(print_status) )










# def set_page_status(scope, tickers='all', replace_df=False, column_adders=None, renew_status=True, caller='unknown' ):

# 	# renew_status = Usually True, but when downloading we sometime 
# 	# need to turn the replace off, if the download fails
# 	width=70
# 	print('='*width)
# 	print('\033[95mSetting Page status\033[0m', '\033[96mcaller = ' + caller + '\033[0m')
# 	print('tickers = ', tickers, 'replace_df = ', replace_df, 'renew_status = ', renew_status, 'column_adders = ', column_adders,)
# 	print('-'*width)

# 	audit_replace_df_status(scope, 'Before set_page_status')	
# 	for page in scope.pages['page_list']:

# 		# Establish list of tickers for this page (streamline the whole function)
# 		df_ticker_list, col_add_ticker_list = list_of_tickers_for_page(scope, page, tickers)

		
# 		if replace_df:
# 			for ticker in df_ticker_list:
# 				# print(ticker)
# 				scope.pages[page]['replace_df'][ticker] = renew_status

# 				print_status = '\033[91m' + str(renew_status) + '\033[0m' if renew_status == False else  '\033[92m' + str(renew_status) + '\033[0m'
# 				print(("scope.pages[" + page + "]['replace_df'][" + ticker + "] = ").ljust(90) + str(print_status) )
		
	


# 		if column_adders != None:
# 			config_group = 'tests' if page == 'screener' else 'charts'
			
# 			for ticker in col_add_ticker_list: 

# 				# Use the active status template for the config_group (it has the active status)
# 				col_adder_template = scope.pages['templates'][config_group].copy()	
			
# 				if column_adders=='all':
# 					# Every col_adder requires a data refresh																		
# 					scope.pages[page]['column_adders'][ticker] = col_adder_template

# 					for col_adder, status in col_adder_template.items():
# 						print_status = '\033[91m' + str(status) + '\033[0m' if status == False else  '\033[92m' + str(status) + '\033[0m'
# 					# 	print(("scope.pages[" + page + "]['column_adders'][" + ticker + "][" + col_adder + "] = ").ljust(90) + str(print_status) )
# 				else:
# 					# A single col_adder requires a data refresh
# 					print_status = '\033[91m' + str(renew_status) + '\033[0m' if renew_status == False else  '\033[92m' + str(renew_status) + '\033[0m'						
# 					scope.pages[page]['column_adders'][ticker][column_adders] = renew_status
# 					# print(("scope.pages[" + page + "]['column_adders'][" + ticker + "][" + column_adders + "] = ").ljust(90) + str(print_status) )

# 	audit_replace_df_status(scope, 'After set_page_status')

# def list_of_tickers_for_page(scope, page, tickers):
# 	if tickers == 'all':
# 		df_ticker_list = list(scope.pages[page]['replace_df'].keys())
# 		col_add_ticker_list = list(scope.pages[page]['column_adders'].keys())
# 	else:
# 		# A single ticker has been provided so return this single ticker in a list
# 		df_ticker_list = [tickers]
# 		col_add_ticker_list = [tickers]

# 	return df_ticker_list, col_add_ticker_list



