import logging

def chart_active_list(scope):
	logging.debug("chart_active_list")
	# Seperate function so it can be called after the initial load - i.e. change user
	# Reset the list as this function will rebuild it
	scope.charts['active_list'] = []

	for chart in scope.charts['chart_list']:	
		if scope.charts['user_config'][chart]['active'] == True:
			scope.charts['active_list'].append(chart)

			