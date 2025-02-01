import logging


def scope_trials_for_users_settings(scope):
	logging.debug("scope_trials_for_users_settings")
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in scope.trials['schema'].items():
		scope.trials['user_config'][trial] = configuration.copy()



