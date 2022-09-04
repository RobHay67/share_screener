
def scope_trials(scope):

	scope.trial_config = {}
	scope.trial_config['trend_directions'] = trend_directions
	scope.trial_config['sma_directions'] = sma_directions

	scope.trial_config['trial_list'] = list(trials_config.keys())

	scope.trials = {}
	for trial, config in trials_config.items():
		scope.trials[trial] = config
	
	trial_active_list(scope)

	trial_column_adders(scope)


def trial_active_list(scope):
	# Seperate function so it can be called after the initial load - i.e. change user

	# Reset the list as this function will rebuild it
	scope.trial_config['active_list'] = []

	for trial in scope.trial_config['trial_list']:	
		if scope.trials[trial]['active'] == True:
			scope.trial_config['active_list'].append(trial)


def trial_column_adders(scope):
	# Seperate function so it can be called after the initial load - i.e. change user

	# Reset the dictionary as this function will rebuild it
	scope.trial_config['column_adders'] = {}

	for trial in scope.trial_config['trial_list']:
		# Add charts that require additional columns
		if scope.trials[trial]['add_columns'] != None:
			scope.trial_config['column_adders'][trial] = scope.trials[trial]['active']








from add_cols.trend import trend_cols
from add_cols.sma import sma_trend


# ==============================================================================================================================================================
# Share Screener Trial Specifications (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings app)
column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down / above or below
add_columns		= 'add_columns'			# Dictionary of Dataframe Column Params	
function		= 'function'			# The function to add the columns for this column_adder

periods 		= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here


# 
trend_directions = [ 'up', 'down' ]
sma_directions = ['above', 'below']



trials_config = {
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
	'sma_open' 		: {
						active			: True,
						name			: 'Open SMA',
						add_columns		: {
											function : sma_trend,
											column 	 : 'open',
											trend	 : 'above',
											periods : 21,
										},
					},
	'sma_high' 		: {
						active			: True,
						name			: 'High SMA',
						add_columns		: {
											function : sma_trend,
											column 	 : 'high',
											trend	 : 'above',
											periods : 21,
										},
					},
	'sma_low' 		: {
						active			: True,
						name			: 'Low SMA',
						add_columns		: {
											function : sma_trend,
											column 	 : 'low',
											trend	 : 'above',
											periods : 21,
										},
					},

	'sma_close' 	: {
						active			: True,
						name			: 'Close SMA',
						add_columns		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above',
											periods : 21,
										},
					},
	'sma_volume' 	: {
						active			: True,
						name			: 'Volume SMA',
						add_columns		: {
											function : sma_trend,
											column 	 : 'volume',
											trend	 : 'above',
											periods : 21,
										},
					},
}


