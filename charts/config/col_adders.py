
def chart_column_adders(scope):
	# Reset the list as this function will rebuild it
	scope.charts['template_col_adders'] = {}

	for chart in scope.charts['chart_list']:
		# Only add charts that require additional columns
		if scope.charts['config'][chart]['add_columns'] != None:
			scope.charts['template_col_adders'][chart] = scope.charts['config'][chart]['active']

