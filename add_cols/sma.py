


def sma_cols( scope, chart, ticker, chart_df):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.charts['config'][chart]['add_columns']['column']
	no_of_days 	= scope.charts['config'][chart]['add_columns']['periods']

	# Change chart_df to be ascending to simplify the shifting
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)

	# add the moving average
	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()

	# ensure Screener_df is back in its descending order (latest first)
	chart_df.sort_values(by=['date'], inplace=True, ascending=False)



