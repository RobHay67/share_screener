



def ema_cols( scope, chart_df, chart):
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.charts[chart]['data_cols']['column']
	no_of_days 	= scope.charts[chart]['data_cols']['periods']

	chart_df[chart] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()



