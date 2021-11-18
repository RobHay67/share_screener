




def sma(scope, plot_df, measure):
	column 		= scope.measures[measure]['params']['column']
	no_of_days 	= scope.measures[measure]['params']['periods']

	plot_df.sort_values(by=['date'], inplace=True, ascending=True)	

	plot_df[measure] = plot_df[column].rolling(window=no_of_days).mean()





