from trials.config import trial_active_list
from trials.config import trial_column_adders
from charts.config import chart_active_list
from charts.config import chart_column_adders

def login_user(scope, login_name):

	# Store User params
	# scope.pages['display'] = 'home_page'
	scope.users['login_name'] = login_name
	scope.users['logged_in'] = True

	# Over-write global user settings
	scope.charts['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.pages['download_days'] = scope.users['json'][login_name]['download_days']
	scope.pages['row_limit'] = scope.users['json'][login_name]['row_limit']
	scope.yf['period'] = scope.users['json'][login_name]['yf_period']

	# ========================================================
	# Trial Settings
	# Over-write the scope.trials['config'] settings with the user values

	user_trial_settings = scope.users['json'][login_name]['trials']
	
	for trial in user_trial_settings.keys():
		# Ensure the TRIAL is still available
		if trial in scope.trials['config'].keys():
			
			# Trial Active Status
			scope.trials['config'][trial]['active'] = user_trial_settings[trial]['active']

			# Trial additional column attribute settings
			add_columns = user_trial_settings[trial]['add_columns']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.trials['config'][trial]['add_columns'][attribute] = add_columns[attribute]
	
	# refresh the Trial lists
	trial_active_list(scope)
	trial_column_adders(scope)


	# ========================================================
	# Chart Settings
	# Over-write the scope.charts['config'] settings with the user values

	user_chart_settings = scope.users['json'][login_name]['charts']

	for chart in user_chart_settings.keys():
		# Ensure the CHART is still available
		if chart in scope.charts['config'].keys():
			
			# Chart Active Status
			scope.charts['config'][chart]['active'] = user_chart_settings[chart]['active']

			# Chart Active_Columns (if available)
			if 'active_columns' in user_chart_settings[chart].keys():
				scope.charts['config'][chart]['active_columns'] = user_chart_settings[chart]['active_columns']

			# Chart additional column attribute settings
			add_columns = user_chart_settings[chart]['add_columns']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.charts['config'][chart]['add_columns'][attribute] = add_columns[attribute]

		
	# refresh the Chart lists
	chart_active_list(scope)
	chart_column_adders(scope)












