import logging

from users.scope.scope_users import scope_users_for_users_settings
from charts.scope.scope_charts import scope_charts_for_users_settings
from trials.scope.scope_trials import scope_trials_for_users_settings
from config.scope.scope_config import scope_config_for_users_settings
from users.helpers.reset_page_to_defaults import reset_page_to_default_values


def set_user_config_to_default_values(scope):
	logging.warning("set_user_config_to_default_values")
	# Reinstate default user setting across config

	# Default User Name
	scope_users_for_users_settings(scope)

	# Chart Config and Chart Height
	scope_charts_for_users_settings(scope)

	# Trial Config
	scope_trials_for_users_settings(scope)

	# row_limit
	scope_config_for_users_settings(scope)

	# Reset Selectors
	reset_page_to_default_values(scope)
