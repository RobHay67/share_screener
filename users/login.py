from trials.config import trial_active_list
from trials.config import trial_column_adders
from charts.config import chart_active_list
from charts.config import chart_column_adders

def login_user(scope, login_name):

	# Store User params
	scope.display_page = 'home_page'
	scope.users['login_name'] = login_name
	scope.user_logged_in = True

	# Determine the Users Settings
	user_trials = scope.users['json'][login_name]['trials']
	user_charts = scope.users['json'][login_name]['charts']

	# Over-write key user settings
	scope.chart_config['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.download['days'] = scope.users['json'][login_name]['download_days']
	scope.pages['row_limit'] = scope.users['json'][login_name]['row_limit']


	# Over-write the trials settings with the user trial values
	for trial in user_trials.keys():
		if trial in scope.trials.keys():
			active_status = user_trials[trial]['active']
			add_columns = user_trials[trial]['add_columns']

			# Update the user config into the scope.config
			scope.trials[trial]['active'] = active_status
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.trials[trial]['add_columns'][attribute] = add_columns[attribute]
	
	# refresh the trial_config lists
	trial_active_list(scope)
	trial_column_adders(scope)

	# Over-write the config charts with the user values
	for chart in user_charts.keys():
		if chart in scope.charts.keys():
			active_status = user_charts[chart]['active']
			add_columns = user_charts[chart]['add_columns']
			
			# Update the user config into the scope.config
			scope.charts[chart]['active'] = active_status
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.charts[chart]['add_columns'][attribute] = add_columns[attribute]

		
	# refresh the chart_config lists
	chart_active_list(scope)
	chart_column_adders(scope)












