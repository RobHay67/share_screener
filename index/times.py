


def open_time( scope, ticker):
	market = scope.share_market
	ticker_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if ticker_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				opening_time = scope.market_opening_hours[market][group]['opening_time']
	return( opening_time )

def trading_minutes( scope, ticker ):
	market = scope.share_market
	ticker_code_first_letter = ticker[0].upper()
	for group in scope.market_opening_hours[market].keys():
		if group != 'timezone':
			if ticker_code_first_letter in scope.market_opening_hours[market][group]['letter_range']:
				trading_minutes_per_day = scope.market_opening_hours[market][group]['minutes_per_day']
	return trading_minutes_per_day 





