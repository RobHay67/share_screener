

from charts.helpers.chart_height import make_chart_heights_proportional


def create_plotly_schema(scope):
	plotly_schema = {
			'no_of_charts'			: 0,
			'col_no' 				: 1,
			'chart_heights' 		: [],
			'requested_charts' 		: [],
			'requested_overlays'	: [],
	}

	# Based on the User Selections - construct lists and variables of objects that need rendering
	for chart in scope.charts.keys():
		if scope.charts[chart]['active'] == True and scope.charts[chart]['is_overlay'] == False: 			# Charts - Selected (active) and IS NOT an overlay
			plotly_schema['no_of_charts'] = plotly_schema['no_of_charts'] + 1
			plotly_schema['chart_heights'].append(scope.charts[chart]['plot']['scale'])
			plotly_schema['requested_charts'].append(chart)
		elif  scope.charts[chart]['active'] == True and scope.charts[chart]['is_overlay'] == True:			# Overlays - Selected (active) and IS an overlay
			plotly_schema['requested_overlays'].append(chart)	

	plotly_schema = make_chart_heights_proportional(scope, plotly_schema)

	return plotly_schema