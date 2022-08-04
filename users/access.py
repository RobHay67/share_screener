


def set_user_access(scope:dict, login_name:str):

	# Store User params
	scope.apps['display_app'] = 'home_page'
	scope.users['login_name'] = login_name

	# Determine the Users Settings
	user_trials = scope.users['json'][login_name]['trials']
	user_charts = scope.users['json'][login_name]['charts']

	# Over-write key user settings
	scope.charts['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.data['download']['days'] = scope.users['json'][login_name]['download_days']
	scope.apps['row_limit'] = scope.users['json'][login_name]['row_limit']


	# Over-write the config trials with the user values
	for trial in user_trials.keys():
		active_status = user_trials[trial]['active']
		add_columns = user_trials[trial]['add_columns']

		# Update the app.template
		scope.apps['templates']['trials'][trial] = active_status

		# Update the user config into the scope.config
		scope.trials[trial]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.trials[trial]['add_columns'][attribute] = add_columns[attribute]

	# Over-write the config charts with the user values
	for chart in user_charts.keys():

		active_status = user_charts[chart]['active']
		add_columns = user_charts[chart]['add_columns']
		
		# Update the app.template
		scope.apps['templates']['charts'][chart] = active_status

		# Update the user config into the scope.config
		scope.charts[chart]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.charts[chart]['add_columns'][attribute] = add_columns[attribute]

		













