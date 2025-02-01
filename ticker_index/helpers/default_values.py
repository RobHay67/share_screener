import logging



def ticker_index_default_values(scope):
	logging.debug("ticker_index_default_values")
	schema = scope.ticker_index['schema']
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	return default_values

