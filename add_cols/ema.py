


def ema_cols( scope, chart_df, chart):
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.config['charts'][chart]['add_columns']['column']
	no_of_days 	= scope.config['charts'][chart]['add_columns']['periods']

	chart_df[chart] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()


	