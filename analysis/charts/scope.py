




# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================

from analysis.charts.macd import macd
from analysis.charts.rsi import rsi



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


from analysis.charts.macd import macd
from analysis.charts.rsi import rsi
from analysis.charts.stoch import stoch
# from analysis.charts.roc									# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart
from analysis.charts.candlestick import plot_candlestick
from analysis.charts.volume import plot_volume


chart_schema = {
				'candlestick'	:{'active':True, 	name:'CandleStick'		, function:plot_candlestick , primary:True , title:'Price', height:1, params:None, },
				'scatter'		:{'active':False, 	name:'Scatter'			, function:None				, primary:True , title:'',  params:None, },
				'bar'			:{'active':False, 	name:'Bar'				, function:None				, primary:True , title:'',  params:None, },
				'line'			:{'active':False, 	name:'Line charts'		, function:None				, primary:True , title:'',  params:None, },
				'heiken_ashi'	:{'active':False, 	name:'Heikin Ashi'		, function:None				, primary:True , title:'',  params:None, },
				'volume'		:{'active':True, 	name:'Volume'			, function:plot_volume		, primary:False, title:'Volume', params:None, },
				'vol_per_minute':{'active':False, 	name:'Volume Per Minute', function:function			, primary:False, title:'', params:None, },  # TODO is this a chart or on overlay - maybe just to the volume chart - I dont know
				'vac'			:{'active':False, 	name:'VAC'				, function:function			, primary:False, title:'', params:None, },
				'macd'			:{'active':True, 	name:'MACD'				, function:macd				, primary:False, title:'MACD', params:{ column:'close', long:26, short:12, signal:9 } },
				'rsi'			:{'active':True, 	name:'RSI'				, function:rsi				, primary:False, title:'', params:{ column:'close', periods:10, }, },
				'vol_osssy'		:{'active':False, 	name:'Volume Oscillator', function:function 		, primary:False, title:'', params:{ column:'volume', fast:14, slow:21 } },
				'stochastic'	:{'active':True, 	name:'Stochastic'		, function:stoch			, primary:False, title:'Stochastic', params:{ lookback_days:14, slow:3, signal:3 } },
				}






def scope_chart(scope):
	scope.charts = chart_schema
	scope.rebuild_plot_df = True		# Default Flag to track if the analysis_df needs a refresh


