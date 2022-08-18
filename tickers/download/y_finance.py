import yfinance as yf					# https://github.com/ranaroussi/yfinance

from tickers.download.format_cols import format_yf_download
from tickers.download.cache import cache_yf_downloaded_data
from partials.messages.y_finance import render_download_message


def download_from_yahoo_finance(scope): 
	# download ticker data for a single or group of tickers

	# valid periods = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
	period = str(int(scope.download['days'])) + 'd' 

	for batch_no, industry in enumerate(scope.download['yf_industry_groups']):

		yf_ticker_string(scope, industry)

		render_download_message(scope, batch_no, industry)		

		if scope.download['yf_ticker_string'].count(' ') == 0:
			
			# Single Ticker being downloaded
			scope.download['yf_schema'] = 'single_ticker'
			yf_download = yf.download( 
										scope.download['yf_ticker_string'], 
										period=period, 
										interval='1d', 
										progress=True, 
										show_errors=False
										)			
			# manually add the ticker column as its missing
			yf_download['Ticker'] = scope.download['yf_ticker_string']
		
		else:
			
			# Multiple Tickers being downloaded
			scope.download['yf_schema'] = 'multiple_tickers'
			yf_download = yf.download( 
										scope.download['yf_ticker_string'], 
										group_by = 'ticker', 				# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
										period=period, 
										interval='1d', 
										progress=True, 
										threads=True, 						# threads : use threads for mass downloading? (True/False/Integer)
										show_errors=False 
										)
			# Sort out the column headers
			yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
		
		yf_download = format_yf_download( scope, yf_download )	
		cache_yf_downloaded_data( scope, yf_download, yf.shared._ERRORS )




def yf_ticker_string(scope, industry):
	# convert an industry into a string of tickers acceptable to y_finance
	
	if industry == 'random_tickers':
		# Selected specific tickers rather than by industry group					 
		app = scope.apps['display_app']
		list_of_tickers = scope.apps[app]['worklist']
	else:
		# selected a share market, industry or multiple industries
		industry_tickers = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
		list_of_tickers = industry_tickers.index.tolist()

	# Create a readable list of the tickers for Y_Finance
	y_finance_ticker_string = ""
	for ticker in list_of_tickers:
		if len(y_finance_ticker_string) != 0:
			y_finance_ticker_string += " "
		y_finance_ticker_string =  y_finance_ticker_string + ticker

	scope.download['yf_ticker_string'] = y_finance_ticker_string






