import logging




def scope_ticker_index_uneditable_columns(scope):
	logging.debug("scope_ticker_index_uneditable_columns")
	schema = scope.ticker_index['schema']
	uneditable_cols=[]
	for field, schema in schema.items():
		if schema['allow_edits'] == False:
			uneditable_cols.append(field)
	scope.ticker_index['lists']['uneditable_columns'] = uneditable_cols
