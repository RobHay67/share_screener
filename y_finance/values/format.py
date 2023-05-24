
from y_finance.schemas import y_finance_schemas
from tickers.schema import ticker_file_schema


def format_downloaded_batch(scope):
	
	# simple object reference
	schema = scope.yf['batch_type']
	yf_download = scope.yf['batch_data']

	# remove any index set during import - we will set the index later
	yf_download.reset_index(inplace=True)   

	for col_no in y_finance_schemas[schema]:
		provider_column_name = y_finance_schemas[schema][col_no]['col_name']
		if col_no < 50:                 	
			# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = ticker_file_schema[col_no]['col_name']
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	
			# its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)