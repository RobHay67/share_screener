from charts.scope.model.schema import charts_config

def user_config_charts(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.charts['primary_height'] = 500
	scope.charts['total_height'] = scope.charts['primary_height']

	# store the default chart configuration dictionary (over-written by user settings)
	scope.charts['user_config'] = {}
	for chart, config in charts_config.items():
		scope.charts['user_config'][chart] = config.copy()