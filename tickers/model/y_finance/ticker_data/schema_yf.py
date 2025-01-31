import logging

def scope_yf_schema(scope):
	logging.debug("scope_yf_schema")
	scope.yf['schemas'] = yf_schemas


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Download Share Data - various schemas
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# the schema index contain the column name of the downloaded dats
# the schema key is the reference to the ticker schema which contains
# the names of the columns for the entire application
# This method faciliates multiple download sources with differing
# column names which can be mapped to an ultimate ticker schema
# The keep_column reference is to allow for redundant cols to be dropped


schema_key 		= 'schema_key'
keep_column 	= 'keep_column'

yf_schemas =    {
		'single_ticker' :   	{
				'Date' 		: { schema_key : 'date'		, keep_column : True  },
				'Open' 		: { schema_key : 'open'		, keep_column : True  },
				'High' 		: { schema_key : 'high'		, keep_column : True  },
				'Low' 		: { schema_key : 'low'		, keep_column : True  },
				'Close' 	: { schema_key : 'close'	, keep_column : True  },
				'Adj Close'	: { schema_key : None  		, keep_column : False },
				'Volume' 	: { schema_key : 'volume'	, keep_column : True  },
				'Ticker' 	: { schema_key : 'ticker'	, keep_column : True  },   # manually added by the imported for consistency
				},
		'multiple_tickers' :    {
				'Date' 		: { schema_key : 'date'		, keep_column : True },
				'Ticker'  	: { schema_key : 'ticker'	, keep_column : True  },
				'Adj Close'	: { schema_key : None		, keep_column : False },
				'Close'		: { schema_key : 'close'	, keep_column : True  },
				'High'	 	: { schema_key : 'high'		, keep_column : True  },
				'Low' 		: { schema_key : 'low'		, keep_column : True  },
				'Open' 		: { schema_key : 'open'		, keep_column : True  },
				'Volume' 	: { schema_key : 'volume'	, keep_column : True  },
				}
		}

# yf_schemas =    {
	# 'single_ticker' :   	{
	# 						1 : { schema_key : 'Date'       , index_col : True  },
	# 						2 : { schema_key : 'Open'       , index_col : False },
	# 						3 : { schema_key : 'High'       , index_col : False },
	# 						4 : { schema_key : 'Low'        , index_col : False },
	# 						5 : { schema_key : 'Close'      , index_col : False },
	# 						50: { schema_key : 'Adj Close'  , index_col : False },
	# 						6 : { schema_key : 'Volume'     , index_col : False },
	# 						0 : { schema_key : 'Ticker'     , index_col : False },   # manually added by the imported for consistency
	# 						},
	# 'multiple_tickers' :    {
	# 						1 : { schema_key : 'Date'       , index_col : True  },
	# 						0 : { schema_key : 'Ticker'     , index_col : False },
	# 						98: { schema_key : 'Adj Close'  , index_col : False },
	# 						5 : { schema_key : 'Close'      , index_col : False },
	# 						3 : { schema_key : 'High'       , index_col : False },
	# 						4 : { schema_key : 'Low'        , index_col : False },
	# 						2 : { schema_key : 'Open'       , index_col : False },
	# 						6 : { schema_key : 'Volume'     , index_col : False },
	# 						}
	# }
