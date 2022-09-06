
def scope_trials(scope):

	scope.trial_config = {}

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
from add_cols.stochastic import stochastic_trend
from add_cols.rsi import rsi_trend




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
short 			= 'short'				# for the MACD
signal 			= 'signal'				# Stochastic
lookback_days 	= 'lookback_days'		# Stochastic Oscillator
slow 			= 'slow'				# Stochastic Oscillator

# 
trends_for_ohlcv = [ 'up_trend', 'down_trend' ]
trends_for_sma = ['above_line', 'below_line']
trends_for_stochastic = ['above_line', 'below_line', 'over_bought', 'over_sold', 'cross_up', 'cross_down']
trends_for_rsi = ['up_trend', 'down_trend', 'over_bought', 'over_sold' ]


trials_config = {
	'trend_open'	: {
						active			: False,
						name			: 'Trend of Open Price',
						add_columns		: {
											function : trend_cols,
											column 	 : 'open',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'trend_high'	: {
						active			: False,
						name			: 'Trend of High price',
						add_columns		: {
											function : trend_cols,
											column 	 : 'high',
											trend	 : 'up_trend',
											duration : 5,
											timespan : 5,
										},
					},
	'trend_low'	: {
						active			: False,
						name			: 'Trend of Low price',
						add_columns		: {
											function : trend_cols,
											column 	 : 'low',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'trend_close'	: {
						active			: False,
						name			: 'Trend of Close price',
						add_columns		: {
											function : trend_cols,
											column 	 : 'close',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'trend_volume'	: {
						active			: False,
						name			: 'Trend of Volume',
						add_columns		: {
											function : trend_cols,
											column 	 : 'volume',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'sma_open' 		: {
						active			: False,
						name			: 'Above/Below SMA of Open',
						add_columns		: {
											function : sma_trend,
											column 	 : 'open',
											trend	 : 'above_line',
											periods : 21,
										},
					},
	'sma_high' 		: {
						active			: False,
						name			: 'Above/Below SMA of High',
						add_columns		: {
											function : sma_trend,
											column 	 : 'high',
											trend	 : 'above_line',
											periods : 21,
										},
					},
	'sma_low' 		: {
						active			: False,
						name			: 'Above/Below SMA of Low',
						add_columns		: {
											function : sma_trend,
											column 	 : 'low',
											trend	 : 'above_line',
											periods : 21,
										},
					},

	'sma_close' 	: {
						active			: False,
						name			: 'Above/Below SMA of Close',
						add_columns		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above_line',
											periods : 21,
										},
					},
	'sma_volume' 	: {
						active			: False,
						name			: 'Above/Below SMA of Volume',
						add_columns		: {
											function : sma_trend,
											column 	 : 'volume',
											trend	 : 'above_line',
											periods : 21,
										},
					},
	'stochastic_1' 	: {
						active			: True,
						name			: 'Stochastic',
						add_columns		: {
											function : stochastic_trend,
											trend	 : 'above_line',
											lookback_days	: 14, 
											slow			: 3, 
											signal			: 3,
										},
					},
	'stochastic_2' 	: {
						active			: True,
						name			: 'Stochastic',
						add_columns		: {
											function : stochastic_trend,
											trend	 : 'over_sold',
											lookback_days	: 14, 
											slow			: 3, 
											signal			: 3,
										},
					},
	'stochastic_3' 	: {
						active			: True,
						name			: 'Stochastic',
						add_columns		: {
											function : stochastic_trend,
											trend	 : 'cross_up',
											lookback_days	: 14, 
											slow			: 3, 
											signal			: 3,
										},
					},
	'rsi_1' 		: {
						active			: True,
						name			: 'Above/Below SMA of Open',
						add_columns		: {
											function 		: rsi_trend,
											trend	 		: 'up_trend',
											column 	 		: 'close',
											lookback_days 	: 10,
										},
					},
	'rsi_2' 		: {
						active			: True,
						name			: 'Above/Below SMA of High',
						add_columns		: {
											function 		: rsi_trend,
											trend	 		: 'over_sold',
											column 	 		: 'close',
											lookback_days 	: 10,
										},
					},

}


