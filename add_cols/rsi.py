

import numpy as np



def rsi_cols(scope, chart, ticker, chart_df):
	# Relative Strength Index (RSI)
	
	# RSI = https://www.investopedia.com/terms/r/rsi.asp

	# https://www.alpharithms.com/relative-strength-index-rsi-in-python-470209/   Python Calculation methodology

	column 			= scope.charts['config'][chart]['add_columns']['column']
	lookback_days	= int(scope.charts['config'][chart]['add_columns']['lookback_days'])

	# Change chart_df to be ascending to simplify the shifting
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)

	chart_df['rsi_delta'] 		= chart_df[column].diff()
	chart_df['rsi_gain']		= np.where(chart_df['rsi_delta'] >= 0, chart_df['rsi_delta']     , 0)
	chart_df['rsi_loss']  		= np.where(chart_df['rsi_delta'] <  0, chart_df['rsi_delta'] * -1, 0)
	chart_df['rsi_avg_gains'] 	= chart_df['rsi_gain'].rolling(window=lookback_days).mean()
	chart_df['rsi_avg_losses'] 	= chart_df['rsi_loss'].rolling(window=lookback_days).mean()
	chart_df['rsi_rs']          = chart_df['rsi_avg_gains'] / chart_df['rsi_avg_losses']
	chart_df['rsi']          	= 100 - ( 100 / ( chart_df['rsi_rs'] +1 ))

	chart_df['rsi'] = chart_df['rsi'] / 100

	chart_df['rsi_overbuy'] 	= 0.7
	chart_df['rsi_oversold'] 	= 0.3

	chart_df['rsi_trend'] = 100 - ( 100 / ( chart_df['rsi_rs'] + 1 ))
	chart_df['rsi_trend'] = chart_df['rsi_trend'].replace(np.nan, 0)
	chart_df['rsi_trend'] = ( chart_df['rsi_trend'] / 10 ).astype(int)

	# ensure df is back in its descending order (latest first)
	chart_df.sort_values(by=['date'], inplace=True, ascending=False)


def rsi_trend(scope, trial, ticker, df):

	trend 			= scope.trials['config'][trial]['add_columns']['trend']
	column 			= scope.trials['config'][trial]['add_columns']['column']
	lookback_days	= int(scope.trials['config'][trial]['add_columns']['lookback_days'])

	# Change chart_df to be ascending to simplify the shifting
	df.sort_values(by=['date'], inplace=True, ascending=True)

	df['rsi_delta'] 	 = df[column].diff()
	df['rsi_gain']		 = np.where(df['rsi_delta'] >= 0, df['rsi_delta']     , 0)
	df['rsi_loss']  	 = np.where(df['rsi_delta'] <  0, df['rsi_delta'] * -1, 0)
	df['rsi_avg_gains']  = df['rsi_gain'].rolling(window=lookback_days).mean()
	df['rsi_avg_losses'] = df['rsi_loss'].rolling(window=lookback_days).mean()
	df['rsi_rs']         = df['rsi_avg_gains'] / df['rsi_avg_losses']
	df['rsi']          	 = 100 - ( 100 / ( df['rsi_rs'] +1 ))

	df['rsi'] = df['rsi'] / 100
	df['rsi_shifted'] = df['rsi'].shift(1)


	# Determine the Result for each row
	if trend == 'up':
		df[trial] = np.where( df['rsi'] >  df['rsi_shifted'], 'pass', 'fail' )
	elif trend == 'down':
		df[trial] = np.where( df['rsi'] <= df['rsi_shifted'], 'pass', 'fail' )
	elif trend == 'over bought':
		df[trial] = np.where( df['rsi'] > 0.7, 'pass', 'fail' )
	elif trend == 'over sold':
		df[trial] = np.where( df['rsi'] < 0.3, 'pass', 'fail' )
	else:
		df[trial] = 'fail'

	print(df.tail(3))
	
	# clean up temp columns
	df.drop(['rsi_delta', 'rsi_gain', 'rsi_loss', 'rsi_avg_gains', 'rsi_avg_losses', 'rsi_rs', 'rsi', 'rsi_shifted'], axis=1, inplace=True)

	# ensure df is back in its descending order (latest first)
	df.sort_values(by=['date'], inplace=True, ascending=False)

	

