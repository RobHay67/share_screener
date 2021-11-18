




def sma(scope, plot_df, measure):
	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.measures[measure]['params']['column']
	no_of_days 	= scope.measures[measure]['params']['periods']

	plot_df[measure] = plot_df[column].rolling(window=no_of_days).mean()





