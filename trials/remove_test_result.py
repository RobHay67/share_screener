




def remove_test_result_column(scope, ticker, config_key_name):
    
	ticker_df = scope.tickers[ticker]['screener']['df']
	if config_key_name in ticker_df:
		del ticker_df[config_key_name]