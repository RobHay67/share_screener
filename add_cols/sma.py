


def sma_cols( scope, chart, ticker, chart_df):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.config['charts'][chart]['add_columns']['column']
	no_of_days 	= scope.config['charts'][chart]['add_columns']['periods']

	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()




