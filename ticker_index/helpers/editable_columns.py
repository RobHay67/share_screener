import logging


def ticker_index_editable_columns(scope):
	logging.debug("ticker_index_editable_columns")
	schema = scope.ticker_index['schema']
	editable_cols={}
	for i, key in enumerate(schema):
		if schema[key]['allow_edits'] == True:
			editable_cols[i]=key
	return editable_cols