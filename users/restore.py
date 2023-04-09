

from users.config import base_config_users
from charts.config import base_config_charts
from page.config.application import base_config_download_days
from page.config.pages import base_config_pages
from y_finance.config import set_yf_period


def restore_base_config(scope):
	# Reinstate default user setting across config

	# Default User Name
	base_config_users(scope)

	# Primary Chart Height
	base_config_charts(scope)

	# Download Days
	base_config_download_days(scope)
	set_yf_period(scope)

	# row_limit
	base_config_pages(scope)


	# TODO - what about the trials config - should this also not revert to the base values
