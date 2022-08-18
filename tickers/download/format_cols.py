
from tickers.schema import ticker_file_schema
from tickers.download.schema import y_finance_schemas



def format_yf_download(scope, yf_download):
	
	download_schema = scope.download['yf_schema']

	yf_download.reset_index(inplace=True)   # remove any index set during import - we will set the index later

	for col_no in y_finance_schemas[download_schema]:
		provider_column_name    = y_finance_schemas[download_schema][col_no]['col_name']
		if col_no < 50:                 	# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = ticker_file_schema[col_no]['col_name']
			
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	# its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
	return( yf_download )




	