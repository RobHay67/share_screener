

from users.scope.model.scope_users import user_config_users
from charts.scope.model.scope_charts import chart_settings_for_user
from trials.scope.model.scope_trials import trial_settings_for_user
from config.scope.model.scope_config import user_config_pages


def restore_base_config(scope):
	# Reinstate default user setting across config

	# Default User Name
	user_config_users(scope)

	# Chart Config and Chart Height
	chart_settings_for_user(scope)

	# Trial Config
	trial_settings_for_user(scope)

	# row_limit
	user_config_pages(scope)


	# TODO - what about the trials config - should this also not revert to the base values
