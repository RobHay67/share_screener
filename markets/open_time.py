
from markets.schema import opening_hours






def open_time( scope, ticker):
	market = scope.pages['share_market']
	ticker_code_first_letter = ticker[0].upper()
	for group in opening_hours[market].keys():
		
		if group not in ['timezone', 'market_open', 'market_close' ]:
			if ticker_code_first_letter in opening_hours[market][group]['letter_range']:
				opening_time = opening_hours[market][group]['opening_time']
	return( opening_time )