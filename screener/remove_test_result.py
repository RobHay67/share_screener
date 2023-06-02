




def remove_test_result_column(scope, ticker, config_key):
    
	ticker_df = scope.tickers[ticker]['screener']['df']
	if config_key in ticker_df:
		del ticker_df[config_key]