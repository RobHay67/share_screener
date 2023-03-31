from markets.schema import opening_hours



def trading_minutes( scope, ticker ):
	market = scope.config['share_market']
	ticker_code_first_letter = ticker[0].upper()
	for group in opening_hours[market].keys():
		if group not in ['timezone', 'market_open', 'market_close' ]:
			if ticker_code_first_letter in opening_hours[market][group]['letter_range']:
				trading_minutes_per_day = opening_hours[market][group]['minutes_per_day']
	return trading_minutes_per_day 