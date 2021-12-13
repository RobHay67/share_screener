



# ==============================================================================================================================================================
# Analysis Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings page)
column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down




trend_direction = [ 'up', 'down' ]



trend_schema = {
					'trend_open'	: {
										active			: True,
										name			: 'Trend of Open Price',
										column 			: 'open',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
									},
					'trend_high'	: {
										active			: True,
										name			: 'Trend of High Price',
										column 			: 'high',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
									},
					'trend_low'	: {
										active			: True,
										name			: 'Trend of Low Price',
										column 			: 'low',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
									},
					'trend_close'	: {
										active			: True,
										name			: 'Trend of Close Price',
										column 			: 'close',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
									},
					'trend_volume'	: {
										active			: True,
										name			: 'Trend of Volume',
										column 			: 'volume',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
									},
					}


def scope_screener(scope):
	
	scope.screener_trends 	= trend_schema
	scope.screener_trend = trend_direction



	

	# scope.volume_trend = 'up'
	# scope.volume_lookback_days = 3

	# scope.rsi_level = 0.50
	# scope.rsi_column = 'close'

	# scope.macd_direction = 'up'
	# scope.macd_strength = 'strong'


	# scope.sma_line = 'above'
	# scope.ema_line = 'above'