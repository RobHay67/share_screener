
def scope_tickers_config(scope):
	scope.ticker_config = {}
	scope.ticker_config['schema'] = schema
	scope.ticker_config['usecols'] = ['date', 'open', 'high', 'low', 'close', 'volume']
	scope.ticker_config['dtypes'] = {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
	scope.ticker_config['dates'] = ['date']

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ticker Data file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
index_col		= 'index_col'
data_type 		= 'data_type'
english 		= 'english'
long_english 	= 'long_english'


schema =  {
		'date'  : { index_col : True  , data_type : 'datetime64[ns]', english:'Date'	, long_english:'Date'  			},
		'open' 	: { index_col : False , data_type : 'float64'		, english:'Opening'	, long_english:'Opening Price'	},
		'high' 	: { index_col : False , data_type : 'float64' 		, english:'Highest'	, long_english:'Highest Price'	},
		'low'  	: { index_col : False , data_type : 'float64' 		, english:'Lowest'	, long_english:'Lowest Price' 	},
		'close' : { index_col : False , data_type : 'float64'		, english:'Closing'	, long_english:'Closing Price'	},
		'volume': { index_col : False , data_type : 'int64'			, english:'Volume'	, long_english:'Volume'			}, 
		'ticker': { index_col : False , data_type : None			, english:'Ticker'	, long_english:'Ticker Code'	},   # will not be added to the column dictionary
		}

