


def make_chart_heights_proportional(scope, plotly_schema):
	for pos, percentage_height in enumerate(plotly_schema['chart_heights']):
		chart_pixel_height = scope.primary_chart_height * percentage_height
		plotly_schema['chart_heights'][pos] = chart_pixel_height

	scope.charts_total_height = sum(plotly_schema['chart_heights'])
	return plotly_schema


	