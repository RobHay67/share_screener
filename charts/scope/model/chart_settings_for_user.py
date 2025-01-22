

def chart_settings_for_user(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.charts['primary_height'] = 500
	scope.charts['total_height'] = scope.charts['primary_height']

	# store the default chart configuration dictionary (over-written by user settings)
	scope.charts['user_config'] = {}
	for chart, config in scope.charts['schema'].items():
		scope.charts['user_config'][chart] = config.copy()