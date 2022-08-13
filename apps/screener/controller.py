from partials.ticker_loader.header import render_page_title		
from partials.ticker_loader.controller import render_ticker_loader
from apps.screener.results import render_trial_results
from apps.screener.trials import render_available_trials

from partials.ticker_search.search_results import render_search_results

from apps.screener.screener_example import example_settings			#TODO fleshing out some ideas - delete when happy


def render_screener_page(scope):

	render_page_title(scope, 'Ticker Screener')

	render_ticker_loader(scope)
	
	if len(scope.apps['screener']['search_results']) == 0:

		render_trial_results(scope)

		render_available_trials(scope)

		example_settings(scope)
	
	else:

		render_search_results(scope)

	# TODO we want to be able to jumpt to single stock analysis from any list - that migth be cool!!!
