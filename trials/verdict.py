

def trial_verdict(scope, ticker):
	
	final_verdict = 'pass'

	# Determine a verdict/test result for this ticker
	# - but only assess currently active trials 
	# - a trial may have since been turned off
	for trial in scope.trial_config['active_list']:
		if scope.tickers[ticker]['trials'][trial] not in [ 'pass', None ]:
			final_verdict = 'fail'
			break
	scope.tickers[ticker]['trials']['verdict'] = final_verdict
