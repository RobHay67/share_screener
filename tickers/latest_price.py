import pandas as pd


def latest_ticker_price(scope, ticker):
    
	price_df =  pd.DataFrame(columns=['Date','Open','High','Low','Close','Volume' ])

	# Check that we have OHLCV data for this ticker
	if ticker in list(scope.tickers.keys()): 
		ticker_df = scope.tickers[ticker]['df']
		
		decimal_places=3
		currency_format = "$ {:." + str(decimal_places) + "f}"				

		# Key Values
		max_date = ticker_df['date'].max()
		max_date = str(max_date.strftime("%d-%b-%Y"))
		open  = round((ticker_df['open'].values[0]),decimal_places)
		high  = round((ticker_df['high'].values[0]),decimal_places)
		low   = round((ticker_df['low'].values[0]),decimal_places)
		close = round((ticker_df['close'].values[0]),decimal_places)
		volume= format((ticker_df['volume'].values[0]), ',d')

		# format for cleaner output
		open = currency_format.format(open)
		high = currency_format.format(high)
		low = currency_format.format(low)
		close = currency_format.format(close)

		ohlcv_df = pd.DataFrame([{'Date':max_date, 'Open':open, 'High':high, 'Low':low, 'Close':close, 'Volume':volume}])
		price_df = pd.concat([price_df, ohlcv_df], axis=0, ignore_index=True)
		
		price_df = price_df.set_index('Date')


	return price_df