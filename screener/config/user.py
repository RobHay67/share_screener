
from screener.config.schema import trial_configuration_dict

def user_config_trials(scope):
	# store the trial configuration dictionary (from below)
	scope.trials['user_config'] = {}
	for trial, configuration in trial_configuration_dict.items():
		scope.trials['user_config'][trial] = configuration.copy()



