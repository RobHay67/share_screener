


# chart_schema = {
# 		# Primary Charts -------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 		'candlestick'		: { active:True , name:'CandleStick'		, overlay:False	, chart:{ function:plot_candlestick , title:'Price'		, height:1 }, data_cols:None, },
# 		'scatter'			: { active:False, name:'Scatter'			, overlay:False	, chart:{ function:None				, title:''			, height:1 }, data_cols:None, },
# 		'bar'				: { active:False, name:'Bar'				, overlay:False	, chart:{ function:None				, title:''			, height:1 }, data_cols:None, },
# 		'line'				: { active:False, name:'Line charts'		, overlay:False	, chart:{ function:None				, title:''			, height:1 }, data_cols:None, },
# 		'heiken_ashi'		: { active:False, name:'Heikin Ashi'		, overlay:False	, chart:{ function:None				, title:''			, height:1 }, data_cols:None, },
# 		# Secondary Charts -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 		'volume'			: { active:True , name:'Volume'				, overlay:False	, chart:{ function:plot_volume		, title:'Volume'	, height:1 }, data_cols:None, },
# 		'vol_per_minute'	: { active:False, name:'Volume Per Minute'	, overlay:False	, chart:{ function:vpm				, title:''			, height:1 }, data_cols:None, },  # TODO is this a chart or on overlay - maybe just to the volume chart - I dont know
# 		'vac'				: { active:False, name:'VAC'				, overlay:False	, chart:{ function:chart			, title:''			, height:1 }, data_cols:None, },
# 		'macd'				: { active:True , name:'MACD'				, overlay:False	, chart:{ function:macd				, title:'MACD'		, height:1 }, data_cols:{ function:macd, column:'close', long:26, short:12, signal:9 } },
# 		'rsi'				: { active:True , name:'RSI'				, overlay:False	, chart:{ function:rsi				, title:''			, height:1 }, data_cols:{ function:rsi, column:'close', periods:10, }, },
# 		'vol_osssy'			: { active:False, name:'Volume Oscillator'	, overlay:False , chart:{ function:chart 			, title:''			, height:1 }, data_cols:{ function:None, column:'volume', fast:14, slow:21 } },
# 		'stochastic'		: { active:True , name:'Stochastic'			, overlay:False , chart:{ function:stoch			, title:'Stochastic', height:1 }, data_cols:{ function:stoch, lookback_days:14, slow:3, signal:3 } },
# 		# Overlays ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 		'sma_1' 			: { active:False, name:'SMA-1'				, overlay:True	, chart:None, data_cols:{ function:sma, column:'close', periods:21 	} },
# 		'sma_2' 			: { active:False, name:'SMA-2'				, overlay:True	, chart:None, data_cols:{ function:sma, column:'close', periods:50 	} },
# 		'sma_3' 			: { active:False, name:'SMA-3'				, overlay:True	, chart:None, data_cols:{ function:sma, column:'close', periods:200	} },
# 		'ema_1' 			: { active:False, name:'EMA-1'				, overlay:True	, chart:None, data_cols:{ function:ema, column:'close', periods:21 	} },
# 		'ema_2' 			: { active:False, name:'EMA-2'				, overlay:True	, chart:None, data_cols:{ function:ema, column:'close', periods:50 	} },
# 		'ema_3' 			: { active:False, name:'EMA-3'				, overlay:True	, chart:None, data_cols:{ function:ema, column:'close', periods:200 } },
# 		'bollinger_bands' 	: { active:False, name:'Bollinger Bands'	, overlay:True	, chart:None, data_cols:{ function:ema, column:'close', length:20, shift_up:2, shift_down:2, m_a_type:'simple', } },
# 		'dividends' 		: { active:False, name:'Dividends'			, overlay:True	, chart:None, data_cols:None },		# TODO - we could still plot into the plot_df
# 		'announcements' 	: { active:False, name:'Announcements'		, overlay:True	, chart:None, data_cols:None },		# TODO - we are still going to need a chart here
# 		'ichi_moku' 		: { active:False, name:'Icki Moku' 			, overlay:True	, chart:None, data_cols:None },		# TODO - Rob to work out if this needs speccing
# 		'ichi_moku_daily'	: { active:False, name:'Icki Moku Daily'	, overlay:True	, chart:None, data_cols:None },		# TODO - Rob to work out if this needs speccing

# 		}
#@st.cache
def create_plot_df(scope, ticker ):
	print ( '\033[93mcreate_plot_df is being rebuilt - are you certain now is the time to do this ? \033[0m')

	plot_df = scope.selected[scope.display_page]['analysis_df'][ticker].copy()
	plot_df.sort_values(by=['date'], inplace=True, ascending=True)	


	print('='*100)
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['data_cols'] != None:
			print ('Add Data Columns for requested chart or overlay = ', chart)
			if scope.charts[chart]['data_cols']['function'] != None:					# TODO - remove this after add everything
				scope.charts[chart]['data_cols']['function'](scope, plot_df, chart)
			else:
				print( '\033[91mFunction has not yet been defined for this Chart\033[0m')
 
	# store the analysis_df
	scope.selected[scope.display_page]['plot_df'][ticker] = plot_df


	# after adding all the relevant measures we can reset this 
	# so this function does not get called unnecasily
	scope.rebuild_plot_df = False
