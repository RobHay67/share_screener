
import pandas as pd



def update_test_results_dict(scope, ticker, test, screener_df):

	if ticker not in scope.screener_test_results.keys():
		scope.screener_test_results[ticker] = {}

	if len(screener_df) > 0:
		scope.screener_test_results[ticker][test] = screener_df[test].iloc[-1]


		




def screener_all_active_test_results(scope, ticker_list):

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




# iterate through each ticker in the ticker list
# iterate through the current active test
# extract the result for active tests from the results
# store the results in a dataframe
# compute an overall result



# {'3DA.AX': {'trend_high': 'failed'}, 
# 'A3D.AX': {'trend_high': 'failed'}, 
# 'ACF.AX': {'trend_high': 'failed'},
#  'AE1.AX': {'trend_high': 'failed'}, 
#  'AIR.AX': {'trend_high': 'failed'},
#   'AJL.AX': {'trend_high': 'failed'},
#    'AL3.AX': {'trend_high': 'failed'},
#    'ANG.AX': {'trend_high': 'failed'},
#     'ASB.AX': {'trend_high': 'failed'},
#     'BMH.AX': {}, 
# 	'BOL.AX': {'trend_high': 'failed'}, 
# 	'BPP.AX': {'trend_high': 'failed'},
# 	 'CFO.AX': {'trend_high': 'failed'}, 
# 	'CIM.AX': {'trend_high': 'failed'},
# 	 'CPV.AX': {'trend_high': 'failed'}, 
# 	'CVL.AX': {'trend_high': 'failed'},
# 	 'CYG.AX': {'trend_high': 'failed'}, 
# 	'DCG.AX': {'trend_high': 'failed'}, 
# 	'DDB.AX': {'trend_high': 'failed'},
# 	 'DRA.AX': {'trend_high': 'failed'}, 
# 	 'DRO.AX': {'trend_high': 'failed'},
# 	  'DUR.AX': {'trend_high': 'failed'},
# 	   'ECL.AX': {'trend_high': 'failed'},
# 	   'EGL.AX': {'trend_high': 'failed'},
# 	    'EGN.AX': {'trend_high': 'failed'},
# 	    'EGY.AX': {'trend_high': 'failed'},
# 		 'EHL.AX': {'trend_high': 'failed'},
# 		 'EMB.AX': {'trend_high': 'failed'},
# 		  'EOS.AX': {'trend_high': 'failed'},
# 		  'EVZ.AX': {'trend_high': 'failed'},
# 		   'FBR.AX': {'trend_high': 'failed'},
# 		   'FLC.AX': {'trend_high': 'failed'},
# 		    'FOS.AX': {'trend_high': 'failed'},
# 		    'GNP.AX': {'trend_high': 'failed'},
# 			 'GWA.AX': {'trend_high': 'failed'},
# 			 'HNG.AX': {'trend_high': 'failed'}}