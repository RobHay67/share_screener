import pandas as pd


# Store the results of any test for easier reporting



def store_test_results( scope, test, ticker, screener_df):
	print ( 'running > store_test_results')
	# Add ticker to tests.results dictionary if its missing
	if ticker not in scope.pages['tests']['results'].keys():
		scope.pages['tests']['results'][ticker] = {}


	if len(screener_df) > 0:
		# From the latest (last) row of the test, record the result in
		# a dictionary which will be used to report the results from all the tests
		scope.pages['tests']['results'][ticker][test] = screener_df[test].iloc[-1]

	print("scope.pages['tests']['results'] >", scope.pages['tests']['results'])
	
	# {
	# 'ABA.AX': {'trend_high': 'fail'}, 
	# 'AFG.AX': {'trend_high': 'fail'}, 
	# 'ANZ.AX': {'trend_high': 'fail'}, 
	# 'BBC.AX': {'trend_high': 'fail'}, 
	# 'BEN.AX': {'trend_high': 'fail'}, 'BFL.AX': {'trend_high': 'fail'}, 'BOQ.AX': {'trend_high': 'fail'}, 'CBA.AX': {'trend_high': 'fail'}, 'GMA.AX': {'trend_high': 'fail'}, 'HGH.AX': {'trend_high': 'fail'}, 'JDO.AX': {'trend_high': 'fail'}, 'KSL.AX': {'trend_high': 'fail'}, 'LFG.AX': {'trend_high': 'fail'}, 'MYS.AX': {'trend_high': 'fail'}, 'N1H.AX': {'trend_high': 'fail'}, 'NAB.AX': {'trend_high': 'fail'}, 'PPM.AX': {'trend_high': 'fail'}, 'RMC.AX': {'trend_high': 'fail'}, 'VUK.AX': {'trend_high': 'fail'}, 'WBC.AX': {'trend_high': 'fail'}, 'YBR.AX': {'trend_high': 'fail'}}



def create_test_result_summary(scope):
# def screener_all_active_test_results(scope):
	print('create_test_result_summary'.upper())
	# For each ticker, store every test result in a df
	# and generate an summary_result pass or fail for each ticker
	# summary_result = every test passes for each ticker

	page 		= scope.pages['display_page']
	
	ticker_list = scope.pages[page]['ticker_list']

	# determine a list of currently active tests - we may have turned off previously run tests
	active_test_list = []
	for test in scope.config['tests']['test_list']:	
		if scope.config['tests'][test]['active'] == True:
			active_test_list.append(test)
	print('active_test_list     = ', active_test_list)
 

	# create an empty dataframe to store every active test result
	# ticker, trend_open, trend_close
	column_list = ['ticker'] + active_test_list + ['summary_result']

	test_results_df = pd.DataFrame(columns=column_list)
	
	print('test_results_df')
	print(test_results_df)
	
	
	print('-'*66)
	for ticker in ticker_list:
		print('ticker               = ', ticker)
		# Ensure we have share data (and consequently test result) for this ticker
		if ticker in scope.pages['screener']['df']:
			
			ticker_test_results = {}
			# ticker_test_results = pd.DataFrame(columns=column_list)
			ticker_test_results['ticker'] = ticker

			print('ticker_test_results  = ', ticker_test_results)

			# Set default result to pass as a single 'fail' result will
			# correctly over-write the summary_result
			summary_result = 'pass'
			
			print('-'*66)
			for test in active_test_list:
				print('test                 = ', test)
				# test_result = scope.pages['screener']['test']['results'][ticker][test] 
				test_result = scope.pages['tests']['results'][ticker][test] 

				print('test_result          = ', test_result)
				
				# a single test failure results in total failure for this ticker
				if test_result != 'pass':
					summary_result = 'fail'						

				ticker_test_results[test] = test_result

				print('-'*66)
				print('ticker_test_results  = ', ticker_test_results)

			ticker_test_results['summary_result'] = summary_result
			print('A'*88)
			print('ticker_test_results > ', ticker_test_results) # {'ticker': 'ABA.AX', 'trend_high': 'fail', 'summary_result': 'fail'}
			
			# add the ???? to the overal test_results_df
			test_results_df = test_results_df.append(ticker_test_results, ignore_index=True)
			print('test_results_df')
			print(test_results_df)

			# pd.concat([df, pd.DataFrame(test.values(), columns=df.columns)], ignore_index=True)
			# ticker_test_results >  {'ticker': 'ABA.AX', 'trend_high': 'fail', 'summary_result': 'fail'}
			# pd.concat([test_results_df, ])
			# test_results_df = pd.concat(test_results_df, ticker_test_results)

	# Store the overall test results_df for reporting by the page
	scope.pages['tests']['df'] = test_results_df
	print('.'*77)
	print('test_results_df')
	print(test_results_df)
	print('='*100)


def screener_all_active_test_results(scope):

	page 		= scope.pages['display_page']
	
	ticker_list = scope.pages[page]['ticker_list']

	# determine a list of currently active tests - we may have turned off previously run tests
	active_test_list = []
	for test in scope.config['tests']['test_list']:	
		if scope.config['tests'][test]['active'] == True:
			active_test_list.append(test)

	# create an empty dataframe to store every active test result
	test_results_df = pd.DataFrame(columns=['ticker']+active_test_list+['all_test_results'])


	# store the active test results for each ticker
	for ticker in ticker_list:
		if ticker in scope.pages['screener']['df']:					# if its not in here, it will not be available - ie no test results
			all_test_results = 'pass'
			ticker_test_result_dict = {}
			ticker_test_result_dict['ticker'] = ticker
			for test in active_test_list:
				test_result = scope.pages['screener']['test_results'][ticker][test] 
				
				if test_result != 'pass':
					all_test_results = 'fail'						# all tests must pass for the entire ticker to meet the criteria

				ticker_test_result_dict[test] = test_result

			ticker_test_result_dict['all_test_results'] = all_test_results

			test_results_df = test_results_df.append(ticker_test_result_dict, ignore_index=True)


	scope.pages['screener']['test_results_df'] = test_results_df