import json


def save_users_table(scope):
	
	user = scope.users['login_name']
	
	if user != 'Login to Use the Application':
		print('Saving the Users Table')
		
		# Set User Variables to the values currently stored in the application
		scope.users['json'][user]['chart_height'] = scope.charts['primary_height']
		scope.users['json'][user]['download_days'] = scope.pages['download_days']
		scope.users['json'][user]['row_limit'] = scope.pages['row_limit']
		scope.users['json'][user]['yf_period'] = scope.yf['period']

		# Set User Trial and Chart Variables to the values currently stored in the application
		user_trials = trials_config(scope)
		user_charts = charts_config(scope)

		scope.users['json'][user]['trials'] = user_trials
		scope.users['json'][user]['charts'] = user_charts

		with open(scope.files['paths']['users'], 'w') as file:
			json.dump(scope.users['json'], file)


def trials_config(scope):

	# Summarise the current TRIALS config for this user 
	excluded_attribute_list = ['function']

	trial_dict = {}

	for trial in scope.trials['trial_list']:
		trial_dict[trial] = {}

		# Save the overall active setting for the trial
		trial_dict[trial]['active'] = scope.trials['config'][trial]['active']
		
		# Save any column adding settings (i.e. selected column or duration)
		add_columns = scope.trials['config'][trial]['add_columns']
		if add_columns != None:
			trial_dict[trial]['add_columns'] = {}
			for attribute in add_columns.keys():
				# Save attributes (unless exluded)
				if attribute not in excluded_attribute_list:
					trial_dict[trial]['add_columns'][attribute] = scope.trials['config'][trial]['add_columns'][attribute]
		else:
			trial_dict[trial]['add_columns'] = None

	return trial_dict


def charts_config(scope):

	# Summarise the current CHARTS config for this user 
	excluded_attribute_list = ['function']

	chart_dict = {}

	for chart in scope.charts['chart_list']:
		chart_dict[chart] = {}

		# print(scope.charts['config'][chart].keys())

		# Save the overall active setting for the chart
		chart_dict[chart]['active'] = scope.charts['config'][chart]['active']

		# Save active_column attributes
		if 'active_columns' in scope.charts['config'][chart].keys():
			chart_dict[chart]['active_columns'] = scope.charts['config'][chart]['active_columns']

		# Save any column adding settings (i.e. selected column or duration)
		add_columns = scope.charts['config'][chart]['add_columns']
		if add_columns != None:
			chart_dict[chart]['add_columns'] = {}
			for attribute in add_columns.keys():
				# Save attributes (unless exluded)
				if attribute not in excluded_attribute_list:
					chart_dict[chart]['add_columns'][attribute] = scope.charts['config'][chart]['add_columns'][attribute]

		else:
			chart_dict[chart]['add_columns'] = None	

	return chart_dict

	