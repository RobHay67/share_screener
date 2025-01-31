import logging


def build_column_adder_template_for_charts(scope):
	logging.debug("build_column_adder_template_for_charts")
	# Reset the list as this function will rebuild it
	scope.charts['template_col_adders'] = {}

	for chart in scope.charts['chart_list']:
		# Only include charts that require additional columns
		if scope.charts['user_config'][chart]['function'] != None:
			scope.charts['template_col_adders'][chart] = scope.charts['user_config'][chart]['active']

