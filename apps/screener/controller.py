from apps.app_header.controller import render_app_header		
from apps.screener.verdicts import render_trial_verdicts


def render_screener_page(scope):

	app = scope.apps['display_app']

	render_app_header(scope, 'Ticker Screener')

	render_trial_verdicts(scope)
