# Determine an overall test result for a particular ticker
# - more than one test may be run
# - the assumption is that every test must pass to obtain
#   an overall pass


def determine_verdict_for_ticker(scope, ticker):

	page = scope.pages['display']
	
	if page == 'screener':
		# determine an overall verdict for this ticker
		if scope.tickers[ticker][page]['replace_verdict']:
	
			final_verdict = 'pass'
			# Determine a verdict/test result for this ticker
			# - but only assess currently active trials 
			# - a trial may have since been turned off
			for trial in scope.trials['active_list']:
				if scope.tickers[ticker][page]['trials'][trial] not in [ 'pass', None ]:
					final_verdict = 'fail'
					break
			scope.tickers[ticker][page]['verdict'] = final_verdict
			# reset request so this does not re-run unncessarily
			scope.tickers[ticker][page]['replace_verdict'] = False


	# so i 2 RSI test running
	# 1 pass and 1 fail
	# i turned off the fail but .......
	# these overall test did not rerun
	# we need to trigger a rerun by setting
	# scope.tickers[ticker][page]['replace_verdict'] == true
