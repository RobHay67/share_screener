

def passing_verdict_list(scope):
	# Generate a list of tickers with an overall passing result
	page = scope.display['page']
	verdict_list = []

	for ticker in scope.page[page]['selected_tickers']:
		# Only mined tickers can have verdicts
		if ticker in scope.page[page]['loaded_ticker_list']:
			if scope.tickers[ticker][page]['verdicts']['overall_verdict'] == 'pass':
				verdict_list.append(ticker)

	return verdict_list
