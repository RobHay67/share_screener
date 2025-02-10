import logging
from users.page_welcome import show_welcome_page
from trials.scope.scope_trials import build_trials_active_list
from trials.scope.scope_trials import build_trials_column_adder_template
from charts.scope.scope_charts import build_chart_active_list
from charts.scope.scope_charts import build_charts_column_adder_template


def login_user(scope, login_name):
	logging.warning("login_user")
	# Store User params

	scope.users['login_name'] = login_name
	scope.users['logged_in'] = True

	# Over-write global user settings
	scope.charts['primary_height'] = scope.users['json'][login_name]['chart_height']
	scope.config['download_days'] = scope.users['json'][login_name]['download_days']
	scope.config['row_limit'] = scope.users['json'][login_name]['row_limit']

	# ========================================================
	# Trial Settings
	# Over-write the scope.trials['user_config'] settings with the user values

	user_trial_settings = scope.users['json'][login_name]['trials']
	
	for trial in user_trial_settings.keys():
		# Ensure the TRIAL is still available
		if trial in scope.trials['user_config'].keys():
			
			# Trial Active Status
			scope.trials['user_config'][trial]['active'] = user_trial_settings[trial]['active']

			# Trial additional column attribute settings
			add_columns = user_trial_settings[trial]['function']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.trials['user_config'][trial]['function'][attribute] = add_columns[attribute]
	
	# refresh the Trial lists
	build_trials_active_list(scope)
	build_trials_column_adder_template(scope)


	# ========================================================
	# Chart Settings
	# Over-write the scope.charts['user_config'] settings with the user values

	user_chart_settings = scope.users['json'][login_name]['charts']

	for chart in user_chart_settings.keys():
		# Ensure the CHART is still available
		if chart in scope.charts['user_config'].keys():
			
			# Chart Active Status
			scope.charts['user_config'][chart]['active'] = user_chart_settings[chart]['active']

			# Chart Active_Columns (if available)
			if 'active_columns' in user_chart_settings[chart].keys():
				scope.charts['user_config'][chart]['active_columns'] = user_chart_settings[chart]['active_columns']

			# Chart additional column attribute settings
			add_columns = user_chart_settings[chart]['function']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.charts['user_config'][chart]['function'][attribute] = add_columns[attribute]

		
	# refresh the Chart lists
	build_chart_active_list(scope)
	build_charts_column_adder_template(scope)

	# open the Welcome Page?
	show_welcome_page(scope)
	
	













