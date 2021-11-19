# ==============================================================================================================================================================
# Technical Indicator Specification for the charts
# ==============================================================================================================================================================


# Primary Charts -------------------------------------
from analysis.charts.candlestick 	import candle_plot
from analysis.charts.volume 		import volume_plot
from analysis.charts.macd 			import macd_plot
from analysis.charts.rsi 			import rsi_plot
from analysis.charts.stoch 			import stoch_plot
from analysis.charts.vpm 			import vpm_plot, vpm_cols
# from analysis.charts.roc									# TODO - not sure what this one is ROb - investigate and add in - i think it might be a primary chart

# Secondary Charts -----------------------------------
from analysis.charts.macd 			import macd_plot, macd_cols
from analysis.charts.rsi 			import rsi_plot, rsi_cols
# from analysis.charts.				# Volume Oscillator					# TODO
from analysis.charts.stoch 			import stoch_plot, stoch_cols

# Overlays -------------------------------------------
from analysis.charts.overlays.sma 	import sma_cols, sma_plot
from analysis.charts.overlays.ema 	import ema_cols




# ==============================================================================================================================================================
# Chart Specification (included the tech indicators where appropriate)
# ==============================================================================================================================================================

active 			= 'active'				# True or False - The chart is active or inactive (displayed or not displayed)
name 			= 'name'				# The display name for the chart (used in the settings page)
# primary 		= 'primary'				# True or False
# 										# True  = Primary on whch can apply Technical Measures - ie a SMA
# 										# False = Secondary Charts which do not accept Technical Measures
overlay 		= 'overlay'				# Indicates that this chart is added to, or overlayed on top of the other charts
active 			= 'active'				# True or False - is this technical Indicator is being applied to our Primary Chart?
# Chart Releated Parameters -------------------------------------------------------------------------------------------------------
chart_schema	= 'chart_schema'		# Dictionary of Chart Parameters
function 		= 'function'			# The function to render this chart
title			= 'title'				# The Title to be rendered for this chart
height			= 'height'				# height for the chart - this is a relative height
# Dataframe Columns Required for this chart -------------------------------------------------------------------------------------------------------
data_cols		= 'data_cols'			# Dictionary of Dataframe Column Params	
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

# TODO - do we even need the overlay variable now - we can just see if we have a chart function or a data_cols function and go from there?


chart_schema = {
		# Primary Charts -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		'candlestick'		: { active:True , name:'CandleStick'		, overlay:False	, chart_schema:{ function:candle_plot 	, title:'Price'		, height:1 }, data_cols:None, },
		'scatter'			: { active:False, name:'Scatter'			, overlay:False	, chart_schema:{ function:None			, title:''			, height:1 }, data_cols:None, },
		'bar'				: { active:False, name:'Bar'				, overlay:False	, chart_schema:{ function:None			, title:''			, height:1 }, data_cols:None, },
		'line'				: { active:False, name:'Line charts'		, overlay:False	, chart_schema:{ function:None			, title:''			, height:1 }, data_cols:None, },
		'heiken_ashi'		: { active:False, name:'Heikin Ashi'		, overlay:False	, chart_schema:{ function:None			, title:''			, height:1 }, data_cols:None, },
		# Secondary Charts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
		'volume'			: { active:False , name:'Volume'			, overlay:False	, chart_schema:{ function:volume_plot	, title:'Volume'	, height:1 }, data_cols:None, },
		'vol_per_minute'	: { active:False, name:'Volume Per Minute'	, overlay:False	, chart_schema:{ function:vpm_plot		, title:''			, height:1 }, data_cols:None, },  # TODO is this a chart or on overlay - maybe just to the volume chart - I dont know
		'vac'				: { active:False, name:'VAC'				, overlay:False	, chart_schema:{ function:None			, title:''			, height:1 }, data_cols:None, },
		'macd'				: { active:False , name:'MACD'				, overlay:False	, chart_schema:{ function:macd_plot		, title:'MACD'		, height:1 }, data_cols:{ function:macd_cols	, column:'close', long:26, short:12, signal:9 } },
		'rsi'				: { active:False , name:'RSI'				, overlay:False	, chart_schema:{ function:rsi_plot		, title:''			, height:1 }, data_cols:{ function:rsi_cols		, column:'close', periods:10, }, },
		'vol_osssy'			: { active:False, name:'Volume Oscillator'	, overlay:False , chart_schema:{ function:None 			, title:''			, height:1 }, data_cols:{ function:None			, column:'volume', fast:14, slow:21 } },
		'stochastic'		: { active:False , name:'Stochastic'		, overlay:False , chart_schema:{ function:stoch_plot	, title:'Stochastic', height:1 }, data_cols:{ function:stoch_cols	, lookback_days:14, slow:3, signal:3 } },
		# Overlays ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		'sma_1' 			: { active:True , name:'SMA-1'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:sma_cols, column:'close', periods:21 	} },
		'sma_2' 			: { active:False, name:'SMA-2'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:sma_cols, column:'close', periods:50 	} },
		'sma_3' 			: { active:False, name:'SMA-3'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:sma_cols, column:'close', periods:200	} },
		'ema_1' 			: { active:False, name:'EMA-1'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:ema_cols, column:'close', periods:21 	} },
		'ema_2' 			: { active:False, name:'EMA-2'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:ema_cols, column:'close', periods:50 	} },
		'ema_3' 			: { active:False, name:'EMA-3'				, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:ema_cols, column:'close', periods:200 } },
		'bollinger_bands' 	: { active:False, name:'Bollinger Bands'	, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:{ function:ema_cols, column:'close', length:20, shift_up:2, shift_down:2, m_a_type:'simple', } },
		'dividends' 		: { active:False, name:'Dividends'			, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:None },		# TODO - we could still plot into the plot_df
		'announcements' 	: { active:False, name:'Announcements'		, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:None },		# TODO - we are still going to need a chart here
		'ichi_moku' 		: { active:False, name:'Icki Moku' 			, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:None },		# TODO - Rob to work out if this needs speccing
		'ichi_moku_daily'	: { active:False, name:'Icki Moku Daily'	, overlay:True	, chart_schema:{ function:sma_plot }, data_cols:None },		# TODO - Rob to work out if this needs speccing

		}

