import yfinance as yf					# https://github.com/ranaroussi/yfinance
import pandas as pd


from tickers.schema import ticker_file_schema
from tickers.schema import ticker_file_usecols
from tickers.schema import y_finance_schemas

from partials.messages.y_finance import download_industry_message

from progress.cache import cache_progress

from ticker_index.save import save_index			# TODO we may need to get this working again


# ==============================================================================================================================================================
#
# Yahoo Finance 
#
# ==============================================================================================================================================================







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



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update Share Index with download status information
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def reset_download_status(scope): # TODO - ERROR - which tickers are being updated????
	# app = scope.apps['display_app']

	# ticker_list = list(scope.selected[app]['selected_tickers'])
	# for ticker in ticker_list:
	# 	scope.ticker_index.at[ticker, 'yahoo_status'] = 'set_for_download'

# def update_download_status(scope): # TODO DONE - but needs robust testing on a large group - also > # TODO What Output to Render
	# for ticker in scope.download['yf_files']['ticker'].unique():
	# 	scope.ticker_index.at[ticker, 'yahoo_status'] = 'downloaded'
	# for ticker, error_message in scope.download['yf_anomolies'].items():
	# 	if error_message == 'No data found, symbol may be delisted':
	# 		scope.ticker_index.at[ticker, 'yahoo_status'] = 'delisted'
	# 	else:
	# 		st.write( ticker + ' - download error = ' + str(error_message))
	# save_index(scope)



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_download_message(scope, count, industry):
	app = scope.apps['display_app']

	if industry == 'random_tickers':
		download_message = ('Yahoo Finance downloading > ' + scope.apps[app]['selected_tickers'][0] )
	else:
		download_message = ('Yahoo Finance downloading > ' + industry + ' ( ' + str(count+1) + ' of ' + str(len(scope.download['industries'])) + ' )' )
	
	download_industry_message(scope, download_message)


def generate_ticker_string_by_industry(scope, industry): # OK

	app = scope.apps['display_app']

	if industry == 'random_tickers': 							# we have selected specific tickers 
		batch_of_tickers = scope.apps[app]['selected_tickers']
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

def format_columns_in_downloaded_share_data( scope, yf_download, download_schema ): # DONE
	
	yf_download.reset_index(inplace=True)   # remove any index set during import - we will set the index later

	for col_no in y_finance_schemas[download_schema]:
		provider_column_name    = y_finance_schemas[download_schema][col_no]['col_name']
		if col_no < 50:                 	# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = ticker_file_schema[col_no]['col_name']
			
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	# its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
	return( yf_download )

def store_yf_download_in_scope( scope, download_ticker_string, yf_download, download_errors ): # TODO What Output to Render
	# store the downloaded data in a single dictionary
	scope.download['yf_files'] = pd.DataFrame(columns=ticker_file_usecols + ['ticker'] )		# Reset for each download
	scope.download['yf_anomolies'] 	=  {}																# Reset for each download

	scope.download['yf_files'] = pd.concat([scope.download['yf_files'], yf_download], sort=False)
	scope.download['yf_anomolies'].update(download_errors)	# store any errors
	
	cache_progress( 	scope, 
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




