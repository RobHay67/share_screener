





def scope_active_trial_list(scope):
	active_trial_list = []
	
	for trial in scope.trial_config['trial_list']:	
		if scope.trials[trial]['active'] == True:
			active_trial_list.append(trial)

	return active_trial_list


