
import time  


def scope_application_variables(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] = time.time()

	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere

