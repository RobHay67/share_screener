import json


def save_users_table(scope):
	
	user = scope.users['login_name']
	
	if user != 'Login to Use the Application':
		print('Saving the Users Table')

		user_tests = tests_config(scope)
		user_charts = charts_config(scope)

		scope.users['json'][user]['chart_height'] = scope.config['charts']['primary_height']
		scope.users['json'][user]['download_days'] = scope.data['download']['days']
		scope.users['json'][user]['row_limit'] = scope.apps['row_limit']

		scope.users['json'][user]['tests'] = user_tests
		scope.users['json'][user]['charts'] = user_charts

		with open(scope.files['paths']['users'], 'w') as file:
			json.dump(scope.users['json'], file)


def tests_config(scope):

	# Summarise the current TESTS config for this user 

	test_dict = {}

	for test in scope.tests['test_list']:
		test_dict[test] = {}
		test_dict[test]['active'] = scope.tests[test]['active']
		add_columns = scope.tests[test]['add_columns']
		if add_columns != None:
			test_dict[test]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					test_dict[test]['add_columns'][attribute] = scope.tests[test]['add_columns'][attribute]
		else:
			test_dict[test]['add_columns'] = None

	return test_dict


def charts_config(scope):

	# Summarise the current CHARTS config for this user 

	chart_dict = {}

	for chart in scope.config['charts']['chart_list']:
		chart_dict[chart] = {}
		chart_dict[chart]['active'] = scope.config['charts'][chart]['active']
		add_columns = scope.config['charts'][chart]['add_columns']
		if add_columns != None:
			chart_dict[chart]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					chart_dict[chart]['add_columns'][attribute] = scope.config['charts'][chart]['add_columns'][attribute]

		else:
			chart_dict[chart]['add_columns'] = None	

	return chart_dict

	