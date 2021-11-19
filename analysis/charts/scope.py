


from config.charts import chart_schema




def scope_chart(scope):
	scope.charts = chart_schema
	scope.rebuild_chart_df = True		# Default Flag to track if the analysis_df needs a refresh


