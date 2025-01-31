# Not sure what these are for anymore
# TODO - might be able to delete these later
import logging


def summarise_trial_config_for_user(scope):
	logging.debug("summarise_trial_config_for_user")
	trial_dict = {}

	for trial in scope.trials['trial_list']:
		trial_dict[trial] = {}
		trial_dict[trial]['active'] = scope.trials['user_config'][trial]['active']
		add_columns = scope.trials['user_config'][trial]['function']
		if add_columns != None:
			trial_dict[trial]['function'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					trial_dict[trial]['function'][attribute] = scope.trials['user_config'][trial]['function'][attribute]
		else:
			trial_dict[trial]['function'] = None

	return trial_dict


def summarise_chart_config_for_user(scope):
	logging.debug("summarise_chart_config_for_user")
	chart_dict = {}

	for chart in scope.charts['chart_list']:
		chart_dict[chart] = {}
		chart_dict[chart]['active'] = scope.charts['user_config'][chart]['active']
		add_columns = scope.charts['user_config'][chart]['function']
		if add_columns != None:
			chart_dict[chart]['function'] = {}
			for attribute in add_columns.keys():
				if attribute not in ['function']:
					chart_dict[chart]['function'][attribute] = scope.charts['user_config'][chart]['function'][attribute]

		else:
			chart_dict[chart]['function'] = None	

	return chart_dict
