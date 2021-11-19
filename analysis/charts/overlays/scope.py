# Measures are applied against the primary chart
# they act as an overlay to say the candlestick chart. i.e. rendering a SMA on the close price


from analysis.measures.sma import sma
from analysis.measures.ema import ema
from analysis.measures.vpm import vpm





active 		= 'active'				# True or False - is this technical Indicator is being applied to our Primary Chart?
name 		= 'name'				# The display name for the technical Indicator  (used in the settings page)
function	= 'function'			# the appropriate function for this measure
params 		= 'params'				# None or dictionary of paramaters required for this techncial indicator
periods 	= 'periods'				# Most Indicators use a base number of days/hours (periods) for their calcs - store it here
column 		= 'column'				# OHLCV column required for calc
length	 	= 'length'				# Bollinger Bands
shift_up 	= 'shift_up'			# Bollinger Bands
shift_down 	= 'shift_down'			# Bollinger Bands
m_a_type 	= 'm_a_type'			# Bollinger Bands

measures = {
					'sma_1' 			: { active:False, name:'SMA-1'			, function:sma,  params:{ periods:21, column:'close' } },
					'sma_2' 			: { active:False, name:'SMA-2'			, function:sma,  params:{ periods:50, column:'close' } },
					'sma_3' 			: { active:False, name:'SMA-3'			, function:sma,  params:{ periods:200, column:'close' } },

					'ema_1' 			: { active:False, name:'EMA-1'			, function:ema,  params:{ periods:21, column:'close' } },
					'ema_2' 			: { active:False, name:'EMA-2'			, function:ema,  params:{ periods:50, column:'close' } },
					'ema_3' 			: { active:False, name:'EMA-3'			, function:ema,  params:{ periods:200, column:'close' } },

					'bollinger_bands' 	: { active:False, name:'Bollinger Bands', function:None, params:{ column:'close', length:20, shift_up:2, shift_down:2, m_a_type:'simple', } },
					'dividends' 		: { active:False, name:'Dividends'		, function:None, params:None },		# TODO - we could still plot into the plot_df
					'announcements' 	: { active:False, name:'Announcements'	, function:None, params:None },		# TODO - we are still going to need a function here
					'ichi_moku' 		: { active:False, name:'Icki Moku' 		, function:None, params:None },		# TODO - Rob to work out if this needs speccing
					'ichi_moku_daily'	: { active:False, name:'Icki Moku Daily', function:None, params:None },		# TODO - Rob to work out if this needs speccing


					'vpm'				: { active:False, name:'Volume Per Minute', function:vpm, params:None }, # TODO Rob to work out how to use this?? it may be a chart specific - ie just for the secondar volume chart
				}



def scope_measures(scope):
	scope.measures = measures