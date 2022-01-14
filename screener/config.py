from metrics.config import metrics_config, trend_direction



def scope_screener(scope):
	
	scope.screener_tests 			= metrics_config
	scope.screener_trends 			= trend_direction
	scope.screener_test_results 	= {}					# this is for any and all test that have been run during the sesssion - ite incrementally updated
	scope.screener_test_results_df 	= {}					# this is just the test results for the currently active tests (a subset of screener_test_results )


	
# scope.rsi_level = 0.50
# scope.rsi_column = 'close'

# scope.macd_direction = 'up'
# scope.macd_strength = 'strong'


# scope.sma_line = 'above'
# scope.ema_line = 'above'