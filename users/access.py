


def set_user_access(scope:dict, login_name:str):

	# Store User params
	scope.apps['display_app'] = 'home_page'
	scope.users['login_name'] = login_name

	# Determine the Users Settings
	user_tests = scope.users['json'][login_name]['tests']
	user_charts = scope.users['json'][login_name]['charts']

	# Over-write key user settings
	scope.config['charts']['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.data['download']['days'] = scope.users['json'][login_name]['download_days']
	scope.apps['row_limit'] = scope.users['json'][login_name]['row_limit']


	# Over-write the config tests with the user values
	for test in user_tests.keys():
		active_status = user_tests[test]['active']
		add_columns = user_tests[test]['add_columns']

		# Update the app.template
		scope.apps['templates']['tests'][test] = active_status

		# Update the user config into the scope.config
		scope.tests[test]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.tests[test]['add_columns'][attribute] = add_columns[attribute]

	# Over-write the config charts with the user values
	for chart in user_charts.keys():

		active_status = user_charts[chart]['active']
		add_columns = user_charts[chart]['add_columns']
		
		# Update the app.template
		scope.apps['templates']['charts'][chart] = active_status

		# Update the user config into the scope.config
		scope.config['charts'][chart]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.config['charts'][chart]['add_columns'][attribute] = add_columns[attribute]

		













