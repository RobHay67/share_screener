




def remove_test_result_column(scope, ticker, schema_key):
    
	ticker_df = scope.tickers[ticker]['screener']['df']
	if schema_key in ticker_df:
		del ticker_df[schema_key]