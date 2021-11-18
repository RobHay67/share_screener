import numpy as np




def stoch(scope, plot_df, chart):
	# Stochastic Oscillator
	
	# 1) identify overbrought and oversold regions and look for reversals
	# 2) cross overs as buy and sell signals
	# 3) divergences between price and the oscillator

	# https://www.investopedia.com/terms/s/stochasticoscillator.asp

	# https://school.stockcharts.com/doku.php?id=technical_indicators:stochastic_oscillator_fast_slow_and_full


	lookback_days	= scope.charts[chart]['params']['lookback_days']   # lookback days
	signal 			= scope.charts[chart]['params']['signal']
	slow_k 			= scope.charts[chart]['params']['slow']

	plot_df['highest_high'] 	= plot_df['high'].rolling(window=lookback_days).max()
	plot_df['lowest_low'] 		= plot_df['low'].rolling(window=lookback_days).min()
	plot_df['stoch_fast_K'] 	= ( ( (plot_df['close'] - plot_df['lowest_low']) / (plot_df['highest_high'] - plot_df['lowest_low']) ) * 100 )
	print(plot_df)
	
	plot_df['stoch_fast_D'] 	= plot_df['stoch_fast_K'].rolling(window=3).mean()
	plot_df['stoch_slow_K'] 	= plot_df['stoch_fast_K'].rolling(window=slow_k).mean()							# ANZ - stoch_length = 14    (black)
	plot_df['stoch_slow_D'] 	= plot_df['stoch_slow_K'].rolling(window=signal).mean()							# ANZ - signal_length = 3    (red)    utilises the signal

	plot_df['above_or_below'] 	= np.where( plot_df['stoch_slow_K'] > plot_df['stoch_slow_D'], 1, 0 )			# Above or Below    1 = slow_k is above Signal line. 0 = the slow_k is below the signal line
	plot_df['stoch_x'] 			= plot_df['above_or_below'].diff().fillna(0).astype(int)						# Point of Change   1 = cross in up direction and -1 cross down
	plot_df['stoch_x'] 			= np.where( ( plot_df['stoch_x'] == +1), 'x_up',
								  np.where( ( plot_df['stoch_x'] == -1), 'x_dn', '--') )
	# plot_df['stoch_trend'] 	= np.where( plot_df['stoch_slow_K'] > plot_df['stoch_slow_D'].shift(1), '/', '\\' )
	plot_df['stoch_zone']		=   np.where( ( plot_df['stoch_slow_K'] > 80), 'sell', 
									np.where( ( plot_df['stoch_slow_K'] < 20), 'buy', '----' ) )

	# plot_df['stoch_recommendation'] = 	np.where( (plot_df['stoch_zone'] == 'buy_zone' ) & (plot_df['stoch_x'] == 'x_up'), 'buy___signal', 
	# 									np.where( (plot_df['stoch_zone'] == 'sell_zone') & (plot_df['stoch_x'] == 'x_dn'), 'prepare_sell', '------------' ) )

	plot_df.drop(['highest_high', 'lowest_low', 'above_or_below'], axis=1, inplace=True)
	
	



