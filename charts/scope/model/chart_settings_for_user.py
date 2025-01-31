import logging

def scope_charts_for_users(scope):
	logging.debug("scope_charts_for_users")
	# Setting can be changed for each user
	# so we need to be able to call when changing user

	scope.charts['primary_height'] = 500
	scope.charts['total_height'] = scope.charts['primary_height']

	# store the default chart configuration dictionary (over-written by user settings)
	scope.charts['user_config'] = {}
	for chart, config in scope.charts['schema'].items():
		scope.charts['user_config'][chart] = config.copy()