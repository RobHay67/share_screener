

from pages.single.chart_height import make_chart_heights_proportional


def create_plotly_schema(scope):
	plotly_schema = {
			'no_of_charts'			: 0,
			'col_no' 				: 1,
			'chart_heights' 		: [],
			'add_chart' 			: [],
			'add_overlay'			: [],
	}

	# Based on the User Selections - construct lists and variables (a Schema) of objects that need rendering
	for chart in scope.config['charts']['chart_list']:	
		if scope.config['charts'][chart]['active'] == True and scope.config['charts'][chart]['is_overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			plotly_schema['no_of_charts'] = plotly_schema['no_of_charts'] + 1
			plotly_schema['chart_heights'].append(scope.config['charts'][chart]['plot']['scale'])
			plotly_schema['add_chart'].append(chart)
		elif  scope.config['charts'][chart]['active'] == True and scope.config['charts'][chart]['is_overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			plotly_schema['add_overlay'].append(chart)	

	plotly_schema = make_chart_heights_proportional(scope, plotly_schema)

	return plotly_schema