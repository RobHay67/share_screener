import logging


def scope_ticker_index_default_values(scope):
	logging.debug("scope_ticker_index_default_values")
	schema = scope.ticker_index['schema']
	default_values={}
	for field, schema in schema.items():
		default_values[field] = schema['default']
	scope.ticker_index['lists']['default_values'] = default_values
