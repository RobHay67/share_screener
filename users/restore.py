

from users.config import base_config_users
from charts.config import base_config_charts
from screener.config import base_config_trials
from views.app_config import base_config_pages


def restore_base_config(scope):
	# Reinstate default user setting across config

	# Default User Name
	base_config_users(scope)

	# Chart Config and Chart Height
	base_config_charts(scope)

	# Trial Config
	base_config_trials(scope)

	# row_limit
	base_config_pages(scope)


	# TODO - what about the trials config - should this also not revert to the base values
