import logging




def ticker_index_uneditable_columns(scope):
	logging.debug("ticker_index_uneditable_columns")
	schema = scope.ticker_index['schema']
	uneditable_cols=[]
	for field, schema in schema.items():
		if schema['allow_edits'] == False:
			uneditable_cols.append(field)
	return uneditable_cols