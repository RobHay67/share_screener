

from screener.model.test_results import update_test_results_dict
from screener.model.test_results import screener_all_active_test_results


def update_screener_dfs(scope):

	page 			= scope.pages['display_page']
	page_row_limit 	= int(scope.pages['row_limit'])
	ticker_list 	= scope.pages[page]['ticker_list']

	if page == 'screener':																								# Function only works on this page
		for ticker in ticker_list:
			if scope.pages[page]['add_ohlcv_data'][ticker] == True:														# so we only refresh if we have been asked to
				if ticker in scope.data['ticker_files']:																	# if data missing, function will not be able to run
					print ( '\033[92m' + ticker.ljust(10) + '> adding ticker to screener_df'.ljust(50) + 'page = ' + page + '\033[0m')
					screener_df = scope.data['ticker_files'][ticker].copy()
					screener_df.sort_values(by=['date'], inplace=True, ascending=True)		

					if page_row_limit != None : 
						screener_df = screener_df.tail(page_row_limit) 													# limit analysis to user specified row limit

					scope.pages[page]['screener_df'][ticker] = screener_df												# store the screener_df with additional metric columns			
					scope.pages[page]['add_ohlcv_data'][ticker] = False													# reset Page df STATUS to prevent unnecesary updates
				else:
					print ( '\033[91m' + ticker.ljust(10) + '> ticker file missing from scope.data[ticker_files] \033[0m')
			# else:
			# 	print ( '\033[96m' + ticker.ljust(10) + '> add_ohlcv_data not requested \033[0m')




def update_screener_metrics(scope):

	page 			= scope.pages['display_page']
	ticker_list 	= scope.pages[page]['ticker_list']

	if page == 'screener':																				# only works on the screener page
		for ticker in ticker_list:																		# iterate through each ticker for the page
			if ticker in scope.pages[page]['screener_df'].keys():										# if data missing, function will not be able to run
				screener_df = scope.pages[page]['screener_df'][ticker]									# short reference to the object being edited
				for test in scope.pages[page]['add_metric_data'][ticker].keys():						# iterate through available tests for this ticker and their run (or not) status
					test_run_status 	= scope.pages[page]['add_metric_data'][ticker][test]
					# test_has_function	= scope.config['tests'][test]['metric_function']					# TODO - remove after restructure
					test_has_function	= scope.config['tests'][test]['metrics']['function']
					if test_run_status==True and test_has_function != None:								# test needs refreshing and requires additional columns (they all do)
						# scope.config['tests'][test]['metric_function'](scope, screener_df, test )		# TODO - delete after restructure Call the column adding function
						scope.config['tests'][test]['metrics']['function'](scope, screener_df, test )	# Call the column adding function
						update_test_results_dict(scope, ticker, test, screener_df)						# store the test results for reporting
						scope.pages[page]['add_metric_data'][ticker][test] = False						# reset Test data STATUS to prevent unnecesary updates
		screener_all_active_test_results(scope)															# determine overall test result summary






