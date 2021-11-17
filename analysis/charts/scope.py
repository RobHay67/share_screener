from analysis.tech_indicators.scope import tech_indicators

primary = 'primary_chart'		# True or False - 
#								  True  = Primary on whch can apply Technical Indicators
# 								  False = Secondary Charts which have there own specific measures 
params = 'params'				# Chart Specific Parameters to Capture - which are stored in the tech_indicators library

chart_schema = {
				'candlestick'	:{'display':True, 	primary:True,  params:None, },
				'scatter'		:{'display':False, 	primary:True,  params:None, },
				'bar'			:{'display':False, 	primary:True,  params:None, },
				'line'			:{'display':False, 	primary:True,  params:None, },
				'heiken_ashi'	:{'display':False, 	primary:True,  params:None, },
				'volume'		:{'display':True, 	primary:False, params:None, },
				'macd'			:{'display':True, 	primary:False, params:tech_indicators['macd'], },
				'stochastic'	:{'display':True, 	primary:False, params:tech_indicators['stochastic'], },
				'rsi'			:{'display':True, 	primary:False, params:tech_indicators['rsi'], },
				'vol_osssy'		:{'display':False, 	primary:False, params:tech_indicators['vol_osssy'], },
				'vac'			:{'display':False, 	primary:False, params:None, },
				}

def scope_chart(scope):
	scope.charts = chart_schema
