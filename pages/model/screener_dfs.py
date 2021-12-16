

from screener.model.test_results import update_test_results_dict
from screener.model.test_results import screener_all_active_test_results


# maybe split this between ticker_data and ticker_metrics










def update_screener_dfs(scope, ticker_list):

	page 				= scope.page_to_display
	page_row_limit 	= int(scope.page_row_limit)

	if page == 'screener':																								# Function only works on this page
		for ticker in ticker_list:
			if scope.pages[page]['refresh_ticker_data'][ticker] == True:												# so we only refresh if we have been asked to
				if ticker in scope.ticker_data_files:																	# if data missing, function will not be able to run
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to screener_df'.ljust(50) + 'page = ' + page + '\033[0m')
					screener_df = scope.ticker_data_files[ticker].copy()
					screener_df.sort_values(by=['date'], inplace=True, ascending=True)		

					if page_row_limit != None : 
						screener_df = screener_df.tail(page_row_limit) 													# limit analysis to user specified row limit

					scope.pages[page]['screener_df'][ticker] = screener_df												# store the screener_df with additional metric columns			
					scope.pages[page]['refresh_ticker_data'][ticker] = False											# reset STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.ticker_data_files \033[0m')
			else:
				print ( '\033[96m' + ticker.ljust(10) + '> refresh_ticker_data not requested \033[0m')

		screener_all_active_test_results(scope, ticker_list)															# determine overall test result summary



def update_screener_metrics(scope, ticker_list):

	page 				= scope.page_to_display


	if page == 'screener':																						# Function only works on this page
		for ticker in ticker_list:																				# iterate through each ticker for the page
			# we need to refer to the refresh_metrics at this point???
			if ticker in scope.pages[page]['screener_df'].keys():												# if data missing, function will not be able to run
				screener_df = scope.pages[page]['screener_df'][ticker]
				
					
				if scope.screener_tests[test]['active'] == True:												# User has chosen to run this test
					# if scope.screener_tests[test]['metrics'] != None:										# This test has additional columns (config contains the column details)
					if scope.screener_tests[test]['metric_function'] != None:									# Some tests use the existing OHLCV columns
						scope.screener_tests[test]['metric_function'](scope, screener_df, test )				# Call the column adding function
						update_test_results_dict(scope, ticker, test, screener_df)								# store the test results for reporting

