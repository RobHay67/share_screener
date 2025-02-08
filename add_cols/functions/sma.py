import logging
import numpy as np


def sma_cols( scope, chart, ticker, chart_df):
	logging.warning("sma_cols")

	# Add a Simple Moving Average (SMA)
	# https://www.investopedia.com/terms/s/sma.asp
	
	column 		= scope.charts['user_config'][chart]['function']['column']
	no_of_days 	= scope.charts['user_config'][chart]['function']['periods']

	# Change chart_df to be ascending to simplify the shifting
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)

	# add the moving average
	chart_df[chart] = chart_df[column].rolling(window=no_of_days).mean()

	# ensure Screener_df is back in its descending order (latest first)
	chart_df.sort_values(by=['date'], inplace=True, ascending=False)



def sma_trend(scope, trial, ticker, df):
	
	trend 		= scope.trials['user_config'][trial]['function']['trend']
	column 		= scope.trials['user_config'][trial]['function']['column']
	no_of_days 	= scope.trials['user_config'][trial]['function']['periods']

	# Change df to be ascending to simplify the shifting
	df.sort_values(by=['date'], inplace=True, ascending=True)

	# add the moving average
	df['temp_ma'] = df[column].rolling(window=no_of_days).mean()

	# Determine the Result for each row
	if trend == 'above_sma':
		df[trial] = np.where( df[column] > df['temp_ma'], 'pass', 'fail' )
	elif trend == 'below_sma':
		df[trial] = np.where( df[column] <= df['temp_ma'], 'pass', 'fail' )
	else:
		df[trial] = 'error'

	# clean up temp columns
	df.drop(['temp_ma'], axis=1, inplace=True)

	# ensure Screener_df is back in its descending order (latest first)
	df.sort_values(by=['date'], inplace=True, ascending=False)


