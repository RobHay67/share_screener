import json


def save_users_table(scope):
	
	# Save the User Table

	# print('-'*80)
	# print('saving Users Json')
	# print('Users Dataframe')
	# print('-'*80)



	# we really should be just saving users as a dictionary
	# TODO - remove this after forst successfule save
	# users={}
	# users['Rob'] = {'password': 'password', 'tests': {}, 'charts': {}}
	# users['Fliss'] = {'password': 'password', 'tests': {}, 'charts': {}}
	# scope.users['json'] = users

	# we know what we loaded
	# for the particular user, we just need to replace the charts and tests component

	user = scope.users['login_name']
	
	if user != 'Login to Use the Application':
		print('Saving the Users Table')

		user_tests = build_tests_config_for_user(scope)
		user_charts = build_charts_config_for_user(scope)

		scope.users['json'][user]['tests'] = user_tests
		scope.users['json'][user]['charts'] = user_charts

		with open(scope.files['paths']['users'], 'w') as file:
			json.dump(scope.users['json'], file)




def build_tests_config_for_user(scope):

	test_dict = {}

	for test in scope.config['tests']['test_list']:
		test_dict[test] = {}
		test_dict[test]['active'] = scope.config['tests'][test]['active']
		add_columns = scope.config['tests'][test]['add_columns']
		if add_columns != None:
			test_dict[test]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					test_dict[test]['add_columns'][attribute] = scope.config['tests'][test]['add_columns'][attribute]
		else:
			test_dict[test]['add_columns'] = None

	return test_dict

def build_charts_config_for_user(scope):

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


# def create_base_user_file():



	