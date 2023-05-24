

from users.config import base_config_users
from charts.config import base_config_charts
from trials.config import base_config_trials
from page.config import base_config_pages
from y_finance.config import set_yf_period


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

	# Download Days (for yahoo_finance module)
	set_yf_period(scope)


	# TODO - what about the trials config - should this also not revert to the base values
