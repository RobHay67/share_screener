
import pandas as pd



def update_test_results_dict(scope, ticker, test, screener_df):

	if ticker not in scope.screener_test_results.keys():
		scope.screener_test_results[ticker] = {}

	if len(screener_df) > 0:
		scope.screener_test_results[ticker][test] = screener_df[test].iloc[-1]


		

def screener_all_active_test_results(scope):

	page 		= scope.page_to_display
	ticker_list = scope.pages[page]['ticker_list']

	# determine a list of currently active tests - we may have turned off previously run tests
	active_test_list = []
	for test in scope.screener_tests.keys():	
		if scope.screener_tests[test]['active'] == True:
			active_test_list.append(test)

	# create an empty dataframe for the active test results
	test_results_df = pd.DataFrame(columns=['ticker']+active_test_list+['all_test_results'])


	# store the active test results for each ticker
	for ticker in ticker_list:
		if ticker in scope.pages['screener']['screener_df']:					# if its not in here, it will not be available - ie no test results
			all_test_results = 'passed'
			ticker_test_result_dict = {}
			ticker_test_result_dict['ticker'] = ticker
			for test in active_test_list:
				test_result = scope.screener_test_results[ticker][test] 
				
				if test_result != 'passed':
					all_test_results = 'failed'						# all tests must pass for the entire ticker to meet the criteria

				ticker_test_result_dict[test] = test_result

			ticker_test_result_dict['all_test_results'] = all_test_results

			test_results_df = test_results_df.append(ticker_test_result_dict, ignore_index=True)


	scope.screener_test_results_df = test_results_df


