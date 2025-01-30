



def trial_template_column_adders(scope):
	# A dictionary of every trial that requires additional columns
	# ignore and trials that dont have column adders
	# Seperate function, so it can be called after the initial load - i.e. change user

	# Reset the dictionary as calling this function will recreate the dictionary
	scope.trials['template_col_adders'] = {}

	for trial in scope.trials['trial_list']:
		if scope.trials['user_config'][trial]['function'] != None:
		# Add trials that require additional columns
			active_status_of_trial = scope.trials['user_config'][trial]['active']
			scope.trials['template_col_adders'][trial] = active_status_of_trial


