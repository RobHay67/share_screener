


def scope_tickers_missing(scope):
	# To Store the missing ticker information
	scope.tickers['missing'] = {}
	scope.tickers['missing'] = {
								'errors': {},
								'local' : [],
								'cloud' : [],
								'list'  : [],
								}
	
def scope_missing_ticker_error(scope, ticker):
	scope.tickers['missing']['errors'][ticker] = {'load':None, 'yf':None}




	# scope.tickers_missing