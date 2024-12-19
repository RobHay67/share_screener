import streamlit as st
import yfinance as yf					# https://github.com/ranaroussi/yfinance
										# https://ranaroussi.github.io/yfinance/index.html



def multiple_tickers_downloader(scope):
	yf_download = yf.download( 
								tickers=scope.yf['batch_ticker_string'], 
								group_by = 'ticker', 				# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
								period=scope.pages['download_days'], 
								interval='1d', 
								progress=True, 
								threads=True, 						# threads : use threads for mass downloading? (True/False/Integer)
								# show_errors=False 
								)

	# Sort out the column headers
	yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)

	# Store the results
	scope.yf['batch_data'] = yf_download
	scope.yf['batch_errors'] = yf.shared._ERRORS