import logging


def scope_ticker_index_data_types(scope):
	logging.debug("scope_ticker_index_data_types")
	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	scope.ticker_index['lists']['data_types'] = dtypes

