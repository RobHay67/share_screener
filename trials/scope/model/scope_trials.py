# trials_config - all config
# trial_list	- list of trial config keys
# active_list	- list of active trial config keys
# column_adders	- dict of { trial : active_status } (includes active and inactive)

# trials is the config
# trials_config are the current settings!!!
import logging
from trials.scope.model.schema import scope_trials_schema
from trials.helpers.trial_active_list import build_trials_active_list
from trials.scope.model.column_adders import build_trials_column_adder_template
from trials.scope.model.settings_for_user import scope_trials_for_users_settings


def scope_trials(scope):
	logging.warning("scope_trials")
	scope.trials = {}
	scope_trials_schema(scope)
	scope_trials_for_users_settings(scope)
	scope.trials['trial_list'] = list(scope.trials['schema'].keys())
	build_trials_active_list(scope)
	build_trials_column_adder_template(scope)
