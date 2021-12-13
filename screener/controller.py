		
from screener.view import screener_title
from screener.view import example_settings			#TODO fleshing out some ideas



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Mult Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def view_ticker_screener(scope):
	screener_title(scope, 'Ticker Screener', 'screener')

	example_settings(scope)

	# TODO we migth be able to jumpt to single stock analysis from any list - that migth be cool!!!


	# if ticker in scope.pages['screener']['chart_df'].keys():	
	# for ticker in scope.pages['screener']['ticker_list']:
		# print (ticker)



