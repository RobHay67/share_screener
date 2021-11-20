import numpy as np

# thinking is that the last leter will refer to the appropriate col on which the trend is based
# we need trend lines - which are over some time frame / or \ to indicate a trend
# ^ or v for today

# The Relative Strength Index (RSI) is a momentum oscillator
# - traders use the RSI as a confirmation of other trends rather than an indicator in its own right
# The Moving Average Convergence Divergence (MACD) is a momentum and trend indicator
# The Volume Weighted Average Price (VWAP) is used to reveal the true average price that a stock was traded at durin
# The stochastic oscillator is a momentum indicator 


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Internal Libraries
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# from trading_diary import update_trade_ledger

# def report_function( params, message ):
# 	if params.terminal['audit']:
# 		print ( '' + white)
# 		print ( 'function > ' + yellow + message + white)





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Trend Lines - Basic
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# def line_sma( params, share_df, column, no_of_days=10 ):   
# 	# add a simple moving average
# 	print ( f'trend - SMA on {column}, number of days = {no_of_days}' )
# 	sma_col = ( 'sma_' +  str(no_of_days) + '_' + str(column[:1]) )
# 	if sma_col not in params.chart_lines: 
# 		params.chart_lines.append(sma_col)
	
# 	share_df[sma_col] = share_df[column].rolling(window=no_of_days).mean()
	
# 	return share_df

# def line_ema( params, share_df, column, no_of_days, temp_ema=False ):
# 	# add an Exponential Moving Average (EMA)
# 	# EMA  = https://www.investopedia.com/terms/e/ema.asp
# 	print ( f'trend - EMA on {column}, number of days = {no_of_days}' )
# 	ema_name =  ( 'ema_' +  str(no_of_days) + '_' + str(column[:1]) )
# 	if column != 'volume':  # volume will not be in the price chart - its in a seperate chart
# 		if ema_name not in params.chart_lines: 
# 			params.chart_lines.append(ema_name)
	
# 	share_df[ema_name] = share_df[column].ewm(span=no_of_days, adjust=False).mean()
# 	return share_df

# def volume_per_minute(params, share_df, ticker ):
# 	report_function( params, f'Volume Per Minute' )
# 	minutes_per_day = params.share_index['file'].loc[ticker]['minutes_per_day']
# 	share_df['vpm'] = (share_df['volume'] / minutes_per_day).astype(int)
# 	return share_df 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Complex measure with trend Lines
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def trend_sma_50_low( params, share_df ):
	# report_function( params, f'Simple Moving Average on low price - number of days = 50' )
	share_df['sma'] = share_df['low'].rolling(window=50).mean()
	share_df['sma_50_l'] = np.where( share_df['low'] > share_df['sma'], '^', 'v' ) 		# add the trend direction
	share_df.drop([ 'sma'], axis=1, inplace=True)	
	return share_df 

def recent_price_moves( params, share_df, lookback_days=5 ):
	for column in params.strategy['price_columns'] + ['volume']:
		# report_function( params, f'Price direction on {column} today and over the past {lookback_days} days' )
		trend_col_name = 'c_' + str(column[:1])
		lookback_col_name = 'lb_' + str(column[:1])		
		share_df['yesterday'] = np.where( share_df[column] > share_df[column].shift(1), 1, 0 )
		share_df[trend_col_name] = np.where( share_df['yesterday'] == 1, 'U', 'D' )
		share_df[lookback_col_name] = share_df['yesterday'].rolling(lookback_days, min_periods=1).sum().astype(int)
		share_df.drop([ 'yesterday'], axis=1, inplace=True)	
	return share_df

# def macd( params, share_df, short=12, long=26, signal=9):
# 	# Moving Average, Convergence, Divergence (MACD)
# 	# MACD = https://www.investopedia.com/terms/m/macd.asp
# 	for column in params.strategy['price_columns'] + ['volume']:
# 		report_function( params, f'MACD on {column} (short={short}, long={long}, signal={signal})' )
# 		macd_trend_column_name = 'macd_' +  str(column[:1])
# 		macd_cross_column_name = 'macd_x_' +  str(column[:1])
# 		macd_histo_strength    = 'macd_s_' +  str(column[:1])
		
# 		share_df['short_ma'] 		= share_df[column].ewm(span=short, adjust=False).mean()
# 		share_df['long_ma']  		= share_df[column].ewm(span=long, adjust=False).mean()
# 		share_df['macd_col'] 		= share_df['short_ma'] - share_df['long_ma']							# black line on ANZ Share Investing
# 		share_df['signal_col'] 		= share_df['macd_col'].ewm(span=signal, adjust=False).mean()			# red line on ANZ Share Investing
# 		share_df['histogram_col'] 	= share_df['macd_col'] - share_df['signal_col']							# red & green bar chart on ANZ Share Investing

# 		# trend direction - when the histogram changes direction - this signals a buy
# 		share_df[macd_trend_column_name] = np.where( share_df['histogram_col'] > share_df['histogram_col'].shift(1), 'U', 'D')

# 		# tag point of crossover
# 		share_df['above_or_below']	= np.where( share_df['macd_col'] > share_df['signal_col'], 1, 0 )				# Above or Below    1 = MACD is above Signal line. 0 = the MACD is below the signal line
# 		share_df[macd_cross_column_name] = share_df['above_or_below'].diff().fillna(0).astype(int)					# Point of Change   1 = cross in up direction and -1 cross down
# 		share_df[macd_cross_column_name] =  np.where( ( share_df[macd_cross_column_name] == +1), 'x_up',
# 											np.where( ( share_df[macd_cross_column_name] == -1), 'x_dn', 'other' ) )
		
# 		share_df[macd_histo_strength] = np.where( (share_df['macd_col'] >= -0.5 ) & (share_df['macd_col'] <= 0.5), 'w', 'S')


# 		share_df.drop([ 'short_ma', 'long_ma', 'macd_col', 'signal_col', 'histogram_col', 'above_or_below'], axis=1, inplace=True)
# 	return share_df

def highs_and_lows( params, share_df ):

	for column in params.strategy['price_columns'] + ['volume']:
		# report_function( params, f'peaks and troughs on {column}' ) 
		p_and_t_col_name = 'pt_' +  str(column[:1])

		share_df['highs'] 	= np.where( share_df[column] > share_df[column].shift(1), share_df[column], 0)  # peaks   today is > yesterday so its a high
		share_df['highs'] 	= share_df['highs'].replace(to_replace=0, method='ffill')
		share_df['lows'] 	= np.where( share_df[column] < share_df[column].shift(1), share_df[column], 0) # troughs
		share_df['lows'] 	= share_df['lows'].replace(to_replace=0, method='ffill')

		share_df[p_and_t_col_name] 	= 	np.where( ( share_df['highs'] >  share_df['highs'].shift(1) ), 'HH', 
										np.where( ( share_df['highs'] <  share_df['highs'].shift(1) ), 'LH',   
										np.where( ( share_df['lows']  >  share_df['lows'].shift(1)  ), 'HL', 
										np.where( ( share_df['lows']  <  share_df['lows'].shift(1)  ), 'LL', 'EE' ) ) ) )
		share_df.drop(['highs', 'lows'], axis=1, inplace=True)
	return share_df
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Momentum Oscillation
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# What is the ROC  - Rate of Change
# https://www.investopedia.com/terms/r/rateofchange.asp

# def rsi( params, share_df, no_of_days=14 ):
# 	# RSI = https://www.investopedia.com/terms/r/rsi.asp
# 	for column in params.strategy['price_columns']+ ['volume']:
# 		report_function( params, f'RSI on {column} number of days = {no_of_days}' )
# 		rsi_trend_col_name 		= 'rsi_' +  str(column[:1])

# 		share_df['rsi_delta'] 	= share_df[column].diff()
# 		share_df['rsi_up']		= np.where(share_df['rsi_delta'] >= 0, share_df['rsi_delta']     , 0)
# 		share_df['rsi_down']  	= np.where(share_df['rsi_delta'] <  0, share_df['rsi_delta'] * -1, 0)
# 		share_df['avg_ups'] 	= share_df['rsi_up'].rolling(window=no_of_days).mean()
# 		share_df['avg_downs'] 	= share_df['rsi_down'].rolling(window=no_of_days).mean()
# 		share_df['RS']           = share_df['avg_ups'] / share_df['avg_downs']
		
# 		share_df[rsi_trend_col_name] = 100 - ( 100 / ( share_df['RS'] + 1 ))
# 		share_df[rsi_trend_col_name] = share_df[rsi_trend_col_name].replace(np.nan, 0)
# 		share_df[rsi_trend_col_name] = ( share_df[rsi_trend_col_name] / 10 ).astype(int)
# 		# share_df[rsi_trend_col_name] = np.where( share_df[rsi_trend_col_name] > 50.0, 'A', 'B' )

# 		# share_df.drop(['rsi_delta', 'rsi_up', 'rsi_down', 'avg_ups', 'avg_downs', 'RS'], axis=1, inplace=True)
# 	return( share_df )

# def stochastic_oscillator(params, share_df, lookback_days=14, slow_k=3, signal=3):
# 	# https://www.investopedia.com/terms/s/stochasticoscillator.asp
# 	# https://school.stockcharts.com/doku.php?id=technical_indicators:stochastic_oscillator_fast_slow_and_full
# 	report_function( params, f'stochastic oscillator (lookback days ={lookback_days}, slow k={slow_k}, signal={signal})' ) 
# 	share_df['highest_high'] 	= share_df['high'].rolling(window=lookback_days).max()
# 	share_df['lowest_low'] 		= share_df['low'].rolling(window=lookback_days).min()
# 	share_df['fast_K'] 			= ( ( (share_df['close'] - share_df['lowest_low']) / (share_df['highest_high'] - share_df['lowest_low']) ) * 100 )
# 	share_df['fast_D'] 			= share_df['fast_K'].rolling(window=3).mean()
# 	share_df['slow_K'] 			= share_df['fast_K'].rolling(window=slow_k).mean()							# ANZ - stoch_length = 14    (black)
# 	share_df['slow_D'] 			= share_df['slow_K'].rolling(window=signal).mean()							# ANZ - signal_length = 3    (red)    utilises the signal

# 	share_df['above_or_below'] 	= np.where( share_df['slow_K'] > share_df['slow_D'], 1, 0 )					# Above or Below    1 = slow_k is above Signal line. 0 = the slow_k is below the signal line
# 	share_df['stoch_x'] 		= share_df['above_or_below'].diff().fillna(0).astype(int)					# Point of Change   1 = cross in up direction and -1 cross down
# 	share_df['stoch_x'] 		=  np.where( ( share_df['stoch_x'] == +1), 'x_up',
# 								   np.where( ( share_df['stoch_x'] == -1), 'x_dn', '--') )
# 	# share_df['stoch_trend'] 	= np.where( share_df['slow_K'] > share_df['slow_D'].shift(1), '/', '\\' )
# 	share_df['stoch_zone']		=   np.where( ( share_df['slow_K'] > 80), 'sell', 
# 									np.where( ( share_df['slow_K'] < 20), 'buy', '----' ) )

# 	# share_df['stoch_recommendation'] = 	np.where( (share_df['stoch_zone'] == 'buy_zone' ) & (share_df['stoch_x'] == 'x_up'), 'buy___signal', 
# 	# 									np.where( (share_df['stoch_zone'] == 'sell_zone') & (share_df['stoch_x'] == 'x_dn'), 'prepare_sell', '------------' ) )
# 	# print ( share_df.tail(20))
# 	share_df.drop(['highest_high', 'lowest_low', 'above_or_below'], axis=1, inplace=True)
	
	
# 	# 1) identify overbrought and oversold regions and look for reversals
# 	# 2) cross overs as buy and sell signals
# 	# 3) divergences between price and the oscillator


# 	return share_df



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Technical Analysis measures (traditional)
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def add_rsi( params, share_df, column, no_of_days=14):
	# Add an RSI
	# RSI = https://www.investopedia.com/terms/r/rsi.asp
	if params.terminal['audit']: print ( 'trend - RSI on', column, 'number of days =', no_of_days )

	share_df['rsi_delta'] = share_df[column].diff()
	share_df['rsi_high']  = np.where(share_df['rsi_delta'] >= 0, share_df['rsi_delta']     , 0)
	share_df['rsi_lows']  = np.where(share_df['rsi_delta'] <  0, share_df['rsi_delta'] * -1, 0)
	
	cum_sum_rsi_high, cum_sum_rsi_lows = 0, 0
	avg_rsi_high, avg_rsi_lows         = np.nan, np.nan    
	avg_high_list, avg_lows_list       = [], []

	for row_no in range(len(share_df)):
		cum_sum_rsi_high = cum_sum_rsi_high + share_df['rsi_high'][row_no]
		cum_sum_rsi_lows = cum_sum_rsi_lows + share_df['rsi_lows'][row_no]
		
		if row_no == (no_of_days):
			avg_rsi_high = cum_sum_rsi_high / no_of_days
			avg_rsi_lows = cum_sum_rsi_lows / no_of_days
		elif row_no > no_of_days:
			avg_rsi_high = ( previous_avg_rsi_high * (no_of_days - 1) + share_df['rsi_high'][row_no] ) / no_of_days 
			avg_rsi_lows = ( previous_avg_rsi_lows * (no_of_days - 1) + share_df['rsi_lows'][row_no] ) / no_of_days 

		avg_high_list.append( avg_rsi_high )
		avg_lows_list.append( avg_rsi_lows )
		
		previous_avg_rsi_high = avg_rsi_high
		previous_avg_rsi_lows = avg_rsi_lows
	
	
	share_df['avg_rsi_high'] = avg_high_list
	share_df['avg_rsi_lows'] = avg_lows_list
   
	share_df['RS']           = share_df['avg_rsi_high'] / share_df['avg_rsi_lows']
	share_df['rsi']          = 100 - ( 100 / ( share_df['RS'] +1 ))
	
	share_df.drop(['rsi_delta', 'rsi_high', 'rsi_lows', 'avg_rsi_high', 'avg_rsi_lows', 'RS'], axis=1, inplace=True)
	
	return( share_df )




