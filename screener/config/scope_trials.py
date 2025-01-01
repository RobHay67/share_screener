# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!

from screener.config.schema import trial_configuration_dict
from screener.config.active_list import trial_active_list
from screener.config.add_columns import trial_column_adders
from screener.config.user import user_config_trials


def scope_trials(scope):

	scope.trials = {}
	user_config_trials(scope)
	scope.trials['trial_list'] = list(trial_configuration_dict.keys())
	trial_active_list(scope)
	trial_column_adders(scope)




