


def sma_cols(scope, chart_df, chart):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.charts[chart]['data_cols']['periods']

	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()




