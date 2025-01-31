import logging
import yfinance as yf					# https://github.com/ranaroussi/yfinance
										# https://ranaroussi.github.io/yfinance/index.html


def single_ticker_downloader(scope):
	logging.debug("single_ticker_downloader")
	yf_download = yf.download( 
					tickers=scope.yf['batch_ticker_string'], 
					period=scope.config['download_days'], 
					interval='1d', 
					progress=True, 
					)			
		
	# Sort out the column headers
	yf_download.columns = yf_download.columns.droplevel(1)

	# manually add the ticker column as its missing
	yf_download['Ticker'] = scope.yf['batch_ticker_string']

	# Store the results
	scope.yf['batch_data'] = yf_download
	scope.yf['batch_errors'] = yf.shared._ERRORS