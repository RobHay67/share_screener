

def chart_active_list(scope):
	# Seperate function so it can be called after the initial load - i.e. change user
	# Reset the list as this function will rebuild it
	scope.charts['active_list'] = []

	for chart in scope.charts['chart_list']:	
		if scope.charts['config'][chart]['active'] == True:
			scope.charts['active_list'].append(chart)

			