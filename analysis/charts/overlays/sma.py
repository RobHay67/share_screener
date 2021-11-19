




def sma(scope, plot_df, chart):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	# column 		= scope.measures[measure]['params']['column']
	# no_of_days 	= scope.measures[measure]['params']['periods']

	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.measures[chart]['data_cols']['periods']


	plot_df[chart] = plot_df[column].rolling(window=no_of_days).mean()





