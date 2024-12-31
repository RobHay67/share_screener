# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!

from screener.config.trials import trial_configuration_dict
from screener.config.active_list import trial_active_list
from screener.config.add_columns import trial_column_adders


def scope_trials(scope):

	scope.trials = {}
	base_config_trials(scope)
	scope.trials['trial_list'] = list(trial_configuration_dict.keys())
	trial_active_list(scope)
	trial_column_adders(scope)


def base_config_trials(scope):
	# store the trial configuration dictionary (from below)
	scope.trials['config'] = {}
	for trial, configuration in trial_configuration_dict.items():
		scope.trials['config'][trial] = configuration.copy()





