
from tickers.scope.model.schema_tickers import schema


def scope_tickers_config(scope):
	scope.ticker_config = {}
	scope.ticker_config['schema'] = schema
	scope.ticker_config['usecols'] = ['date', 'open', 'high', 'low', 'close', 'volume']
	scope.ticker_config['dtypes'] = {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
	scope.ticker_config['dates'] = ['date']

	# To Store the missing ticker information
	scope.ticker_config['missing'] = {}
	scope.ticker_config['missing'] = {
								'errors': {},
								'local' : [],
								'cloud' : [],
								'list'  : [],
								}

	
def scope_missing_ticker_error(scope, ticker):
	scope.ticker_config['missing']['errors'][ticker] = {'load':None, 'yf':None}
