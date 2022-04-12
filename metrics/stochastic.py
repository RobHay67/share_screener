
import numpy as np




def stoch_cols(scope, chart_df, chart):
	# Stochastic Oscillator
	
	# 1) identify overbrought and oversold regions and look for reversals
	# 2) cross overs as buy and sell signals
	# 3) divergences between price and the oscillator

	# https://www.investopedia.com/terms/s/stochasticoscillator.asp

	# https://school.stockcharts.com/doku.php?id=technical_indicators:stochastic_oscillator_fast_slow_and_full


	lookback_days	= scope.config['charts'][chart]['add_columns']['lookback_days']   # lookback days
	signal 			= scope.config['charts'][chart]['add_columns']['signal']
	slow_k 			= scope.config['charts'][chart]['add_columns']['slow']

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
	# chart_df['stoch_trend'] 	= np.where( chart_df['stoch_slow_K'] > chart_df['stoch_slow_D'].shift(1), '/', '\\' )
	chart_df['stoch_zone']		=   np.where( ( chart_df['stoch_slow_K'] > 80), 'sell', 
									np.where( ( chart_df['stoch_slow_K'] < 20), 'buy', '----' ) )

	# chart_df['stoch_recommendation'] = 	np.where( (chart_df['stoch_zone'] == 'buy_zone' ) & (chart_df['stoch_x'] == 'x_up'), 'buy___signal', 
	# 									np.where( (chart_df['stoch_zone'] == 'sell_zone') & (chart_df['stoch_x'] == 'x_dn'), 'prepare_sell', '------------' ) )

	chart_df.drop(['highest_high', 'lowest_low', 'above_or_below'], axis=1, inplace=True)