
import pandas as pd


from config.tests.active_tests import scope_active_test_list



def create_summary_of_test_results(scope):

	page = scope.pages['display_page']
	active_test_list = scope_active_test_list(scope)
	column_list = ['ticker'] + active_test_list + ['summary_result']

	# Create an overall df to store the results for every ticker and test
	test_results_df = pd.DataFrame(columns=column_list)

	# Iterate through the tickers and extract the test results
	for ticker in scope.pages[page]['ticker_list']:
		print(ticker)

		ticker_test_results = {}
		ticker_test_results['ticker'] = ticker

		# Set default result to pass as a single test 'fail'
		# will over-write the summary_result
		summary_result = 'pass'

		# Check that we have some data for this ticker
		if ticker in scope.pages[page]['df'].keys():
			
			ticker_df = scope.pages[page]['df'][ticker]

			for test in active_test_list:

				test_result = ticker_df[test].iloc[-1]

				if test_result != 'pass':
					# not all tests have passed so we fail overall
					summary_result = 'fail'		

				# Store the result for this test in the temp dictionary
				ticker_test_results[test] = test_result

			# Store the overall summary result
			ticker_test_results['summary_result'] = summary_result

			# Store tickers every test result and the overall result in a dataframe 
			test_results_df = test_results_df.append(ticker_test_results, ignore_index=True)


	return test_results_df

