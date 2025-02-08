import logging

def save_trials_user_settings(scope):
	logging.warning("save_trials_user_settings")
	# Summarise the current TRIALS config for this user 
	excluded_attribute_list = ['function']

	trial_dict = {}

	for trial in scope.trials['trial_list']:
		trial_dict[trial] = {}

		# Save the overall active setting for the trial
		trial_dict[trial]['active'] = scope.trials['user_config'][trial]['active']
		
		# Save any column adding settings (i.e. selected column or duration)
		add_columns = scope.trials['user_config'][trial]['function']
		if add_columns != None:
			trial_dict[trial]['function'] = {}
			for attribute in add_columns.keys():
				# Save attributes (unless exluded)
				if attribute not in excluded_attribute_list:
					trial_dict[trial]['function'][attribute] = scope.trials['user_config'][trial]['function'][attribute]
		else:
			trial_dict[trial]['function'] = None

	return trial_dict


