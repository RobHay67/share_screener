


def sma_cols(scope, chart_df, chart):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.config['charts']['config'][chart]['metrics']['column']
	no_of_days 	= scope.config['charts']['config'][chart]['metrics']['periods']

	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()




