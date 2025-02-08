import logging


def ema_cols(  scope, chart, ticker, chart_df):
	logging.warning("ema_cols")
	# add an Exponential Moving Average (EMA)
	
	# EMA  = https://www.investopedia.com/terms/e/ema.asp

	column 		= scope.charts['user_config'][chart]['function']['column']
	no_of_days 	= scope.charts['user_config'][chart]['function']['periods']

	chart_df[chart] = chart_df[column].ewm(span=no_of_days, adjust=False).mean()


	