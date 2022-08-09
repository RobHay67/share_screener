import json


def save_users_table(scope):
	
	user = scope.users['login_name']
	
	if user != 'Login to Use the Application':
		print('Saving the Users Table')

		
		# Set User Variables to the values currently stored in the application
		scope.users['json'][user]['chart_height'] = scope.charts['primary_height']
		scope.users['json'][user]['download_days'] = scope.download['days']
		scope.users['json'][user]['row_limit'] = scope.apps['row_limit']


		# Set User Trial and Chart Variables to the values currently stored in the application
		user_trials = trials_config(scope)
		user_charts = charts_config(scope)

		scope.users['json'][user]['trials'] = user_trials
		scope.users['json'][user]['charts'] = user_charts

		with open(scope.files['paths']['users'], 'w') as file:
			json.dump(scope.users['json'], file)


def trials_config(scope):

	# Summarise the current TRIALS config for this user 

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


def charts_config(scope):

	# Summarise the current CHARTS config for this user 

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

	