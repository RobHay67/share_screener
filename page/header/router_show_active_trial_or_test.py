import logging
from trials.views.active_trials import show_active_trials


def router_show_active_trial_or_test(scope):
	logging.warning("router_show_active_trial_or_test")
	page = scope.display['page']

	match page:
		case 'screener':show_active_trials(scope)
		case 'chart':logging.critical("yet to build an active charts render - TODO")

