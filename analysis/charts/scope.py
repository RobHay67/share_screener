


from config.charts import chart_schema, chart_colours




def scope_chart(scope):
	scope.charts = chart_schema
	scope.primary_chart_height = 1000
	scope.chart_colours = chart_colours
	scope.rebuild_chart_df = True		# Default Flag to track if the analysis_df needs a refresh

	

