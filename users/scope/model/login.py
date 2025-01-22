from screener.scope.model.scope_trials import trial_active_list
from screener.scope.model.scope_trials import trial_template_column_adders
from charts.scope.model.scope_charts import chart_active_list
from charts.scope.model.scope_charts import chart_column_adders

# from users.views
from users.views.page_welcome import show_welcome_page

def login_user(scope, login_name):
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
			add_columns = user_trial_settings[trial]['add_columns']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.trials['user_config'][trial]['add_columns'][attribute] = add_columns[attribute]
	
	# refresh the Trial lists
	trial_active_list(scope)
	trial_template_column_adders(scope)


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
			add_columns = user_chart_settings[chart]['add_columns']
			if add_columns != None:
				for attribute in add_columns.keys():
					scope.charts['user_config'][chart]['add_columns'][attribute] = add_columns[attribute]

		
	# refresh the Chart lists
	chart_active_list(scope)
	chart_column_adders(scope)

	# open the Welcome Page?
	show_welcome_page(scope)













