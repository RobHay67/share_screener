def format_downloaded_ticker_data(scope):
	# simple object reference
	type = scope.yf['batch_type']
	yf_df = scope.yf['batch_data']
	yf_schema = scope.yf['schemas'][type]

	# remove any index set during import - we will set the index later
	yf_df.reset_index(inplace=True)   

	# Remove redundant columns
	for yf_column in yf_schema:
		ticker_schema_key = yf_schema[yf_column]['schema_key']
		keep_column = yf_schema[yf_column]['keep_column']
		
		if keep_column : 
			yf_df.rename(columns = { yf_column : ticker_schema_key }, inplace = True)
		else:
			del yf_df[yf_column]

	# ensure any empty volume days contain a zero rather than being null or empty
	yf_df['volume'] = yf_df['volume'].fillna(0).astype(int)
