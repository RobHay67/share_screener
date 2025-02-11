import logging
from trials.views.active_trials import show_active_trials
from charts.active_charts import show_active_charts


def router_show_active_trial_or_test(scope):
	logging.warning("router_show_active_trial_or_test")
	page = scope.display['page']

	match page:
		case 'screener':
			show_active_trials(scope)
		case 'chart':
			show_active_charts(scope)
