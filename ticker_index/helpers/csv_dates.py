import logging


def ticker_index_csv_dates(scope):
	logging.debug("ticker_index_csv_dates")
	schema = scope.ticker_index['schema']
	dates_to_parse = []
	for field, schema in schema.items():
		if schema['dtype'] == 'datetime64[ns]': 
			dates_to_parse.append(field)
	return dates_to_parse