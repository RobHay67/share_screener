from partials.app_header.controller import render_app_header		
from apps.screener.verdicts import render_trial_verdicts
from apps.screener.trials import render_available_trials

from partials.ticker_search.search_results import render_search_results

from apps.screener.example import example_settings			#TODO fleshing out some ideas - delete when happy



def render_screener_page(scope):

	app = scope.apps['display_app']

	render_app_header(scope, 'Ticker Screener')

	if len(scope.apps[app]['search_results']) == 0:

		render_trial_verdicts(scope)

		render_available_trials(scope)

		example_settings(scope)
	
	else:

		render_search_results(scope)