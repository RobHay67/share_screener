from trials.config import trial_column_adders
from charts.config import chart_column_adders

def set_user_access(scope:dict, login_name:str):

	# Store User params
	scope.apps['display_app'] = 'home_page'
	scope.users['login_name'] = login_name

	# Determine the Users Settings
	user_trials = scope.users['json'][login_name]['trials']
	user_charts = scope.users['json'][login_name]['charts']

	# Over-write key user settings
	scope.charts['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.download['days'] = scope.users['json'][login_name]['download_days']
	scope.apps['row_limit'] = scope.users['json'][login_name]['row_limit']


	# Over-write the trials settings with the user trial values
	for trial in user_trials.keys():
		active_status = user_trials[trial]['active']
		add_columns = user_trials[trial]['add_columns']

		# Update the user config into the scope.config
		scope.trials['config'][trial]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.trials['config'][trial]['add_columns'][attribute] = add_columns[attribute]
	
	# refresh the list of active column adders for trials
	trial_column_adders(scope)

	# Over-write the config charts with the user values
	for chart in user_charts.keys():

		active_status = user_charts[chart]['active']
		add_columns = user_charts[chart]['add_columns']
		
		# Update the user config into the scope.config
		scope.charts['config'][chart]['active'] = active_status
		if add_columns != None:
			for attribute in add_columns.keys():
				scope.charts['config'][chart]['add_columns'][attribute] = add_columns[attribute]

		
	# refresh the list of active column adders for charts
	chart_column_adders(scope)











