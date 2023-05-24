import yfinance as yf					# https://github.com/ranaroussi/yfinance



def download_ticker_data(scope):

	# empty the temporary download data holder
	scope.yf['batch_data'] = {}
	scope.yf['batch_errors'] = {}
	downloaded_data = False

	print(scope.yf['period'])

	if scope.yf['batch_type'] == 'single_ticker':
		# Single Ticker being downloaded
	
		yf_download = yf.download( 
									tickers=scope.yf['batch_ticker_string'], 
									period=scope.yf['period'], 
									interval='1d', 
									progress=True, 
									show_errors=False
									)			
		# manually add the ticker column as its missing
		yf_download['Ticker'] = scope.yf['batch_ticker_string']

		# print(yf_download)
		downloaded_data = True

	if scope.yf['batch_type'] == 'multiple_tickers':
		# Multiple Tickers being downloaded
			
		yf_download = yf.download( 
									tickers=scope.yf['batch_ticker_string'], 
									group_by = 'ticker', 				# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
									period=scope.yf['period'], 
									interval='1d', 
									progress=True, 
									threads=True, 						# threads : use threads for mass downloading? (True/False/Integer)
									show_errors=False 
									)
		# Sort out the column headers
		yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

		downloaded_data = True

	# Cache the downloaded data for the next process
	if downloaded_data:
		scope.yf['batch_data'] = yf_download
		scope.yf['batch_errors'] = yf.shared._ERRORS
