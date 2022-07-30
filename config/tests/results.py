
import pandas as pd


from config.tests.active_tests import scope_active_test_list



def create_summary_of_test_results(scope):

	app = scope.apps['display_app']
	active_test_list = scope_active_test_list(scope)
	column_list = ['ticker'] + active_test_list + ['summary_result']

	# Create an overall df to store the results for every ticker and test
	test_results_df = pd.DataFrame(columns=column_list)

	# Iterate through the ticker_list and extract the test results
	for ticker in scope.apps[app]['ticker_list']:

		ticker_test_results = []
		ticker_test_results.append(ticker)

		# Set default result to pass as a single test 'fail'
		# will over-write the summary_result
		summary_result = 'pass'

		# Check that we have some data for this ticker
		if ticker in scope.apps[app]['dfs'].keys():
			
			ticker_df = scope.apps[app]['dfs'][ticker]

			for test in active_test_list:

				# test_result = ticker_df[test].iloc[-1]
				test_result = ticker_df[test].iloc[0]

				if test_result != 'pass':
					# not all tests have passed so we fail overall
					summary_result = 'fail'		

				# Store the result for this test in the temp dictionary
				ticker_test_results.append(test_result)

			# Store the overall summary result
			ticker_test_results.append(summary_result)

			# Store tickers every test result and the overall result in a dataframe 
			test_results_df.loc[len(test_results_df.index)] = ticker_test_results


	return test_results_df

