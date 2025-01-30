

def trial_settings_for_user(scope):
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in scope.trials['schema'].items():
		scope.trials['user_config'][trial] = configuration.copy()



