import logging

from users.scope.model.scope_users import scope_users_for_users
from charts.scope.model.scope_charts import scope_charts_for_users
from trials.scope.model.scope_trials import scope_trials_for_users_settings
from config.scope.model.scope_config import scope_config_for_users_settings


def restore_user_config(scope):
	logging.debug("restore_user_config")
	# Reinstate default user setting across config

	# Default User Name
	scope_users_for_users(scope)

	# Chart Config and Chart Height
	scope_charts_for_users(scope)

	# Trial Config
	scope_trials_for_users_settings(scope)

	# row_limit
	scope_config_for_users_settings(scope)


	# TODO - what about the trials config - should this also not revert to the base values
