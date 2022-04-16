
# Store the results of any test for easier reporting



def store_test_results( scope, test, ticker, screener_df):
	print ( 'running > store_test_results')
	# Add ticker to tests.results dictionary if its missing
	if ticker not in scope.pages['tests']['results'].keys():
		# print('adding ', ticker, ' to scope.pages[tests][results]')
	# if ticker not in scope.pages['screener']['test_results'].keys():
		# scope.pages['screener']['test_results'][ticker] = {}
		scope.pages['tests']['results'][ticker] = {}


	if len(screener_df) > 0:
		# print('screener_df is > 0 rows long')
		# print(screener_df.tail(10))
		# TODO - what is this function doing exactly - grabbing the last col??
		# print(screener_df[test].iloc[-1])
		# scope.pages['screener']['test_results'][ticker][test] = screener_df[test].iloc[-1]
		scope.pages['tests']['results'][ticker][test] = screener_df[test].iloc[-1]

	# print(scope.pages['tests']['results'])
		





# {'ABA.AX': {'trend_high': 'failed'}, 
# 'AFG.AX': {'trend_high': 'failed'}, 
# 'ANZ.AX': {'trend_high': 'failed'}, 
# 'BBC.AX': {'trend_high': 'failed'}, 
# 'BEN.AX': {'trend_high': 'failed'}, 
# 'BFL.AX': {'trend_high': 'failed'}, 
# 'BOQ.AX': {'trend_high': 'failed'}, 
# 'CBA.AX': {'trend_high': 'failed'},
#  'GMA.AX': {'trend_high': 'failed'}, 
#  'HGH.AX': {'trend_high': 'failed'}, 'JDO.AX': {'trend_high': 'failed'}, 'KSL.AX': {'trend_high': 'failed'}, 'LFG.AX': {'trend_high': 'failed'}, 'MYS.AX': {'trend_high': 'failed'}, 'N1H.AX': {'trend_high': 'failed'}, 'NAB.AX': {'trend_high': 'failed'}, 'PPM.AX': {'trend_high': 'failed'}, 'RMC.AX': {'trend_high': 'failed'}, 'VUK.AX': {'trend_high': 'failed'}, 'WBC.AX': {'trend_high': 'failed'}, 'YBR.AX': {'trend_high': 'failed'}, 'ABV.AX': {'trend_high': 'failed'}, 'ARB.AX': {'trend_high': 'passed'}, 'ATL.AX': {'trend_high': 'failed'}, 'CBR.AX': {'trend_high': 'failed'}, 'DDT.AX': {'trend_high': 'failed'}, 'GUD.AX': {'trend_high': 'failed'}, 'PWH.AX': {'trend_high': 'failed'}, 'RPM.AX': {'trend_high': 'failed'}, 'SFC.AX': {'trend_high': 'failed'}}








