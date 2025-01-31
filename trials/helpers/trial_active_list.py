import logging


def build_trial_active_list(scope):
	logging.debug("build_trial_active_list")
	# a list of every currently active trial
	# Seperate function so it can be called after the initial load - i.e. change user

	# Reset the list as this function will rebuild it
	scope.trials['active_list'] = []

	for trial in scope.trials['trial_list']:	
		if scope.trials['user_config'][trial]['active'] == True:
			scope.trials['active_list'].append(trial)

			