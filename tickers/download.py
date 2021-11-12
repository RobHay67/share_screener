import yfinance as yf					# https://github.com/ranaroussi/yfinance
import pandas as pd


import streamlit as st


from index.file import save_index

from web.results import render_results

from tickers.file import save_tickers


# ==============================================================================================================================================================
# Download Controller : Donwload Ticker Data from y_finance
# ==============================================================================================================================================================
def load_and_download_ticker_data( scope ):
	print ( '\033[91m' + 'Loading before downloading has been turned off - confirm this is what we want' + '\033[0m' )
	st.markdown("""---""")

	# load_ticker_data_files(scope, ticker_list)				# TODO playing with not doing this - make it the users responsibility
	download_from_yahoo_finance(scope )
	combine_downloaded_with_any_loaded_ticker_data(scope)
	# check_share_data_for_missing_dates( scope )				# TODO Not Sure this is Required anymore

	scope.download_industries = [] 								# Reset for next download




# ==============================================================================================================================================================
# Yahoo Finance - current source of OHLCV Share Data
# ==============================================================================================================================================================
def download_from_yahoo_finance( scope ): 													# TODO What Output to Render
	# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
	# threads : use threads for mass downloading? (True/False/Integer)
	# st.subheader('Downloading Ticker data from Yahoo Finance (as specified by the Ticker List')
	
	st.markdown('##### Downloading Ticker data from Yahoo Finance')
	
	period = str(st.download_days) + 'd' # 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

	reset_download_status(scope)

	for count, industry in enumerate(scope.download_industries):
		download_message = ('downloading > ' + industry + ' ( ' + str(count+1) + ' of ' + str(len(scope.download_industries)) + ' )' )
		st.write(  download_message)
		# print ( download_message)

		download_ticker_string = generate_ticker_string_by_industry(scope, industry)

		if download_ticker_string.count(' ') == 0:
			download_schema = 'y_finance_single'
			yf_download = yf.download( download_ticker_string, period=period , interval='1d', progress=True, show_errors=False )
			yf_download['Ticker'] = download_ticker_string   			# manually add the ticker column as its missing
		else:
			download_schema = 'y_finance_multi'
			scope.download_schema = 'y_finance_multi'	# we are downloading multiple tickers
			yf_download = yf.download( download_ticker_string, group_by = 'ticker', period=period , interval='1d', progress=True, threads=True, show_errors=False )
			yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
		yf_download = format_columns_in_downloaded_share_data( scope, yf_download, download_schema )	
		store_yf_download_in_scope( scope, download_ticker_string, yf_download, yf.shared._ERRORS )
	update_download_status(scope)


# ==============================================================================================================================================================
# Update Share Index with download status information
# ==============================================================================================================================================================
def reset_download_status(scope): # TODO - test output
	for ticker in scope.ticker_list:
		scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'set_for_download'

def update_download_status(scope): # TODO DONE - but needs robust testing on a large group - also > # TODO What Output to Render
	for ticker in scope.downloaded_yf_ticker_data['ticker'].unique():
		scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'downloaded'
	for ticker, error_message in scope.downloaded_yf_anomolies.items():
		if error_message == 'No data found, symbol may be delisted':
			scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'delisted'
		else:
			st.write( ticker + ' - download error = ' + str(error_message))
	save_index(scope)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def generate_ticker_string_by_industry(scope, industry): # DONE
	if industry == 'random_tickers': 							# we have selected specific tickers 
		batch_of_tickers = scope.ticker_list
	else: 														# user has selected a share market, industry or multiple industries
		industry_tickers = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
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

	for col_no in scope.download_schemas[download_schema]:
		provider_column_name    = scope.download_schemas[download_schema][col_no]['col_name']
		if col_no < 50:                 	# its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = scope.share_data_schema[col_no]['col_name']
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           	# its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
	return( yf_download )

def store_yf_download_in_scope( scope, download_ticker_string, yf_download, download_errors ): # TODO What Output to Render
	# store the downloaded data in a single dictionary
	scope.downloaded_yf_ticker_data = pd.DataFrame(columns=scope.share_data_usecols + ['ticker'] )		# Reset for each download
	scope.downloaded_yf_anomolies 	=  {}																# Reset for each download

	scope.downloaded_yf_ticker_data = pd.concat([scope.downloaded_yf_ticker_data, yf_download], sort=False)
	scope.downloaded_yf_anomolies.update(download_errors)	# store any errors
	render_results( scope, passed='Downloaded these Shares > ', passed_2='na', failed='Falied to Download > ' )
	failed_download_list = []
	for ticker, error in download_errors.items():
		failed_download_list.append(ticker)

	ticker_list = download_ticker_string.split(' ')
	
	for ticker in ticker_list:
		if ticker not in failed_download_list:
			render_results( scope, ticker, result='passed' )
		else:
			render_results( scope, ticker, result='failed' )
	render_results(scope, 'Finished', final_print=True )




# ==============================================================================================================================================================
# Combiner - concatenates any downloaded data with any loaded data resulting in a complete (hopefully) temporal history of existing share data
# ==============================================================================================================================================================
def combine_downloaded_with_any_loaded_ticker_data(scope): # WIP - change to check for loaded ticker
	# st.subheader('Combining the Loaded and Downloaded Share Data Files')
	st.markdown('##### Combine download with previously Loaded ticker data')
	render_results( scope, passed='COMBINED > ', passed_2='CREATED new files > ', failed='na' )

	for ticker in scope.ticker_list:																		# iterate through the target tickers
		if ticker in scope.downloaded_yf_ticker_data['ticker'].unique():										# if we have downloaded data (we may have nothing)
			ticker_data = scope.downloaded_yf_ticker_data[scope.downloaded_yf_ticker_data['ticker'] == ticker]	# subset to a specific ticker in the downloaded data
			ticker_data = ticker_data[scope.share_data_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]											# drop rows where volume is zero 
			if ticker in scope.downloaded_loaded_list:														# we have an exisiting share_data_file so we concatenate the data
				scope.share_data_files[ticker] = pd.concat([scope.share_data_files[ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
				render_results( scope, ticker, result='passed' )
			else:
				scope.share_data_files[ticker] = ticker_data												# its brand new - so we can just add it to the dictionary
				render_results( scope, ticker, result='passed_2' )
			scope.share_data_files[ticker].sort_values(by=['date'], inplace=True, ascending=False)			# sort the share data into date order ascending
	render_results(scope, 'Finished', final_print=True )
	save_tickers( scope )


