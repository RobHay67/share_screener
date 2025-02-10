import logging


def open_time( scope, ticker):
	logging.warning("open_time")
	market = scope.config['share_market']
	opening_hours = scope.config['opening_hours']
	ticker_code_first_letter = ticker[0].upper()
	for group in opening_hours[market].keys():
		
		if group not in ['timezone', 'market_open', 'market_close' ]:
			if ticker_code_first_letter in opening_hours[market][group]['letter_range']:
				opening_time = opening_hours[market][group]['opening_time']
	return( opening_time )