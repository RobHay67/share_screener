import logging


def scope_ticker_index_csv_dtypes(scope):
	logging.warning("scope_ticker_index_csv_dtypes")
	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	scope.ticker_index['lists']['csv_dtypes'] = dtypes


