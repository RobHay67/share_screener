# Not sure what these are for anymore
# TODO - might be able to delete these later



def summarise_trial_config_for_user(scope):

	trial_dict = {}

	for trial in scope.trials['trial_list']:
		trial_dict[trial] = {}
		trial_dict[trial]['active'] = scope.trials['config'][trial]['active']
		add_columns = scope.trials['config'][trial]['add_columns']
		if add_columns != None:
			trial_dict[trial]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					trial_dict[trial]['add_columns'][attribute] = scope.trials['config'][trial]['add_columns'][attribute]
		else:
			trial_dict[trial]['add_columns'] = None

	return trial_dict


def summarise_chart_config_for_user(scope):

	chart_dict = {}

	for chart in scope.charts['chart_list']:
		chart_dict[chart] = {}
		chart_dict[chart]['active'] = scope.charts['config'][chart]['active']
		add_columns = scope.charts['config'][chart]['add_columns']
		if add_columns != None:
			chart_dict[chart]['add_columns'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					chart_dict[chart]['add_columns'][attribute] = scope.charts['config'][chart]['add_columns'][attribute]

		else:
			chart_dict[chart]['add_columns'] = None	

	return chart_dict
