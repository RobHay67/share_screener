from pages.view.analysis_title import analysis_titles		
from screener.view.example import example_settings			#TODO fleshing out some ideas
from screener.view.buttons import execute_screening_button


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_ticker_screener(scope):
	analysis_titles(scope, 'Ticker Screener', 'screener')

	execute_screening = execute_screening_button(scope)

	example_settings(scope)

	if execute_screening:
		print ( 'lets kick of the screening')
		for test in scope.screener_schema.keys():	
		# for test, criteria in scope.screener_schema.items():
			if scope.screener_schema[test]['active'] == True:											# User has chosen to run this test
				if scope.screener_schema[test]['data_cols'] != None:									# This test has additional columns (config contains the column details)
					if scope.screener_schema[test]['data_cols']['function'] != None:					# Some tests use the existing OHLCV columns
						scope.screener_schema[test]['data_cols']['metric_function'](scope, chart_df, test)		# Call the column adding function

				for ticker in scope.pages['screener']['ticker_list']:
					print ( '\033[95m' + ticker + ' > checking for criteria = ' + test + '\033[0m')







	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!


	# if ticker in scope.pages['screener']['chart_df'].keys():	
	# for ticker in scope.pages['screener']['ticker_list']:
		# print (ticker)



