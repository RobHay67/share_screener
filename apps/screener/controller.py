from partials.app_header.controller import render_app_header		
from apps.screener.verdicts import render_trial_verdicts

from partials.search_results import render_search_results



def render_screener_page(scope):

	app = scope.apps['display_app']

	render_app_header(scope, 'Ticker Screener')

	if len(scope.apps[app]['search_results']) == 0:

		render_trial_verdicts(scope)
	else:

		render_search_results(scope)