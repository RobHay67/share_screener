

def trial_verdict(scope, ticker):
	final_verdict = 'pass'
	for trial in scope.trial_config['trial_list']:
		if scope.tickers[ticker]['trials'][trial] not in [ 'pass', None ]:
			final_verdict = 'fail'
	scope.tickers[ticker]['trials']['verdict'] = final_verdict
