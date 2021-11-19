




# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================
# Charts -----------------------------------
from analysis.charts.candlestick import plot_candlestick
from analysis.charts.volume import plot_volume
from analysis.charts.macd import macd
from analysis.charts.rsi import rsi
from analysis.charts.stoch import stoch
# from analysis.charts.roc									# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart

# Overlays ---------------------------------
from analysis.charts.overlays.sma import sma
from analysis.charts.overlays.ema import ema
from analysis.charts.overlays.vpm import vpm

# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 		= 'active'		# True or False - The chart is active or inactive (displayed or not displayed)
name 		= 'name'		# The display name for the chart (used in the settings page)
function	= 'function'	# the appropriate function for this measure
primary 	= 'primary'		# True or False
							# True  = Primary on whch can apply Technical Measures - ie a SMA
 							# False = Secondary Charts which do not accept Technical Measures
title		= 'title'		# The Title to be rendered for this chart
height		= 'height'		# height for the chart - this is a relative height
params 		= 'params'		# Chart Specific Parameters to Capture - which are stored in the tech_indicators library

# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================
active 			= 'active'				# True or False - is this technical Indicator is being applied to our Primary Chart?
params 			= 'params'				# None or dictionary of paramaters required for this techncial indicator
periods 		= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
column 			= 'column'				# OHLCV column required for calc
fast 			= 'fast'
slow 			= 'slow'
long 			= 'long'				# for the MACD
short 			= 'short'				# for the MACD
signal 			= 'signal'				# Signal line for some charts
lookback_days 	= 'lookback_days'		# Stochastic Oscillator
overlay 		= 'overlay'				# Indicates that this chart is added to, or overlayed on top of the other charts

chart_schema = {
		'candlestick'		:{active:True, 	name:'CandleStick'		, overlay:False	, function:plot_candlestick , primary:True , title:'Price', height:1, params:None, },
		'scatter'			:{active:False, name:'Scatter'			, overlay:False	, function:None				, primary:True , title:'',  params:None, },
		'bar'				:{active:False, name:'Bar'				, overlay:False	, function:None				, primary:True , title:'',  params:None, },
		'line'				:{active:False, name:'Line charts'		, overlay:False	, function:None				, primary:True , title:'',  params:None, },
		'heiken_ashi'		:{active:False, name:'Heikin Ashi'		, overlay:False	, function:None				, primary:True , title:'',  params:None, },
		'volume'			:{active:True, 	name:'Volume'			, overlay:False	, function:plot_volume		, primary:False, title:'Volume', params:None, },
		'vol_per_minute'	:{active:False, name:'Volume Per Minute', overlay:False	, function:function			, primary:False, title:'', params:None, },  # TODO is this a chart or on overlay - maybe just to the volume chart - I dont know
		'vac'				:{active:False, name:'VAC'				, overlay:False	, function:function			, primary:False, title:'', params:None, },
		'macd'				:{active:True, 	name:'MACD'				, overlay:False	, function:macd				, primary:False, title:'MACD', params:{ column:'close', long:26, short:12, signal:9 } },
		'rsi'				:{active:True, 	name:'RSI'				, overlay:False	, function:rsi				, primary:False, title:'', params:{ column:'close', periods:10, }, },
		'vol_osssy'			:{active:False, name:'Volume Oscillator', overlay:False , function:function 			, primary:False, title:'', params:{ column:'volume', fast:14, slow:21 } },
		'stochastic'		:{active:True, 	name:'Stochastic'		, overlay:False , function:stoch				, primary:False, title:'Stochastic', params:{ lookback_days:14, slow:3, signal:3 } },
		# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
		# Overlays
		'sma_1' 			:{ active:False, name:'SMA-1'			, overlay:True	, function:sma,  params:{ periods:21, column:'close' } },
		'sma_2' 			:{ active:False, name:'SMA-2'			, overlay:True	, function:sma,  params:{ periods:50, column:'close' } },
		'sma_3' 			:{ active:False, name:'SMA-3'			, overlay:True	, function:sma,  params:{ periods:200, column:'close' } },
		'ema_1' 			:{ active:False, name:'EMA-1'			, overlay:True	, function:ema,  params:{ periods:21, column:'close' } },
		'ema_2' 			:{ active:False, name:'EMA-2'			, overlay:True	, function:ema,  params:{ periods:50, column:'close' } },
		'ema_3' 			:{ active:False, name:'EMA-3'			, overlay:True	, function:ema,  params:{ periods:200, column:'close' } },
		'bollinger_bands' 	:{ active:False, name:'Bollinger Bands'	, overlay:True	, function:None, params:{ column:'close', length:20, shift_up:2, shift_down:2, m_a_type:'simple', } },
		'dividends' 		:{ active:False, name:'Dividends'		, overlay:True	, function:None, params:None },		# TODO - we could still plot into the plot_df
		'announcements' 	:{ active:False, name:'Announcements'	, overlay:True	, function:None, params:None },		# TODO - we are still going to need a function here
		'ichi_moku' 		:{ active:False, name:'Icki Moku' 		, overlay:True	, function:None, params:None },		# TODO - Rob to work out if this needs speccing
		'ichi_moku_daily'	:{ active:False, name:'Icki Moku Daily'	, overlay:True	, function:None, params:None },		# TODO - Rob to work out if this needs speccing


		'vpm'				: { active:False, name:'Volume Per Minute', function:vpm, params:None }, # TODO Rob to work out how to use this?? it may be a chart specific - ie just for the secondar volume chart





		}



measures = {
					
				}











def scope_chart(scope):
	scope.charts = chart_schema
	scope.rebuild_plot_df = True		# Default Flag to track if the analysis_df needs a refresh


