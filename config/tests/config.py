from add_cols.trend import trend_cols




# ==============================================================================================================================================================
# Share Screener Test Specifications (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings page)
column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down
add_columns		= 'add_columns'				# Dictionary of Dataframe Column Params	
function		= 'function'			# The function to add the columns for this metric


# 
trend_direction = [ 'up', 'down' ]



tests_config = {
	'trend_open'	: {
						active			: False,
						name			: 'Open trend',
						add_columns		: {
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
						add_columns		: {
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
						add_columns		: {
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
						add_columns		: {
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
						add_columns		: {
											function : trend_cols,
											column 	 : 'volume',
											trend	 : 'up',
											duration : 4,
											timespan : 10,
										},
					},
}



