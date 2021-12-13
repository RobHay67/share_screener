from pages.view.analysis_title import analysis_titles		
# from screener.view.title import screener_title
from screener.view.example import example_settings			#TODO fleshing out some ideas



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_ticker_screener(scope):
	analysis_titles(scope, 'Ticker Screener', 'screener')

	example_settings(scope)

	

	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!


	# if ticker in scope.pages['screener']['chart_df'].keys():	
	# for ticker in scope.pages['screener']['ticker_list']:
		# print (ticker)



