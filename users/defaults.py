

from config.tests.config import scope_tests
from config.charts.config import scope_charts


def set_user_defaults(scope):


	# Reset the login status
	scope.users['login_name'] = 'Login to Use the Application'
	scope.pages['display_page'] = 'login'
	
	# Reset the test and chart config back to be the defaults
	scope_tests(scope)
	scope_charts(scope)

