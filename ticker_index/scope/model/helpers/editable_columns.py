import logging


def scope_ticker_index_editable_columns(scope):
	logging.debug("scope_ticker_index_editable_columns")
	schema = scope.ticker_index['schema']
	editable_cols={}
	for i, key in enumerate(schema):
		if schema[key]['allow_edits'] == True:
			editable_cols[i]=key
	scope.ticker_index['lists']['editable_columns'] = editable_cols
