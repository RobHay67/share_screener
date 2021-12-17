

from screener.model.test_results import update_test_results_dict
from screener.model.test_results import screener_all_active_test_results


def update_screener_dfs(scope, ticker_list):

	page 				= scope.page_to_display
	page_row_limit 	= int(scope.page_row_limit)

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
			else:
				print ( '\033[96m' + ticker.ljust(10) + '> add_ohlcv_data not requested \033[0m')




def update_screener_metrics(scope, ticker_list):

	page 				= scope.page_to_display

	if page == 'screener':																				# only works on the screener page
		for ticker in ticker_list:																		# iterate through each ticker for the page
			if ticker in scope.pages[page]['screener_df'].keys():										# if data missing, function will not be able to run
				screener_df = scope.pages[page]['screener_df'][ticker]									# short reference to the object being edited
				for test in scope.pages[page]['add_metric_data'][ticker].keys():						# iterate through available tests for this ticker and their run (or not) status
					test_run_status 	= scope.pages[page]['add_metric_data'][ticker][test]
					test_has_function	= scope.screener_tests[test]['metric_function']
					if test_run_status==True and test_has_function != None:								# test needs refreshing and requires additional columns (they all do)
						scope.screener_tests[test]['metric_function'](scope, screener_df, test )		# Call the column adding function
						update_test_results_dict(scope, ticker, test, screener_df)						# store the test results for reporting
						scope.pages[page]['add_metric_data'][ticker][test] = False						# reset Test data STATUS to prevent unnecesary updates
		screener_all_active_test_results(scope, ticker_list)															# determine overall test result summary






