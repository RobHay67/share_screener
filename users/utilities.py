
def summarise_trial_config_for_user(scope):

	trial_dict = {}

	for trial in scope.trials['trial_list']:
		trial_dict[trial] = {}
		trial_dict[trial]['active'] = scope.trials[trial]['active']
		add_columns = scope.trials[trial]['add_columns']
		if add_columns != None:
			trial_dict[trial]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					trial_dict[trial]['add_columns'][attribute] = scope.trials[trial]['add_columns'][attribute]
		else:
			trial_dict[trial]['add_columns'] = None

	return trial_dict


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
