

from trials.config import scope_trials
from charts.config import scope_charts


def set_user_defaults(scope):


	# Reset the login status
	scope.users['login_name'] = 'Login to Use the Application'
	scope.apps['display_app'] = 'login'
	
	# Reset the trial and chart config back to be the defaults
	scope_trials(scope)
	scope_charts(scope)

