import logging
from add_cols.functions.trend import trend_cols
from add_cols.functions.sma import sma_trend
from add_cols.functions.rsi import rsi_trend
from add_cols.functions.stochastic import stochastic_trend

def scope_trials_schema(scope):
	logging.debug("scope_trials_schema")
	scope.trials['schema'] = trials_schema
# ==============================================================================================================================================================
# Share Screener Trial Specifications (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The Analysis is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the Analysis (used in the settings Page)
short_name		= 'short_name'			# A short name used for various Screen Outputs
definition		= 'definition'			# URL link to the definition for this chart or overlay

column 			= 'column'				# OHLCV column required for the Analysis
duration		= 'duration'			# the length or number of consecutive occurances
timespan 		= 'timespan'			# The entire analysis Period
trend			= 'trend'				# the trend or direction of the trend - up or down / above or below
function		= 'function'			# Dictionary of Dataframe Column Params	
function		= 'function'			# The function to add the columns for this schema_key

periods 		= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
short 			= 'short'				# for the MACD
signal 			= 'signal'				# Stochastic
lookback_days 	= 'lookback_days'		# Stochastic Oscillator
slow 			= 'slow'				# Stochastic Oscillator

# 

trends_for_ohlcv 		= [ 'up', 'down' ]
trends_for_sma 			= ['above', 'below']
trends_for_stochastic 	= ['above_line', 'below_line', 'over_bought', 'over_sold', 'cross_up', 'cross_down']
trends_for_rsi 			= ['up', 'down', 'over bought', 'over sold' ]


trials_schema = {
	'price_1'	: {
						active			: False,
						name			: 'Price Direction (OHLCV)',
						short_name		: 'Price Direction (OHLCV)',
						definition		: 'https://www.investopedia.com/terms/o/openingprice.asp',
						function		: {
											function : trend_cols,
											column 	 : 'close',
											trend	 : 'up',
											duration : 4,
											timespan : 10,
										},
					},
	'price_2'	: {
						active			: False,
						name			: 'Price Direction (OHLCV)',
						short_name		: 'Price Direction (OHLCV)',
						definition		: 'https://www.investopedia.com/terms/c/closingprice.asp',
						function		: {
											function : trend_cols,
											column 	 : 'high',
											trend	 : 'up',
											duration : 4,
											timespan : 10,
										},
					},
	'price_3'		: {
						active			: False,
						name			: 'Price Direction (OHLCV)',
						short_name		: 'Price Direction (OHLCV)',
						definition		: '',
						function		: {
											function : trend_cols,
											column 	 : 'volume',
											trend	 : 'up',
											duration : 4,
											timespan : 10,
										},
					},
	'sma_1' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 1',
						definition		: 'https://www.investopedia.com/terms/s/sma.asp',
						function		: {
											function : sma_trend,
											column 	 : 'close',
											trend	 : 'above',
											periods  : 21,
										},
					},
	'sma_2' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 2',
						definition		: 'https://www.investopedia.com/terms/s/sma.asp',
						function		: {
											function : sma_trend,
											column 	 : 'open',
											trend	 : 'above',
											periods  : 50,
										},
					},
	'sma_3' 	: {
						active			: False,
						name			: 'OHLCV Trending Above or Below SMA',
						short_name		: 'SMA Trend 3',
						definition		: 'https://www.investopedia.com/terms/s/sma.asp',
						function		: {
											function : sma_trend,
											column 	 : 'volume',
											trend	 : 'above',
											periods  : 200,
										},
					},	
	'stochastic_1' 	: {
						active			: True,
						name			: 'Stochastic',
						short_name		: 'Stochastic',
						definition		: 'https://www.investopedia.com/terms/s/stochasticoscillator.asp',
						function		: {
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
						definition		: 'https://www.investopedia.com/terms/s/stochasticoscillator.asp',
						function		: {
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
						definition		: 'https://www.investopedia.com/terms/s/stochasticoscillator.asp',
						function		: {
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
						definition		: 'https://www.investopedia.com/terms/r/rsi.asp',
						function		: {
											function 		: rsi_trend,
											trend	 		: 'upwards',
											column 	 		: 'close',
											lookback_days 	: 10,
										},
					},
	'rsi_2' 		: {
						active			: True,
						name			: 'RSI-2',
						short_name		: 'RSI-2',
						definition		: 'https://www.investopedia.com/terms/r/rsi.asp',
						function		: {
											function 		: rsi_trend,
											trend	 		: 'over_sold',
											column 	 		: 'open',
											lookback_days 	: 10,
										},
					},

}
