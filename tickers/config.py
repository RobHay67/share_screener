



def scope_ticker_files(scope):

	scope.tickers = {}


def scope_missing_tickers(scope):
	scope.missing_tickers = {}
	scope.missing_tickers['errors'] = {}
	scope.missing_tickers['local'] = []
	scope.missing_tickers['cloud'] = []
	scope.missing_tickers['list']  = []


def scope_missing_ticker_error(scope, ticker):
	scope.missing_tickers['errors'][ticker] = {'load':None, 'yf':None}