# trials_config - all config
# chart_list	- list of chart config keys
# active_list	- list of acttive chart config keys
# column_adders	-  dict of { chart : active_status } (includes active and inactive)



def scope_charts(scope):
	scope.charts = {}
	base_config_charts(scope)
	scope.charts['chart_list'] = list(charts_config.keys())
	scope.charts['colours'] = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	
	chart_active_list(scope)

	chart_column_adders(scope)


def base_config_charts(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.charts['primary_height'] = 500
	scope.charts['total_height'] = scope.charts['primary_height']

	# store the chart configuration dictionary (from below)
	scope.charts['config'] = {}
	for chart, config in charts_config.items():
		scope.charts['config'][chart] = config.copy()
	

def chart_active_list(scope):
	# Seperate function so it can be called after the initial load - i.e. change user
	# Reset the list as this function will rebuild it
	scope.charts['active_list'] = []

	for chart in scope.charts['chart_list']:	
		if scope.charts['config'][chart]['active'] == True:
			scope.charts['active_list'].append(chart)


def chart_column_adders(scope):

	# Reset the list as this function will rebuild it
	scope.charts['template_col_adders'] = {}

	for chart in scope.charts['chart_list']:
		# Only add charts that require additional columns
		if scope.charts['config'][chart]['add_columns'] != None:
			scope.charts['template_col_adders'][chart] = scope.charts['config'][chart]['active']





# ---------------------------------------------------------------------------------
# Charts and Overlays STATUS Working List
# ---------------------------------------------------------------------------------
# candlestick		DONE
# scatter			ignore for now
# bar				DONE
# line				DONE						- WIP - custom button to select line
# heiken_ashi		ignore for now
# volume			DONE
# vol_per_minute	scope
# vac
# VWAP							- What Is the Volume-Weighted Average Price (VWAP)?
# macd				DONE
# macd_vol			DONE
# rsi				DONE
# vol_osssy
# stochastic		DONE
# ichi_moku
# ichi_moku_daily
# Overlays.............................
# sma_1				DONE
# sma_2				DONE
# sma_3				DONE
# ema_1				DONE
# ema_2				DONE		
# ema_3				DONE				
# bollinger_bands
# dividends			DONE
# announcements




# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================

# Primary Charts -------------------------------------
from charts.candlestick 		import candle_plot
# from charts.scatter										# TODO
from charts.bar					import bar_ohlc_plot
from charts.line 				import line_plot
# from charts.heikin_ashi

# Secondary Charts -----------------------------------
from charts.volume 				import volume_plot
# from charts.vac											# TODO
from add_cols.vpm				import vpm_cols
from charts.vpm 				import vpm_plot
from add_cols.macd				import macd_cols
from charts.macd 				import macd_plot
from add_cols.macd_on_volume	import macd_vol_cols
from charts.macd_vol			import macd_vol_plot
from add_cols.rsi 				import rsi_cols
from charts.rsi 				import rsi_plot
from add_cols.stochastic		import stoch_cols
from charts.stoch 				import stoch_plot
# from analysis.charts.				# Volume Oscillator				# TODO
# from charts.roc													# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart
											
# Overlays -------------------------------------------
from add_cols.sma				import sma_cols
from charts.overlays.sma 		import sma_plot
from add_cols.ema				import ema_cols
from charts.overlays.ema 		import ema_plot
from add_cols.dividends			import dividend_cols
from charts.overlays.dividends 	import dividend_plot


# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The chart is active or inactive (displayed or not displayed)
active_columns	= 'active_columns'		# List of columns to utilise by this config group
name 			= 'name'				# The display name for the chart (used in the settings page)
short_name		= 'short_name'			# A short name used if various Screen Outputs
is_overlay 		= 'is_overlay'			# Indicates that this chart is over layed on top of the other charts which accept overlays
add_overlays	= 'add_overlays'		# Apply the overlay to this chart - some charts are % in which case $ based averages distort the overall chart
definition		= 'definition'			# URL link to the definition for this chart or overlay
notes			= 'notes'				# Notes regarding this chart or overlay
# Chart Releated Parameters -------------------------------------------------------------------------------------------------------
plot			= 'plot'				# Dictionary of Plot Parameters for Rendering this chart
function 		= 'function'			# The function to render this chart
colour			= 'colour'				# Default Colour for certain lines
title			= 'title'				# The Title to be rendered for this chart
scale			= 'scale'				# height for the chart - this is a relative height > % of charts_height_primary
yaxis			= 'yaxis'				# Format for the Y Axis on the charts
# Dataframe Columns Required for this chart -------------------------------------------------------------------------------------------------------
add_columns		= 'add_columns'			# Dictionary of Column Params to be added to the page[df]
periods 		= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
column 			= 'column'				# OHLCV column required for calc
fast 			= 'fast'
slow 			= 'slow'
long 			= 'long'				# for the MACD
short 			= 'short'				# for the MACD
signal 			= 'signal'				# Signal line for some charts
lookback_days 	= 'lookback_days'		# Stochastic Oscillator

length	 		= 'length'				# Bollinger Bands
shift_up 		= 'shift_up'			# Bollinger Bands
shift_down 		= 'shift_down'			# Bollinger Bands
m_a_type 		= 'm_a_type'			# Bollinger Bands

charts_config = {
		# Primary Charts -----------------------------------------------------------------------
		'candlestick'		: { 
								active			: True,
								name			: 'Candlestick',
								short_name		: 'Candle',
								is_overlay		: False, 
								add_overlays	: True, 
								definition		: 'https://www.investopedia.com/terms/c/candlestick.asp',
								notes			: 'Open set by he novice trading yesterdays sentiment, High is set by the Bulls, Low is set by the Bears. The close is set by the professional investors.',
								plot			: { 
									 				function	: candle_plot, 
													title		: 'Candlestick', 
													scale		: 1.00, 
													yaxis		: '$,.2f',
												},
								add_columns		: None, 
								},
		'bar'				: { 
								active			: False, 
								name			: 'Bar Chart', 
								short_name		: 'Bar',
								is_overlay		: False, 
								add_overlays	: True, 
								definition		: 'https://www.investopedia.com/terms/b/barchart.asp',
								notes			: '',
								plot			: { 
													function	: bar_ohlc_plot, 
													title		: 'Bar Chart - OHLC', 
													scale		: 0.80, 
													yaxis		: '$,.2f' 
												}, 
								add_columns		: None, 
							},
		'scatter'			: { 
								active			: False, 
								name			: 'Scatter', 
								short_name		: 'Scatter',
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.80, 
													yaxis		: '$,.2f',	
												}, 	
								add_columns		: None, 
							},
		'line'				: { 
								active			: True , 
								name			: 'Line Chart', 
								short_name		: 'Line',
								is_overlay		: False, 
								add_overlays	: True , 
								active_columns	: ['open','high','low','close'], 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: line_plot, 
													title		: 'Line Chart', 
													scale		: 0.50, 
													yaxis		: '$,.2f' 
												}, 	
								add_columns		: None, 
							},
		'heiken_ashi'		: { 
								active			: False, 
								name			: 'Heikin Ashi', 
								short_name		: 'Heikin Ashi',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function:None, 
													title:'', 
													scale:0.80, 
													yaxis:'$,.2f' ,
												}, 	
								add_columns		: None, 
								},

		
		'VWAP'				: { 
								active			: True , 
								name			: 'Volume Weighted Average Price', 
								short_name		: 'VWAP',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	:  volume_plot, 
													title		: 'Volume', 
													scale		: 0.25, 
													yaxis		: ',.'
												}, 	
								add_columns		: None, 
								},

		
		# Secondary Charts ---------------------------------------------------------------------
		'volume'			: { 
								active			: True , 
								name			: 'Volume', 
								short_name		: 'Volume',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	:  volume_plot, 
													title		: 'Volume', 
													scale		: 0.25, 
													yaxis		: ',.'
												}, 	
								add_columns		: None, 
								},
		'vol_per_minute'	: { 
								active			: False, 
								name			: 'Volume Per Minute (VPM)',
								short_name		: 'VPM', 
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: vpm_plot, 
													title		: '', 
													scale		: 0.25, 
													yaxis		: ',.' 	
												}, 	
								add_columns		: None, 					# TODO is this a chart or on is_overlay - maybe just to the volume chart - I dont know
								},  
		'vac'				: { 
								active			: False, 
								name			: 'I have no idea what this is - VAC', 
								short_name		: 'VAC',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.25, 
													yaxis		: ',.' 
													}, 	
								add_columns		: None, 
								},
		'macd'				: { 
								active			: True, 
								name			: 'Moving Average Convergence Divergence (MACD)', 
								short_name		: 'MACD',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: macd_plot, 
													title		: 'MACD', 
													scale		: 0.50, 
													yaxis		: ',.' 
												}, 	
								add_columns		: { 
													function	: macd_cols, 
													column		: 'close', 
													long		: 26, 
													short		: 12, 
													signal		: 9 
												} 
								},
		'macd_vol'			: { 
								active			: True, 
								name			: 'MACD on Volume', 
								short_name		: 'MACD Vol',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: macd_vol_plot	, 
													title		: 'MACD (Volume)', 
													scale		: 0.50, 
													yaxis		: ',.', 	
												}, 	
								add_columns		: { 
													function	:macd_vol_cols, 
													column		:'volume', 
													long		:26, 
													short		:12, 
													signal		:9,
												}
								},
		'rsi'				: { 
								active			: True, 
								name			: 'Relative Strength Index (RSI)',
								short_name		: 'RSI',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function		: rsi_plot, 
													title			: 'RSI', 
													scale			: 0.50, 
													yaxis			: '.0%',
												}, 	
								add_columns		: { 
													function		: rsi_cols, 
													column			: 'close', 
													lookback_days	: 10, 
												}, 
								},
		'vol_osssy'			: { 
								active			: False, 
								name			: 'Volume Oscillator', 
								short_name		: 'Volume Oscillator',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.75, 
													yaxis		: '$,.2f',
												}, 	
								add_columns		: { 
													function	: None, 
													column		: 'volume', 
													fast		: 14, 
													slow		: 21 
													} 
								},
		'stochastic'		: { 
								active			: True, 
								name			: 'Stochastic', 
								short_name		: 'Stochastic',
								is_overlay		: False, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function		: stoch_plot, 
													title			: 'Stochastic', 
													scale			: 0.50, 
													yaxis			: '.0%',
												}, 	
								add_columns		: { 
													function		: stoch_cols, 
													lookback_days	: 14, 
													slow			: 3, 
													signal			: 3 ,
												} 
								},

		# Overlays -----------------------------------------------------------------------------
		'sma_a' 			: { 
								active			: False, 
								name			: 'Simple Moving Average (1)', 
								short_name		: 'SMA-1',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { function : sma_plot, colour : 'blue' }, 									
								add_columns		: {	function : sma_cols, column : 'close', periods:21 } 
								},		
		'sma_b' 			: { 
								active			: False, 
								name			: 'Simple Moving Average (2)', 
								short_name		: 'SMA-2',
								is_overlay		: True , 
								add_overlays		: False, 
								definition		: '',
								notes			: '',
								plot			: { function : sma_plot, colour : 'green' }, 									
								add_columns		: {	function : sma_cols, column : 'close', periods:50 } 
								},		
		'sma_c' 			: { 
								active			: False, 
								name			: 'Simple Moving Average (3)', 
								short_name		: 'SMA-3',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { function : sma_plot, colour : 'green' }, 									
								add_columns		: {	function : sma_cols, column : 'close', periods:200 } 
								},		
		'ema_a' 			: { 
								active			: False, 
								name			: 'Exponential Moving Average (1)', 
								short_name		: 'EMA-1',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { function : ema_plot, colour : 'red' }, 									
								add_columns		: {	function : ema_cols, column : 'close', periods:21 } 
								},
		'ema_b' 			: { 
								active			: False, 
								name			: 'Exponential Moving Average (2)', 
								short_name		: 'EMA-2',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { function : ema_plot, colour : 'blue' }, 									
								add_columns		: {	function : ema_cols, column : 'close', periods:50 } 
								},
		'ema_c' 			: { 
								active			: False, 
								name			: 'Exponential Moving Average (3)', 
								short_name		: 'EMA-3',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { function : ema_plot, colour : 'SteelBlue' }, 									
								add_columns		: {	function : ema_cols, column : 'close', periods:200 } 
								},
		'bollinger_bands' 	: { 
								active			: False, 
								name			: 'Bollinger Bands', 
								short_name		: 'Bollinger',
								is_overlay		: True, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function:sma_plot, 
													colour:'black' 		
												}, 									
								add_columns		:{ 
													function:ema_cols, 
													column:'close', 
													length:20, 
													shift_up:2, 
													shift_down:2, 
													m_a_type:'simple', 
												} 
								},
		'dividends' 		: { 
								active			: True, 
								name			: 'Dividends', 
								short_name		: 'Dividends',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function: dividend_plot, 
													colour	:'blue' 		
												}, 									
								add_columns		: { 
													function:dividend_cols			# TODO - we could still plot into the plot_df
												} 
								},		
		'announcements' 	: { 
								active			: False, 
								name			: 'Announcements', 
								short_name		: 'Announcements',
								is_overlay		: True , 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			: { 
													function:sma_plot, 
													colour	:'black' 		
												}, 									
								add_columns		: None,			 # TODO - we are still going to need a chart here
								},		
		'ichi_moku' 		: { 
								active			: False, 
								name			: 'Icki Moku', 
								short_name		: 'Icki Moku',
								is_overlay		: True, 
								add_overlays	: False, 
								definition		: '',
								notes			: '',
								plot			:{ 
													function:sma_plot, 
													colour	:'black' 		
												}, 									
								add_columns		: None 			# TODO - Rob to work out if this needs speccing
								},		
		'ichi_moku_daily'	: { 
								active			:False, 
								name			:'Icki Moku Daily', 
								short_name		:'Icki Moku Daily',
								is_overlay		:True,
								add_overlays	:False,
								definition		: '',
								notes			: '',
								plot			: { 
													function:sma_plot, 
													colour	:'black'
													},
								add_columns		: None 					# TODO - Rob to work out if this needs speccing

								},		
		}







