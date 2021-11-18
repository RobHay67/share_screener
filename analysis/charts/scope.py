


# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================

active 	= 'active'				# True or False - is this technical Indicator is being applied to our Primary Chart?
params 	= 'params'				# None or dictionary of paramaters required for this techncial indicator
periods = 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
column 	= 'column'				# OHLCV column required for calc
fast 	= 'fast'
slow 	= 'slow'
long 	= 'long'				# for the MACD
short 	= 'short'				# for the MACD
signal 	= 'signal'				# Signal line for some charts

chart_measures = {
		'rsi'			:{ periods:10  , column:'close' , fast:None, slow:None, long:None, short:None, signal:None },
		'stochastic'	:{ periods:14  , column:'close' , fast:None, slow:3   , long:None, short:None, signal:3    },
		'macd'			:{ periods:None, column:'close' , fast:None, slow:None, long:26  , short:12  , signal:9    },
		'vol_osssy'		:{ periods:None, column:'volume', fast:14  , slow:21  , long:None, short:None, signal:None },				
		}


# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 	= 'active'				# True or False - The chart is active or inactive (displayed or not displayed)
name 	= 'name'				# The display name for the chart (used in the settings page)
primary = 'primary'				# True or False
								# True  = Primary on whch can apply Technical Measures - ie a SMA
 								# False = Secondary Charts which do not accept Technical Measures
params 	= 'params'				# Chart Specific Parameters to Capture - which are stored in the tech_indicators library

chart_schema = {
				'candlestick'	:{'active':True, 	name:'CandleStick'		, primary:True,  params:None, },
				'scatter'		:{'active':False, 	name:'Scatter'			, primary:True,  params:None, },
				'bar'			:{'active':False, 	name:'Bar'				, primary:True,  params:None, },
				'line'			:{'active':False, 	name:'Line charts'		, primary:True,  params:None, },
				'heiken_ashi'	:{'active':False, 	name:'Heikin Ashi'		, primary:True,  params:None, },
				'volume'		:{'active':True, 	name:'Volume'			, primary:False, params:None, },
				'vol_per_minute':{'active':False, 	name:'Volume Per Minute', primary:False, params:None, },
				'vac'			:{'active':False, 	name:'VAC'				, primary:False, params:None, },
				'macd'			:{'active':True, 	name:'MACD'				, primary:False, params:chart_measures['macd'], },
				'stochastic'	:{'active':True, 	name:'Stochastic'		, primary:False, params:chart_measures['stochastic'], },
				'rsi'			:{'active':True, 	name:'RSI'				, primary:False, params:chart_measures['rsi'], },
				'vol_osssy'		:{'active':False, 	name:'Volume Oscillator', primary:False, params:chart_measures['vol_osssy'], },
				}


def scope_chart(scope):
	scope.charts = chart_schema
	scope.rebuild_plot_df = True		# Default Flag to track if the analysis_df needs a refresh


