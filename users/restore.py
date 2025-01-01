

from users.scope_users import user_config_users
from charts.config.scope_charts import user_config_charts
from screener.config.scope_trials import user_config_trials
from app.scope_pages import user_config_pages


def restore_base_config(scope):
	# Reinstate default user setting across config

	# Default User Name
	user_config_users(scope)

	# Chart Config and Chart Height
	user_config_charts(scope)

	# Trial Config
	user_config_trials(scope)

	# row_limit
	user_config_pages(scope)


	# TODO - what about the trials config - should this also not revert to the base values
