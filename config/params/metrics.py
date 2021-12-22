

from metrics.model.trend import trend_cols



# ==============================================================================================================================================================
# Analysis Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================
metric_function = 'metric_function'		# The function to add the columns for this metric
active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings page)
column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down




trend_direction = [ 'up', 'down' ]



metrics_config = {
					'trend_open'	: {
										active			: False,
										name			: 'Open trend',
										column 			: 'open',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
										metric_function	: trend_cols,
									},
					'trend_high'	: {
										active			: True,
										name			: 'High trend',
										column 			: 'high',
										trend			: 'up',
										duration		: 5,
										timespan		: 5,
										metric_function	: trend_cols,
									},
					'trend_low'	: {
										active			: False,
										name			: 'Low trend',
										column 			: 'low',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
										metric_function	: trend_cols,
									},
					'trend_close'	: {
										active			: False,
										name			: 'Close trend',
										column 			: 'close',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
										metric_function	: trend_cols,
									},
					'trend_volume'	: {
										active			: False,
										name			: 'Volume trend',
										column 			: 'volume',
										trend			: 'up',
										duration		: 4,
										timespan		: 10,
										metric_function	: trend_cols,
									},
					}
