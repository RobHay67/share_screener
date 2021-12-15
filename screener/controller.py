from pages.view.analysis_title import analysis_titles		
from screener.view.example import example_settings			#TODO fleshing out some ideas
# from screener.view.buttons import execute_screening_button
from screener.view.test_results import view_test_results




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_ticker_screener(scope):
	analysis_titles(scope, 'Ticker Screener', 'screener')

	# execute_screening = execute_screening_button(scope)

	view_test_results(scope)



	example_settings(scope)


	

	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!


	# if ticker in scope.pages['screener']['chart_df'].keys():	
	# for ticker in scope.pages['screener']['ticker_list']:
		# print (ticker)



