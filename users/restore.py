
from charts.config import base_config_charts
from tickers.config import base_config_download
from apps.config import base_config_apps
from users.config import base_config_users

def restore_base_config(scope):
	# Reinstate default user setting across config

	# Default User Name
	base_config_users(scope)

	# Primary Chart Height
	base_config_charts(scope)

	# Download Days
	base_config_download(scope)

	# row_limit
	base_config_apps(scope)
