
import numpy as np




def stoch_cols( scope, chart, ticker, chart_df):
	# Stochastic Oscillator
	
	# 1) identify overbrought and oversold regions and look for reversals
	# 2) cross overs as buy and sell signals
	# 3) divergences between price and the oscillator

	# https://www.investopedia.com/terms/s/stochasticoscillator.asp

	# https://school.stockcharts.com/doku.php?id=technical_indicators:stochastic_oscillator_fast_slow_and_full


	lookback_days	= int(scope.charts['config'][chart]['add_columns']['lookback_days'])
	signal 			= scope.charts['config'][chart]['add_columns']['signal']
	slow_k 			= scope.charts['config'][chart]['add_columns']['slow']

	# Change chart_df to be ascending to simplify the shifting
	chart_df.sort_values(by=['date'], inplace=True, ascending=True)

	chart_df['highest_high'] 	= chart_df['high'].rolling(window=lookback_days).max()
	chart_df['lowest_low'] 		= chart_df['low'].rolling(window=lookback_days).min()
	chart_df['stoch_fast_K'] 	= ( ( (chart_df['close'] - chart_df['lowest_low']) / (chart_df['highest_high'] - chart_df['lowest_low']) ) * 100 )
	
	chart_df['stoch_fast_D'] 	= chart_df['stoch_fast_K'].rolling(window=3).mean()
	chart_df['stoch_slow_K'] 	= chart_df['stoch_fast_K'].rolling(window=slow_k).mean()							# ANZ - stoch_length = 14    (black)
	chart_df['stoch_slow_D'] 	= chart_df['stoch_slow_K'].rolling(window=signal).mean()							# ANZ - signal_length = 3    (red)    utilises the signal

	chart_df['stoch_slow_K'] = chart_df['stoch_slow_K'] / 100
	chart_df['stoch_slow_D'] = chart_df['stoch_slow_D'] / 100

	chart_df['stoch_overbuy'] 	= 0.8
	chart_df['stoch_oversold'] 	= 0.2

	chart_df['above_or_below'] 	= np.where( chart_df['stoch_slow_K'] > chart_df['stoch_slow_D'], 1, 0 )			# Above or Below    1 = slow_k is above Signal line. 0 = the slow_k is below the signal line
	chart_df['stoch_x'] 		= chart_df['above_or_below'].diff().fillna(0).astype(int)						# Point of Change   1 = cross in up direction and -1 cross down
	chart_df['stoch_x'] 		= np.where( ( chart_df['stoch_x'] == +1), 'x_up',
								  np.where( ( chart_df['stoch_x'] == -1), 'x_dn', '--') )

	chart_df['stoch_zone']		=   np.where( ( chart_df['stoch_slow_K'] > 80), 'sell', 
									np.where( ( chart_df['stoch_slow_K'] < 20), 'buy', '----' ) )

	chart_df.drop(['highest_high', 'lowest_low', 'above_or_below'], axis=1, inplace=True)

	# ensure Screener_df is back in its descending order (latest first)
	chart_df.sort_values(by=['date'], inplace=True, ascending=False)




def stochastic_trend( scope, trial, ticker, df):

	trend 			= scope.trials['config'][trial]['add_columns']['trend']
	lookback_days	= int(scope.trials['config'][trial]['add_columns']['lookback_days'])
	signal 			= scope.trials['config'][trial]['add_columns']['signal']
	slow_k 			= scope.trials['config'][trial]['add_columns']['slow']


	# Change df to be ascending to simplify the shifting
	df.sort_values(by=['date'], inplace=True, ascending=True)

	df['temp_highest_high'] = df['high'].rolling(window=lookback_days).max()
	df['temp_lowest_low'] 	= df['low'].rolling(window=lookback_days).min()
	df['temp_stoch_fast_K'] = ( ( (df['close'] - df['temp_lowest_low']) / (df['temp_highest_high'] - df['temp_lowest_low']) ) * 100 )
	
	df['temp_stoch_fast_D'] = df['temp_stoch_fast_K'].rolling(window=3).mean()
	df['temp_stoch_slow_K'] = df['temp_stoch_fast_K'].rolling(window=slow_k).mean()							# ANZ - stoch_length = 14    (black)
	df['temp_stoch_slow_D'] = df['temp_stoch_slow_K'].rolling(window=signal).mean()							# ANZ - signal_length = 3    (red)    utilises the signal

	df['temp_stoch_slow_K'] = df['temp_stoch_slow_K'] / 100
	df['temp_stoch_slow_D'] = df['temp_stoch_slow_D'] / 100

	# Add some values to assist with working out if the trial passed or failed
	df['temp_above_or_below'] 	 = np.where( df['temp_stoch_slow_K'] > df['temp_stoch_slow_D'], 1, 0 )			# Above or Below    1 = slow_k is above Signal line. 0 = the slow_k is below the signal line	
	df['temp_stoch_cross_point'] = df['temp_above_or_below'].diff().fillna(0).astype(int)						# Point of Change   1 = cross in up direction and -1 cross down

	# Determine the Result for each row
	if trend == 'above_line':
		df[trial] = np.where( df['temp_stoch_slow_K'] > df['temp_stoch_slow_D'], 'pass', 'fail')
	elif trend == 'below_line':
		df[trial] = np.where( df['temp_stoch_slow_K'] <= df['temp_stoch_slow_D'], 'pass', 'fail')
	elif trend == 'over_bought':
		df[trial] = np.where( df['temp_stoch_slow_K'] > 0.8, 'pass', 'fail')
	elif trend == 'over_sold':
		df[trial] = np.where( df['temp_stoch_slow_K'] < 0.2, 'pass', 'fail')
	elif trend == 'cross_up':
		df[trial] = np.where( df['temp_stoch_cross_point'] == +1, 'pass', 'fail')
	elif trend == 'cross_down':
		df[trial] = np.where( df['temp_stoch_cross_point'] == -1, 'pass', 'fail')
	else:
		df[trial] = 'fail'

	# Clean up Temp Columns	
	df.drop(['temp_highest_high', 'temp_lowest_low', 'temp_stoch_fast_D', 'temp_stoch_slow_K', 'temp_stoch_slow_D','temp_above_or_below', 'temp_stoch_cross_point'], axis=1, inplace=True)

	# ensure Screener_df is back in its descending order (latest first)
	df.sort_values(by=['date'], inplace=True, ascending=False)

