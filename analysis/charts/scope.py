

from analysis.charts.macd import macd
from analysis.charts.rsi import rsi
from analysis.charts.stoch import stoch




# from analysis.charts.roc	# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart



# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================

from analysis.charts.macd import macd
from analysis.charts.rsi import rsi


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


chart_measures = {
					'rsi'			:{ column:'close', periods:10, },
					'stochastic'	:{ lookback_days:14, slow:3, signal:3    },
					'macd'			:{ column:'close', long:26, short:12, signal:9 },
					'vol_osssy'		:{ column:'volume', fast:14, slow:21 },				
					}


# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 		= 'active'		# True or False - The chart is active or inactive (displayed or not displayed)
name 		= 'name'		# The display name for the chart (used in the settings page)
function	= 'function'	# the appropriate function for this measure
primary 	= 'primary'		# True or False
							# True  = Primary on whch can apply Technical Measures - ie a SMA
 							# False = Secondary Charts which do not accept Technical Measures
params 		= 'params'		# Chart Specific Parameters to Capture - which are stored in the tech_indicators library

chart_schema = {
				'candlestick'	:{'active':True, 	name:'CandleStick'		, function:None		, primary:True,  params:None, },
				'scatter'		:{'active':False, 	name:'Scatter'			, function:None		, primary:True,  params:None, },
				'bar'			:{'active':False, 	name:'Bar'				, function:None		, primary:True,  params:None, },
				'line'			:{'active':False, 	name:'Line charts'		, function:None		, primary:True,  params:None, },
				'heiken_ashi'	:{'active':False, 	name:'Heikin Ashi'		, function:None		, primary:True,  params:None, },
				'volume'		:{'active':True, 	name:'Volume'			, function:None		, primary:False, params:None, },
				'vol_per_minute':{'active':False, 	name:'Volume Per Minute', function:function	, primary:False, params:None, },  # TODO is this a chart or on overlay - maybe just to the volume chart - I dont know
				'vac'			:{'active':False, 	name:'VAC'				, function:function	, primary:False, params:None, },
				'macd'			:{'active':True, 	name:'MACD'				, function:macd		, primary:False, params:chart_measures['macd'], },
				'stochastic'	:{'active':True, 	name:'Stochastic'		, function:stoch	, primary:False, params:chart_measures['stochastic'], },
				'rsi'			:{'active':True, 	name:'RSI'				, function:rsi		, primary:False, params:chart_measures['rsi'], },
				'vol_osssy'		:{'active':False, 	name:'Volume Oscillator', function:function , primary:False, params:chart_measures['vol_osssy'], },
				}


def scope_chart(scope):
	scope.charts = chart_schema
	scope.rebuild_plot_df = True		# Default Flag to track if the analysis_df needs a refresh


