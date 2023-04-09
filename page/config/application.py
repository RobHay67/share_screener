
import time  


def scope_application_variables(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] = time.time()

	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere

	# Download Days
	base_config_download_days(scope)


def base_config_download_days(scope):
	# Setting can be changed for each user
	# so we need to be able to call when changing user
	scope.config['download_days'] = 7
