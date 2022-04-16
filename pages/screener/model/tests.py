
import pandas as pd



def store_test_results(scope, ticker, test, screener_df):
	print ( 'running > store_test_results')
	# Add ticker to tests.results dictionary if its missing
	if ticker not in scope.pages['tests']['results'].keys():
		print('adding ', ticker, ' to scope.pages[tests][results]')
	# if ticker not in scope.pages['screener']['test_results'].keys():
		# scope.pages['screener']['test_results'][ticker] = {}
		scope.pages['tests']['results'][ticker] = {}


	if len(screener_df) > 0:
		print('screener_df is > 0 rows long')
		print(screener_df.tail(10))
		# TODO - what is this function doing exactly - grabbing the last col??
		print(screener_df[test].iloc[-1])
		# scope.pages['screener']['test_results'][ticker][test] = screener_df[test].iloc[-1]
		scope.pages['tests']['results'][ticker][test] = screener_df[test].iloc[-1]

	print(scope.pages['tests']['results'])
		

{'ABA.AX': {'trend_high': 'failed'}, 
'AFG.AX': {'trend_high': 'failed'}, 
'ANZ.AX': {'trend_high': 'failed'}, 
'BBC.AX': {'trend_high': 'failed'}, 
'BEN.AX': {'trend_high': 'failed'}, 
'BFL.AX': {'trend_high': 'failed'}, 
'BOQ.AX': {'trend_high': 'failed'}, 
'CBA.AX': {'trend_high': 'failed'},
 'GMA.AX': {'trend_high': 'failed'}, 
 'HGH.AX': {'trend_high': 'failed'}, 'JDO.AX': {'trend_high': 'failed'}, 'KSL.AX': {'trend_high': 'failed'}, 'LFG.AX': {'trend_high': 'failed'}, 'MYS.AX': {'trend_high': 'failed'}, 'N1H.AX': {'trend_high': 'failed'}, 'NAB.AX': {'trend_high': 'failed'}, 'PPM.AX': {'trend_high': 'failed'}, 'RMC.AX': {'trend_high': 'failed'}, 'VUK.AX': {'trend_high': 'failed'}, 'WBC.AX': {'trend_high': 'failed'}, 'YBR.AX': {'trend_high': 'failed'}, 'ABV.AX': {'trend_high': 'failed'}, 'ARB.AX': {'trend_high': 'passed'}, 'ATL.AX': {'trend_high': 'failed'}, 'CBR.AX': {'trend_high': 'failed'}, 'DDT.AX': {'trend_high': 'failed'}, 'GUD.AX': {'trend_high': 'failed'}, 'PWH.AX': {'trend_high': 'failed'}, 'RPM.AX': {'trend_high': 'failed'}, 'SFC.AX': {'trend_high': 'failed'}}





def screener_all_active_test_results(scope):

	page 		= scope.pages['display_page']
	
	ticker_list = scope.pages[page]['ticker_list']

	# determine a list of currently active tests - we may have turned off previously run tests
	active_test_list = []
	for test in scope.config['tests']['test_list']:	
		if scope.config['tests'][test]['active'] == True:
			active_test_list.append(test)

	# create an empty dataframe for the active test results
	test_results_df = pd.DataFrame(columns=['ticker']+active_test_list+['all_test_results'])


	# store the active test results for each ticker
	for ticker in ticker_list:
		if ticker in scope.pages['screener']['df']:					# if its not in here, it will not be available - ie no test results
			all_test_results = 'passed'
			ticker_test_result_dict = {}
			ticker_test_result_dict['ticker'] = ticker
			for test in active_test_list:
				test_result = scope.pages['screener']['test_results'][ticker][test] 
				
				if test_result != 'passed':
					all_test_results = 'failed'						# all tests must pass for the entire ticker to meet the criteria

				ticker_test_result_dict[test] = test_result

			ticker_test_result_dict['all_test_results'] = all_test_results

			test_results_df = test_results_df.append(ticker_test_result_dict, ignore_index=True)


	scope.pages['screener']['test_results_df'] = test_results_df


