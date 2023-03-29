# Determine an overall test result for a particular ticker
# - more than one test may be run
# - the assumption is that every test must pass to obtain
#   an overall pass


def determine_overall_ticker_verdict(scope, ticker):

	app = scope.apps['display_app']

	if app == 'screener':
		if scope.tickers[ticker][app]['replace_verdict']:
		# determine an overall verdict for this ticker
			final_verdict = 'pass'
			# Determine a verdict/test result for this ticker
			# - but only assess currently active trials 
			# - a trial may have since been turned off
			for trial in scope.trial_config['active_list']:
				if scope.tickers[ticker][app]['trials'][trial] not in [ 'pass', None ]:
					final_verdict = 'fail'
					break
			scope.tickers[ticker][app]['verdict'] = final_verdict
			# reset request so this does not re-run unncessarily
			scope.tickers[ticker][app]['replace_verdict'] = False
