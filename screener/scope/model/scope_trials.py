# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!

from screener.scope.model.schema import trials_schema
from screener.scope.model.active_list import trial_active_list
from screener.scope.model.column_adders import trial_template_column_adders
from screener.scope.model.scope_user_config import user_config_trials


def scope_trials(scope):

	scope.trials = {}
	user_config_trials(scope)
	scope.trials['trial_list'] = list(trials_schema.keys())
	trial_active_list(scope)
	trial_template_column_adders(scope)
	




