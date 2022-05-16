



from users.model.logout import set_user_defaults


def scope_user(scope:dict):

	scope.users = {}

	set_user_defaults(scope)
	# scope.user_pword = None




def set_user_access(scope:dict, login_name:str):

	print('setting user access')

	scope.pages['display_page'] = 'welcome'

	scope.users['login_name'] = login_name
	# scope.user_pword = None

	user_tests = scope.users['json'][login_name]['tests']
	user_charts = scope.users['json'][login_name]['charts']

	for test in user_tests.keys():
		active_status = user_tests[test]['active']
		add_columns = user_tests[test]['add_columns']

		scope.config['tests'][test]['active'] = active_status

		if add_columns != None:
			for attribute in add_columns.keys():
				scope.config['tests'][test]['add_columns'][attribute] = add_columns[attribute]

	for chart in user_charts.keys():
		active_status = user_charts[chart]['active']
		add_columns = user_charts[chart]['add_columns']

		scope.config['charts'][chart]['active'] = active_status

		if add_columns != None:
			for attribute in add_columns.keys():
				scope.config['charts'][chart]['add_columns'][attribute] = add_columns[attribute]

		














