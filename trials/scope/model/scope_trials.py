# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!

from trials.scope.model.schema import scope_trials_schema
from trials.helpers.trial_active_list import trial_active_list
from trials.scope.model.column_adders import trial_template_column_adders
from trials.scope.model.settings_for_user import trial_settings_for_user


def scope_trials(scope):

	scope.trials = {}
	scope_trials_schema(scope)
	trial_settings_for_user(scope)
	scope.trials['trial_list'] = list(scope.trials['schema'].keys())
	trial_active_list(scope)
	trial_template_column_adders(scope)
