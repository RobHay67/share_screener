import logging


def ticker_index_csv_dtypes(scope):
	logging.debug("ticker_index_csv_dtypes")
	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		if schema['dtype'] != 'datetime64[ns]': 
			dtypes[field] = schema['dtype']
	return dtypes


