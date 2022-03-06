# TODO - metics should be moved into that library
# 



# Charts and Overlays STATUS Working List
# ---------------------------------------------------------------------------------
# candlestick		DONE
# scatter			ignore for now
# bar				ignore for now
# line				DONE						- WIP - custom button to select line
# heiken_ashi		ignore for now
# volume			DONE
# vol_per_minute	scope
# vac
# macd				DONE
# macd_vol			DONE
# rsi				DONE
# vol_osssy
# stochastic		DONE
# sma_1				DONE
# sma_2				DONE
# sma_3				DONE
# ema_1				DONE
# ema_2				DONE		
# ema_3				DONE				
# bollinger_bands
# dividends			DONE
# announcements
# ichi_moku
# ichi_moku_daily



# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================

# Primary Charts -------------------------------------
from charts.charts.candlestick 		import candle_plot
# from charts.charts.scatter										# TODO
# from charts.charts.bar											# TODO
from charts.charts.line 			import line_plot
# from charts.charts.heikin_ashi

# Secondary Charts -----------------------------------
from charts.charts.volume 			import volume_plot
# from charts.charts.vac											# TODO
from metrics.model.vpm				import vpm_cols
from charts.charts.vpm 				import vpm_plot
from metrics.model.macd				import macd_cols
from charts.charts.macd 			import macd_plot
from metrics.model.macd_on_volume	import macd_vol_cols
from charts.charts.macd_vol			import macd_vol_plot
from metrics.model.rsi 				import rsi_cols
from charts.charts.rsi 				import rsi_plot
from metrics.model.stochastic		import stoch_cols
from charts.charts.stoch 			import stoch_plot
# from analysis.charts.				# Volume Oscillator				# TODO
# from charts.roc													# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart
											
# Overlays -------------------------------------------
from metrics.model.sma				import sma_cols
from charts.view.sma 			import sma_plot
from metrics.model.ema				import ema_cols
from charts.view.ema 			import ema_plot
from metrics.model.dividends		import dividend_cols
from charts.view.dividends 		import dividend_plot


# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The chart is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the chart (used in the settings page)
is_overlay 		= 'is_overlay'			# Indicates that this chart is over layed on top of the other charts which accept overlays
add_overlays	= 'add_overlays'		# Apply the overlay to this chart - some charts are % in which case $ based averages distort the overall chart
active 			= 'active'				# True or False - is this technical Indicator is being applied to our Primary Chart?
# Chart Releated Parameters -------------------------------------------------------------------------------------------------------
plot			= 'plot'				# Dictionary of Plot Parameters for Rendering this chart
function 		= 'function'			# The function to render this chart
colour			= 'colour'				# Default Colour for certain lines
title			= 'title'				# The Title to be rendered for this chart
scale			= 'scale'				# height for the chart - this is a relative height > % of charts_height_primary
yaxis			= 'yaxis'				# Format for the Y Axis on the charts
# Dataframe Columns Required for this chart -------------------------------------------------------------------------------------------------------
metrics			= 'metrics'			# Dictionary of Dataframe Column Params	
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

chart_config = {
		# Primary Charts -----------------------------------------------------------------------
		'candlestick'		: { 
								active			: True,
								name			: 'CandleStick', 
								is_overlay		: False, 
								add_overlays	: True, 
								plot			: { 
									 				function	: candle_plot, 
													title		: 'Price', 
													scale		: 1.00, 
													yaxis		: '$,.2f',
												},
								metrics			: None, 
								},
		'scatter'			: { 
								active			: False, 
								name			: 'Scatter', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.80, 
													yaxis		: '$,.2f',	
												}, 	
								metrics			: None, 
							},
		'bar'				: { 
								active			: False, 
								name			: 'Bar', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.80, 
													yaxis		: '$,.2f' 
												}, 
								metrics			: None, 
							},
		'line'				: { 
								active			: True , 
								name			: 'Line charts', 
								is_overlay		: False, 
								add_overlays	: True , 
								plot			: { 
													function	: line_plot, 
													title		: 'Line', 
													scale		: 0.50, 
													yaxis		: '$,.2f' 
												}, 	
								metrics			: {
													function	: None, 
													column		: 'close',
												},
							},
		'heiken_ashi'		: { 
								active			: False, 
								name			: 'Heikin Ashi', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function:None, 
													title:'', 
													scale:0.80, 
													yaxis:'$,.2f' ,
												}, 	
								metrics			: None, 
								},
		# Secondary Charts ---------------------------------------------------------------------
		'volume'			: { 
								active			: True , 
								name			: 'Volume', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	:  volume_plot, 
													title		: 'Volume', 
													scale		: 0.25, 
													yaxis		: ',.'
												}, 	
								metrics			: None, 
								},
		'vol_per_minute'	: { 
								active			: False, 
								name			: 'Volume Per Minute', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: vpm_plot, 
													title		: '', 
													scale		: 0.25, 
													yaxis		: ',.' 	
												}, 	
								metrics			: None, 					# TODO is this a chart or on is_overlay - maybe just to the volume chart - I dont know
								},  
		'vac'				: { 
								active			: False, 
								name			: 'VAC', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.25, 
													yaxis		: ',.' 
													}, 	
								metrics			: None, 
								},
		'macd'				: { 
								active			: True, 
								name			: 'MACD', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: macd_plot, 
													title		: 'MACD', 
													scale		: 0.50, 
													yaxis		: ',.' 
												}, 	
								metrics			: { 
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
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: macd_vol_plot	, 
													title		: 'MACD (Volume)', 
													scale		: 0.50, 
													yaxis		: ',.', 	
												}, 	
								metrics			: { 
													function	:macd_vol_cols, 
													column		:'volume', 
													long		:26, 
													short		:12, 
													signal		:9,
												}
								},
		'rsi'				: { 
								active			: True, 
								name			: 'RSI',
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function		: rsi_plot, 
													title			: 'RSI', 
													scale			: 0.50, 
													yaxis			: '.0%',
												}, 	
								metrics			: { 
													function		: rsi_cols		, 
													column			: 'close'	, 
													lookback_days	: 10, 
												}, 
								},
		'vol_osssy'			: { 
								active			: False, 
								name			: 'Volume Oscillator', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function	: None, 
													title		: '', 
													scale		: 0.75, 
													yaxis		: '$,.2f',
												}, 	
								metrics			: { 
													function	: None, 
													column		: 'volume', 
													fast		: 14, 
													slow		: 21 
													} 
								},
		'stochastic'		: { 
								active			: True, 
								name			: 'Stochastic', 
								is_overlay		: False, 
								add_overlays	: False, 
								plot			: { 
													function		: stoch_plot, 
													title			: 'Stochastic', 
													scale			: 0.50, 
													yaxis			: '.0%',
												}, 	
								metrics			: { 
													function		: stoch_cols, 
													lookback_days	: 14, 
													slow			: 3, 
													signal			: 3 ,
												} 
								},

		# Overlays -----------------------------------------------------------------------------
		'sma_1' 			: { 
								active			: False, 
								name			: 'SMA-1', 
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { function : sma_plot, colour : 'blue' }, 									
								metrics			: {	function : sma_cols, column : 'close', periods:21 } 
								},		
		'sma_2' 			: { 
								active			: False, 
								name			: 'SMA-2', 
								is_overlay		: True , 
								add_overlays		: False, 
								plot			: { function : sma_plot, colour : 'green' }, 									
								metrics			: {	function : sma_cols, column : 'close', periods:50 } 
								},		
		'sma_3' 			: { 
								active			: False, 
								name			: 'SMA-3', 
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { function : sma_plot, colour : 'green' }, 									
								metrics			: {	function : sma_cols, column : 'close', periods:200 } 
								},		
		'ema_1' 			: { 
								active			: False, 
								name			: 'EMA-1', 
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { function : ema_plot, colour : 'red' }, 									
								metrics			: {	function : ema_cols, column : 'close', periods:21 } 
								},
		'ema_2' 			: { 
								active			: False, 
								name			: 'EMA-2', 
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { function : ema_plot, colour : 'blue' }, 									
								metrics			: {	function : ema_cols, column : 'close', periods:50 } 
								},
		'ema_3' 			: { 
								active			: False, 
								name			: 'EMA-3', 
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { function : ema_plot, colour : 'SteelBlue' }, 									
								metrics			: {	function : ema_cols, column : 'close', periods:200 } 
								},
		'bollinger_bands' 	: { 
								active			: False, 
								name			: 'Bollinger Bands', 
								is_overlay		: True, 
								add_overlays	: False, 
								plot			: { 
													function:sma_plot, 
													colour:'black' 		
												}, 									
								metrics			:{ 
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
								is_overlay		: True , 
								add_overlays	: False, 
								plot			: { 
													function: dividend_plot, 
													colour	:'blue' 		
												}, 									
								metrics			: { 
													function:dividend_cols			# TODO - we could still plot into the plot_df
												} 
								},		
		'announcements' 	: { 
								active			:False, 
								name			:'Announcements', 
								is_overlay		:True , 
								add_overlays	:False, 
								plot			:{ 
													function:sma_plot, 
													colour	:'black' 		
												}, 									
								metrics			: None,			 # TODO - we are still going to need a chart here
								},		
		'ichi_moku' 		: { 
								active			: False, 
								name			: 'Icki Moku', 
								is_overlay		: True, 
								add_overlays	: False, 
								plot			:{ 
													function:sma_plot, 
													colour	:'black' 		
												}, 									
								metrics			: None 			# TODO - Rob to work out if this needs speccing
								},		
		'ichi_moku_daily'	: { 
								active			:False, 
								name			:'Icki Moku Daily', 
								is_overlay		:True,
								add_overlays	:False,
								plot			: { 
													function:sma_plot, 
													colour	:'black'
													},
								metrics			: None 					# TODO - Rob to work out if this needs speccing

								},		
		}







def scope_chart(scope):
	scope.charts = chart_config
	scope.charts_height_primary = 500
	scope.charts_total_height = scope.charts_height_primary
	scope.chart_colours = ['blue','orange','green','red','LightSkyBlue','ForestGreen','SteelBlue','black', 'yellow']
	

