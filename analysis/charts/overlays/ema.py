



def ema_cols( scope, chart_df, measure):
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.measures[measure]['params']['column']
	no_of_days 	= scope.measures[measure]['params']['periods']

	chart_df[measure] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()



