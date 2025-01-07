from tickers.scope.model.y_finance.ticker_data.schema import yf_ticker_schema
from tickers.scope.model.schema import ticker_file_schema


def format_downloaded_ticker_data(scope):
	
	# simple object reference
	schema = scope.yf['batch_type']
	yf_df = scope.yf['batch_data']

	# remove any index set during import - we will set the index later
	yf_df.reset_index(inplace=True)   

	# Remove redundant columns
	for col_no in yf_ticker_schema[schema]:
		provider_column_name = yf_ticker_schema[schema][col_no]['col_name']
		if col_no < 50:                 	
			# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = ticker_file_schema[col_no]['col_name']
			yf_df.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	
			# its a column that we do not need, so lets delete it
			del yf_df[provider_column_name]
	yf_df['volume'] = yf_df['volume'].fillna(0).astype(int)