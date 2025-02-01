import logging


def ticker_index_data_types(scope):
	logging.debug("ticker_index_data_types")

	schema = scope.ticker_index['schema']
	dtypes={}
	for field, schema in schema.items():
		dtypes[field] = schema['dtype']
	return dtypes


