import logging
from tickers.scope.model.schema_tickers import schema


def scope_tickers_schema(scope):
	logging.debug("scope_tickers_schema")
	scope.ticker_schema = {}
	scope.ticker_schema['schema'] = schema
	scope.ticker_schema['usecols'] = ['date', 'open', 'high', 'low', 'close', 'volume']
	scope.ticker_schema['dtypes'] = {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
	scope.ticker_schema['dates'] = ['date']

	# To Store the missing ticker information
	scope.ticker_schema['missing'] = {}
	scope.ticker_schema['missing'] = {
								'errors': {},
								'local' : [],
								'cloud' : [],
								'list'  : [],
								}

	
def scope_missing_ticker_error(scope, ticker):
	logging.error("scope_missing_ticker_error")
	scope.ticker_schema['missing']['errors'][ticker] = {'load':None, 'yf':None}
