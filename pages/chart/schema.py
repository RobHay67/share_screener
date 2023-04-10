

def create_schema_for_plotly(scope):
	schema = {
			'no_of_charts'			: 0,
			'col_no' 				: 1,
			'chart_heights' 		: [],
			'add_chart' 			: [],
			'add_overlay'			: [],
	}

	# Based on the User Selections - construct lists and variables (a Schema) of objects that need rendering
	for chart in scope.chart_settings['chart_list']:	
		if scope.charts[chart]['active'] == True and scope.charts[chart]['is_overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			schema['no_of_charts'] = schema['no_of_charts'] + 1
			schema['chart_heights'].append(scope.charts[chart]['plot']['scale'])
			schema['add_chart'].append(chart)
		elif  scope.charts[chart]['active'] == True and scope.charts[chart]['is_overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			schema['add_overlay'].append(chart)	

	schema = make_chart_heights_proportional(scope, schema)

	return schema



def make_chart_heights_proportional(scope, schema):
	for pos, percentage_height in enumerate(schema['chart_heights']):
		chart_pixel_height = scope.chart_settings['primary_height'] * percentage_height
		schema['chart_heights'][pos] = chart_pixel_height

	scope.chart_settings['total_height'] = sum(schema['chart_heights'])
	return schema



# Sample Schema
# {
# 	'no_of_charts': 7, 
# 	'col_no': 1, 
# 	'chart_heights': [500.0, 250.0, 125.0, 250.0, 250.0, 250.0, 250.0], 
# 	'add_chart': ['candlestick', 'line', 'volume', 'macd', 'macd_vol', 'rsi', 'stochastic'],
# 	'add_overlay': ['sma_1', 'dividends']
# }