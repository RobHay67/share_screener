
def summarise_test_config_for_user(scope):

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


def summarise_chart_config_for_user(scope):

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
