import yfinance as yf					# https://github.com/ranaroussi/yfinance
import pandas as pd


from tickers.schema import ticker_file_schema
from tickers.schema import ticker_file_usecols
from tickers.schema import y_finance_schemas

from partials.messages.y_finance import download_industry_message

from progress.cache import cache_progress

from ticker_index.save import save_index			# TODO we may need to get this working again


from partials.messages.y_finance import render_download_message
from tickers.download.format_cols import format_columns_in_downloaded_share_data





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# download ticker data for a single or group of tickers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def download_from_yahoo_finance(scope): 													# TODO What Output to Render
	# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
	# threads : use threads for mass downloading? (True/False/Integer)

	# valid periods = 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
	period = str(int(scope.download['days'])) + 'd' 

	# reset_download_status(scope)

	# TODO scope.download['industries'] - this variable needs to be better defined and explained
	# industry_groups_to_download = scope.download['industries'] - something like this anyway TODO

	for count, industry in enumerate(scope.download['industries']):
		render_download_message(scope, count, industry)

		download_ticker_string = generate_ticker_string_by_industry(scope, industry)

		if download_ticker_string.count(' ') == 0:
			download_schema = 'y_finance_single'
			yf_download = yf.download( download_ticker_string, period=period , interval='1d', progress=True, show_errors=False )
			yf_download['Ticker'] = download_ticker_string   			# manually add the ticker column as its missing
		else:
			download_schema = 'y_finance_multi'			# TODO - is this being decalared twice, once in scope and once outside - why?
			scope.download_schema = 'y_finance_multi'	# we are downloading multiple tickers
			yf_download = yf.download( download_ticker_string, group_by = 'ticker', period=period , interval='1d', progress=True, threads=True, show_errors=False )
			yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
		yf_download = format_columns_in_downloaded_share_data( scope, yf_download, download_schema )	
		store_yf_download_in_scope( scope, download_ticker_string, yf_download, yf.shared._ERRORS )
	# update_download_status(scope)






def generate_ticker_string_by_industry(scope, industry): # OK

	app = scope.apps['display_app']

	if industry == 'random_tickers': 							# we have selected specific tickers 
		batch_of_tickers = scope.apps[app]['worklist']
	else: 														# user has selected a share market, industry or multiple industries
		industry_tickers = scope.ticker_index[scope.ticker_index['industry_group'] == industry ]
		batch_of_tickers = industry_tickers.index.tolist()

	# Create a readable list of the tickers for Y_Finance
	download_ticker_string = ""
	for ticker in batch_of_tickers:
		if len(download_ticker_string) != 0:
			download_ticker_string += " "
		download_ticker_string =  download_ticker_string + ticker

	return download_ticker_string




def store_yf_download_in_scope( scope, download_ticker_string, yf_download, download_errors ): # TODO What Output to Render
	# store the downloaded data in a single dictionary
	scope.download['yf_files'] = pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		# Reset for each download
	scope.download['yf_anomolies'] 	=  {}																# Reset for each download

	scope.download['yf_files'] = pd.concat([scope.download['yf_files'], yf_download], sort=False)
	scope.download['yf_anomolies'].update(download_errors)	# store any errors
	
	cache_progress( scope, 
					passed='Downloaded > ', 
					passed_2='na', 
					failed='Falied to Download > ' 
					)
	
	failed_download_list = []
	for ticker, error in download_errors.items():
		failed_download_list.append(ticker)

	ticker_list = download_ticker_string.split(' ')
	
	for ticker in ticker_list:
		if ticker not in failed_download_list:
			cache_progress( scope, ticker, result='passed' )
		else:
			cache_progress( scope, ticker, result='failed' )
	cache_progress(scope, 'Finished', final_print=True )



