




def remove_test_result_column(scope, ticker, column_adder):
    
	ticker_df = scope.tickers[ticker]['screener']['df']
	if column_adder in ticker_df:
		del ticker_df[column_adder]