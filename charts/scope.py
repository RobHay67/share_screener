


from config.charts import chart_schema, chart_colours




def scope_chart(scope):
	scope.charts = chart_schema
	scope.primary_chart_height = 500
	scope.charts_total_height = scope.primary_chart_height
	scope.chart_colours = chart_colours
	




