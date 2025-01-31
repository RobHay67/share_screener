import logging


def scope_trials_for_users(scope):
	logging.debug("scope_trials_for_users")
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in scope.trials['schema'].items():
		scope.trials['user_config'][trial] = configuration.copy()



