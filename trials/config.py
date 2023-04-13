# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!






def scope_trials(scope):

	scope.trials = {}

	scope.trials['trial_list'] = list(trial_configuration_dict.keys())

	# store the trial configuration dictionary (from below)
	scope.trials['config'] = {}
	for trial, configuration in trial_configuration_dict.items():
		scope.trials['config'][trial] = configuration
	
	trial_active_list(scope)

	trial_column_adders(scope)


def trial_active_list(scope):
	# a list of every currently active trial
	# Seperate function so it can be called after the initial load - i.e. change user

	# Reset the list as this function will rebuild it
	scope.trials['active_list'] = []

	for trial in scope.trials['trial_list']:	
		if scope.trials['config'][trial]['active'] == True:
			scope.trials['active_list'].append(trial)


def trial_column_adders(scope):
	# A dictionary of every trial that requires additional columns
	# ignore and trials that dont have column adders
	# Seperate function so it can be called after the initial load - i.e. change user

	# Reset the dictionary as calling this function will recreate the dictionary
	scope.trials['template_col_adders'] = {}

	for trial in scope.trials['trial_list']:
		if scope.trials['config'][trial]['add_columns'] != None:
		# Add trials that require additional columns
			active_status_of_trial = scope.trials['config'][trial]['active']
			scope.trials['template_col_adders'][trial] = active_status_of_trial



from add_cols.trend import trend_cols
from add_cols.sma import sma_trend
from add_cols.stochastic import stochastic_trend
from add_cols.rsi import rsi_trend




# ==============================================================================================================================================================
# Share Screener Trial Specifications (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings Page)
short_name		= 'short_name'			# A short name used if various Screen Outputs

column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the lenght or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down / above or below
add_columns		= 'add_columns'			# Dictionary of Dataframe Column Params	
function		= 'function'			# The function to add the columns for this config_key

periods 		= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
short 			= 'short'				# for the MACD
signal 			= 'signal'				# Stochastic
lookback_days 	= 'lookback_days'		# Stochastic Oscillator
slow 			= 'slow'				# Stochastic Oscillator

# 
trends_for_sma 	= ['above_sma', 'below_sma']
trends_for_ohlcv = [ 'up_trend', 'down_trend' ]



trends_for_stochastic = ['above_line', 'below_line', 'over_bought', 'over_sold', 'cross_up', 'cross_down']
trends_for_rsi = ['up_trend', 'down_trend', 'over_bought', 'over_sold' ]


trial_configuration_dict = {
	'price_1'	: {
						active			: False,
						name			: 'OHLCV Price Direction',
						short_name		: 'OHLCV Price Direction',
						add_columns		: {
											function : trend_cols,
											column 	 : 'close',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'price_2'	: {
						active			: False,
						name			: 'OHLCV Price Direction',
						short_name		: 'OHLCV Price Direction',
						add_columns		: {
											function : trend_cols,
											column 	 : 'high',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'price_3'		: {
						active			: False,
						name			: 'OHLCV Price Direction',
						short_name		: 'OHLCV Price Direction',
						add_columns		: {
											function : trend_cols,
											column 	 : 'volume',
											trend	 : 'up_trend',
											duration : 4,
											timespan : 10,
										},
					},
	'sma_1' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 1',
						add_columns		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above_sma',
											periods  : 21,
										},
					},
	'sma_2' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 2',
						add_columns		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above_sma',
											periods  : 50,
										},
					},
	'sma_3' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 3',
						add_columns		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above_sma',
											periods  : 200,
										},
					},	
	'stochastic_1' 	: {
						active			: True,
						name			: 'Stochastic',
						short_name		: 'Stochastic',
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
						short_name		: 'Stochastic',
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
						short_name		: 'Stochastic',
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
						name			: 'RSI-1',
						short_name		: 'RSI-1',
						add_columns		: {
											function 		: rsi_trend,
											trend	 		: 'up_trend',
											column 	 		: 'close',
											lookback_days 	: 10,
										},
					},
	'rsi_2' 		: {
						active			: True,
						name			: 'RSI-2',
						short_name		: 'RSI-2',
						add_columns		: {
											function 		: rsi_trend,
											trend	 		: 'over_sold',
											column 	 		: 'close',
											lookback_days 	: 10,
										},
					},

}
