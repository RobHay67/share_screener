


def scope_tickers_missing(scope):
	# To Store the missing ticker information
	scope.tickers_missing = {
								'errors': {},
								'local' : [],
								'cloud' : [],
								'list'  : [],
								}
	
def scope_missing_ticker_error(scope, ticker):
	scope.tickers_missing['errors'][ticker] = {'load':None, 'yf':None}