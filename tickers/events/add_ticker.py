
from tickers.config import scope_new_ticker


def add_ticker_event(scope, ticker):

	# This event is triggered after new ticker data is
	# either loaded or downloaded. 
	#  
	# Add keys to the ticker to house the df 
	# Add appropriate column adders state information
	# This function only generate the empty objects with
	# the default values. Data is added by other functions.


	# config for new ticcker is kept in the config module for consistency
	scope_new_ticker(scope, ticker)



