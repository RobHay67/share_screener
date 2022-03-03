

from metrics.model.trend import trend_cols



# ==============================================================================================================================================================
# Analysis/Metrics Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings page)
column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down
metrics			= 'metrics'				# Dictionary of Dataframe Column Params	
# metric_function = 'metric_function'		# The function to add the columns for this metric
function		= 'function'			# The function to add the columns for this metric


# 
trend_direction = [ 'up', 'down' ]



		# 'line'				: { 
		# 						active			: True , 
		# 						name			: 'Line charts', 
		# 						is_overlay		: False, 
		# 						add_overlays	: True , 
		# 						plot			: { 
		# 											function	: line_plot, 
		# 											title		: 'Line', 
		# 											scale		: 0.50, 
		# 											yaxis		: '$,.2f' 
		# 										}, 	
		# 						metrics			: {
		# 											function	: None, 
		# 											column		: 'close',
		# 										},
		# 					},


metrics_config = {
					'trend_open'	: {
										active			: False,
										name			: 'Open trend',
										# column 			: 'open',
										# trend			: 'up',
										# duration		: 4,
										# timespan		: 10,
										# metric_function	: trend_cols,
										metrics			: {
															function : trend_cols,
															column 	 : 'open',
															trend	 : 'up',
															duration : 4,
															timespan : 10,
														},
									},
					'trend_high'	: {
										active			: True,
										name			: 'High trend',
										# column 			: 'high',
										# trend			: 'up',
										# duration		: 5,
										# timespan		: 5,
										# metric_function	: trend_cols,
										metrics			: {
															function : trend_cols,
															column 	 : 'high',
															trend	 : 'up',
															duration : 5,
															timespan : 5,
														},
									},
					'trend_low'	: {
										active			: False,
										name			: 'Low trend',
										# column 			: 'low',
										# trend			: 'up',
										# duration		: 4,
										# timespan		: 10,
										# metric_function	: trend_cols,
										metrics			: {
															function : trend_cols,
															column 	 : 'low',
															trend	 : 'up',
															duration : 4,
															timespan : 10,
														},
									},
					'trend_close'	: {
										active			: False,
										name			: 'Close trend',
										# column 			: 'close',
										# trend			: 'up',
										# duration		: 4,
										# timespan		: 10,
										# metric_function	: trend_cols,
										metrics			: {
															function : trend_cols,
															column 	 : 'close',
															trend	 : 'up',
															duration : 4,
															timespan : 10,
														},
									},
					'trend_volume'	: {
										active			: False,
										name			: 'Volume trend',
										# column 			: 'volume',
										# trend			: 'up',
										# duration		: 4,
										# timespan		: 10,
										# metric_function	: trend_cols,
										metrics			: {
															function : trend_cols,
															column 	 : 'volume',
															trend	 : 'up',
															duration : 4,
															timespan : 10,
														},
									},
					}
