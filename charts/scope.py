def scope_chart(scope):
	scope.chart_lines = []
	scope.chart_macd_on_price = {}
	scope.chart_macd_on_volume = {}


	scope.chart = {
					'candlestick':True,
					'heiken_ashi':False,
					
					'macd':True,
					'stochastic':True,
					'rsi':True,
					'ichi_moku':False,
					
					'bollinger_bands':False,
					
					'volume':True,
					'vac':False,
					'vol_osclillator':False,

					'line':False,		

					'dividends':False,
					'announcements':False,
	}



