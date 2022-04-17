
# TODO - confirm we need these libraries


# from pages.screener.model.tests import store_test_results
from pages.screener.model.tests import screener_all_active_test_results
from config.tests.results import create_test_result_summary


def renew_pages_dfs(scope):
	
	page 				= scope.pages['display_page']
	page_row_limit 		= int(scope.pages['row_limit'])
	page_ticker_list 	= scope.pages[page]['ticker_list']
	config_group		= 'tests' if page == 'screener' else 'charts'
	loaded_tickers		= list(scope.data['ticker_files'].keys())

	
	for ticker in page_ticker_list:
		
		renew_ticker_data_status = scope.pages[page]['renew']['ticker_data'][ticker]

		
		# renew_expansions_for_ticker = list(scope.pages[page]['renew']['expanders']  [ticker].keys())
		# ====================================================================
		# Replace all of the ticker data for the ticker
		# ====================================================================

		# Check if we have been requested to renew the ticker data for this ticker
		if  renew_ticker_data_status == True:

				# Check that there is share data available for this ticker
				# before attempting to copy that share date for use by this page
				# (function will fail if ticker data is not available) 

				if ticker in loaded_tickers: 
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to page df where page = ' + page + '\033[0m')
					
					ticker_df = scope.data['ticker_files'][ticker].copy()
					
					# sort the df into the correct order for the charting
					ticker_df.sort_values(by=['date'], inplace=True, ascending=True)
					
					# limit no of rows for the page_df (speeds up page rendering)
					if page_row_limit != None : 
						ticker_df = ticker_df.tail(page_row_limit) 									
					
					# Store the ticker dataframe for use by the page
					scope.pages[page]['df'][ticker] = ticker_df

					# reset Share Data Refresh STATUS to prevent unnecesary updates				
					scope.pages[page]['renew']['ticker_data'][ticker] = False
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')


		# ====================================================================
		# Replace the columns required for this ticker / chart 
		# ====================================================================

		expanders = list(scope.pages[page]['renew']['expanders'][ticker].keys())
		tickers_already_loaded_for_page = list(scope.pages[page]['df'].keys())

		for expander in expanders:
			
			renew_expander = scope.pages[page]['renew']['expanders'][ticker][expander]

			# Check if we have been requested to renew the columns for this ticker
			if renew_expander == True:
				
				if ticker in tickers_already_loaded_for_page:

					ticker_df				= scope.pages[page]['df'][ticker]
					column_adder			= scope.config[config_group][expander]['add_columns']
					column_adder_function 	= scope.config[config_group][expander]['add_columns']['function']

					# Expansion has a column_adder which requires additional columns (ie. has a function)
					if column_adder != None and column_adder_function != None:	
						
						# Call the column adding function for this expander
						scope.config[config_group][expander]['add_columns']['function'](scope, expander, ticker, ticker_df)
					
						# if page == 'screener':
						# 	# Store any test results (only for screener page)
						# 	store_test_results(scope, ticker, expander, ticker_df)						# store the test results for reporting

						# reset the refresh.metric_cols STATUS to prevent further updates
						scope.pages[page]['renew']['expanders'][ticker][expander] = False	

		# ====================================================================
		# Summary Result for any tests
		# ====================================================================

		create_test_result_summary(scope)

# Below is the original code which seemed to work ok

def update_screener_dfs(scope):

	page 			= scope.page_to_display
	page_row_limit 	= int(scope.page_row_limit)
	ticker_list 	= scope.pages[page]['ticker_list']

	if page == 'screener':																								# Function only works on this page
		for ticker in ticker_list:
			if scope.pages[page]['add_ohlcv_data'][ticker] == True:														# so we only refresh if we have been asked to
				if ticker in scope.ticker_data_files:																	# if data missing, function will not be able to run
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to screener_df'.ljust(50) + 'page = ' + page + '\033[0m')
					screener_df = scope.ticker_data_files[ticker].copy()
					screener_df.sort_values(by=['date'], inplace=True, ascending=True)		

					if page_row_limit != None : 
						screener_df = screener_df.tail(page_row_limit) 													# limit analysis to user specified row limit

					scope.pages[page]['screener_df'][ticker] = screener_df												# store the screener_df with additional metric columns			
					scope.pages[page]['add_ohlcv_data'][ticker] = False													# reset Page df STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.ticker_data_files \033[0m')
			# else:
			# 	print ( '\033[96m' + ticker.ljust(10) + '> add_ohlcv_data not requested \033[0m')


def update_screener_metrics(scope):
	print('$'*50)
	for ticker in scope.pages['screener']['ticker_list']:
		print(ticker)
		for test in scope.pages['screener']['renew']['tests'][ticker].keys():
			print(test)

	page 			= scope.pages['display_page']
	ticker_list 	= scope.pages[page]['ticker_list']

	if page == 'screener':																				# only works on the screener page
		for ticker in ticker_list:																		# iterate through each ticker for the page
			if ticker in scope.pages[page]['df'].keys():												# if data missing, function will not be able to run
				screener_df = scope.pages[page]['df'][ticker]											# short reference to the object being edited
				for test in scope.pages[page]['renew']['tests'][ticker].keys():							# iterate through available tests for this ticker and their run (or not) status
					test_run_status   = scope.pages[page]['renew']['tests'][ticker][test]
					test_has_function = scope.config['tests'][test]['add_columns']['function']
					if test_run_status==True and test_has_function != None:								# test needs refreshing and requires additional columns (they all do)
						scope.config['tests'][test]['add_columns']['function'](scope, screener_df, test )# Call the column adding function
						
						
						update_test_results_dict(scope, ticker, test, screener_df)						# store the test results for reporting
						scope.pages[page]['renew']['tests'][ticker][test] = False						# reset Test data STATUS to prevent unnecesary updates
		screener_all_active_test_results(scope)															# determine overall test result summary





# def update_chart_metrics(scope):
		# for ticker in scope.pages[page]['ticker_list']:
			
			# Check that the page share_data is present for this ticker before 
			# attempting to make changes to its dataframe
			# (function will fail if not present)
			
			# if ticker in scope.pages[page]['df'].keys():
				
				# chart_df = scope.pages[page]['df'][ticker]

				# iterate through each chart being utilised by this ticker 
				# and then execute (or not) the column adding function
				# for chart in scope.pages[page]['renew']['expanders'][ticker].keys():
					# chart_refresh_requested = scope.pages[page]['renew']['expanders'][ticker][chart]
					# chart_has_metric		= scope.config['expanders'][chart]['add_columns']
					# metric_has_function 	= scope.config['expanders'][chart]['add_columns']['function']
					
					# Chart needs refreshing and has add_cols and requires additional columns (function)
					# if chart_refresh_requested==True and chart_has_metric!=None and metric_has_function != None:	
						
						# # Call the add_cols (column) adding function
						# scope.config['expanders'][chart]['add_columns']['function'](scope, chart_df, chart)		
						
						# # reset Chart Data Refresh STATUS to prevent unnecesary updates
						# scope.pages[page]['renew']['expanders'][ticker][chart] = False					


