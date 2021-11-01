


import streamlit as st
import pandas as pd
import yfinance as yf					# https://github.com/ranaroussi/yfinance
# import datetime
import os

from share_index import save_share_index_file
from scope import generate_path_for_share_data_file
# from reports import report_progress, terminal_heading, output_result_to_terminal, print_missing_dates
from reports import output_results_to_browser


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Browser Render Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_share_data_page(scope):
	st.title('Load and/or Download Share Data')

	st.success(('Current number of Loaded Files ( ' + str((len(scope.share_data_files))) + ' )'))

	list_of_loaded_tickers = list(scope.share_data_files.keys())
	list_of_loaded_tickers.insert(0, '< select a ticker >')
	
	# ticker_list_message = str(len(scope.ticker_list))

	col1,col2,col3 = st.columns([3,3,3])

	with col1: st.subheader('Reports')
	with col1: show_tickers = st.button( ('Show Ticker List ( ' + str((len(scope.ticker_list))) + ' )') )
	with col1: show_ticker = st.selectbox('Show Share Data'  , list_of_loaded_tickers, help='Select a Ticker and I will show you all the data we have for it')

	with col2: st.subheader('Load Share Data Files')
	with col2: st.subheader('(per ticker list)')
	with col2: st.write(('number of Files to Load = ( ' + str((len(scope.ticker_list))) + ' )'))
	with col2: load_tickers = st.button('Load OHLC Data')

	with col3: st.subheader('Download Latest Share Data')
	with col3: st.subheader('(per ticker list)')
	with col3: st.download_days = st.number_input('change ( - / + )  number of days to download', min_value=1, max_value=10, value=1, key='0')    
	with col3: download_tickers = st.button('Download OHLC Data')
	

	st.markdown("""---""")

	if show_ticker != '< select a ticker >':
		st.header( show_ticker ) 
		st.write('loaded and downloaded share data.')
		
		st.dataframe(scope.share_data_files[show_ticker], 2000, 1200)


	if show_tickers:
		st.header('Ticker List - target tickers for analysis (use sidebar to add tickers to this list)')
		ticker_list_message = ''
		for ticker in scope.ticker_list:
			ticker_list_message = ticker_list_message + ticker + ' - '
		st.success(ticker_list_message)

	if load_tickers:
		st.header('Loading Tickers (as specified by the Ticker List)')

		if len(scope.ticker_list) != 0: 
			load_share_data_files(scope)
		else:
			st.error('Ticker List does not contain any tickers - add tickers using the sidebar')

	if download_tickers:
		st.header('Downloading Tickers from Yahoo Finance (as specified by the Ticker List)')

		if len(scope.ticker_list) != 0: 
			st.subheader('Loading Tickers (as specified by the Ticker List)')
			load_share_data_files(scope)
			# st.markdown("""---""")

			determine_download_groups_for_y_finance(scope)

			download_from_yahoo_finance(scope)

			combine_loaded_and_downloaded_share_data(scope)

			# check_share_data_for_missing_dates( scope )

		else:
			st.error('Ticker List does not contain any tickers - add tickers using the sidebar')


		



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Primary Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def ensure_share_data_is_available(params):
# 	if len(params.analysis['ticker_list']) > 0:								# we have some share data to analyse
# 		# load_share_data_files( params )
# 		download_from_yahoo_finance( params )			
# 		combine_loaded_and_downloaded_share_data(params)
# 		check_share_data_for_missing_dates( params )   # ensure that the expected date ranges are actually available for each stock




# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Primary Controller
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
def combine_loaded_and_downloaded_share_data(scope): # DONE
	st.subheader('Combining the Loaded and Downloaded Share Data Files')
	output_results_to_browser( scope, passed='COMBINED > ', passed_2='CREATED new files > ', failed='na' )

	for ticker in scope.ticker_list:
		if ticker in scope.download_yf_share_data['ticker'].unique():
			ticker_data = scope.download_yf_share_data[scope.download_yf_share_data['ticker'] == ticker]	# subset to specific ticker
			ticker_data = ticker_data[scope.share_data_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]											# drop rows where volume is zero 
			if ticker in scope.share_data_loaded_list:														# we have an exisiting share_data_file so we concatenate the data
				scope.share_data_files[ticker] = pd.concat([scope.share_data_files[ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
				output_results_to_browser( scope, ticker, result='passed' )
			else:
				scope.share_data_files[ticker] = ticker_data												# its brand new - so we can just add it to the dictionary
				output_results_to_browser( scope, ticker, result='passed_2' )
			scope.share_data_files[ticker].sort_values(by=['date'], inplace=True)							# sort the share data into date order ascending
	output_results_to_browser(scope, 'Finished', final_print=True )
	save_share_data_files( scope )

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Share Data File - missing dates
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def check_share_data_for_missing_dates(params):
# 	if params.analysis['check_dates']:
# 		terminal_heading( params, ('Checking for missing dates ' + cyan + 'Completed set' + '  /  ' + purple + 'Missing some' + white ), line_filler='-' )
# 		reset_missing_dates(params)
# 		output_result_to_terminal( params )
# 		for ticker in params.share_data['files']:
# 			share_data_df = params.share_data['files'][ticker][['date']].copy()
# 			share_data_df['date'] = share_data_df['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
# 			available_dates_list = list( (share_data_df['date']))
# 			missing_dates_list = list(set(params.analysis['date_list']) - set(available_dates_list))
			
# 			if len(missing_dates_list) > 0:			
# 				# Adjust missing_dates_list for any prelisting dates ( if the listing_date is between our analysis dates, before they start or after they finish )
# 				listing_date = (params.share_index['file'].loc[ticker]['listing_date'])
# 				if (listing_date > params.analysis['start'] and listing_date < params.analysis['end']) or (listing_date < params.analysis['start']) or (listing_date > params.analysis['end']):
# 					pre_listing_dates = list(pd.date_range(params.analysis['start'], listing_date, freq='B').strftime('%Y-%m-%d'))
# 					missing_dates_list = list(set(missing_dates_list) - set(pre_listing_dates))

# 			if len(missing_dates_list) > 0:
# 				# at the moment we need to manually tag the trading halt dates (after confirmation with the ASX that this is the case) terminal > pipenv run python app.py -th boq
# 				if pd.notna(params.share_index['file'].loc[ticker]['trading_halt_dates']):
# 					trading_halt_dates_list = [ date for date in params.share_index['file'].loc[ticker]['trading_halt_dates'].split()]
# 					missing_dates_list = list(set(missing_dates_list) - set(trading_halt_dates_list))

# 			if len(missing_dates_list) > 0 :
# 				store_missing_dates( params, ticker, missing_dates_list )
# 				output_result_to_terminal( params, ticker, result='failed' )
# 			else:
# 				store_missing_dates( params, ticker, None )
# 				output_result_to_terminal( params, ticker, result='passed' )
# 		output_result_to_terminal(params, (' - dates good for ' + cyan + str(params.terminal['count_passed']) + white + ' and gaps with ' + purple + str(params.terminal['count_failed']) + white), final_print=True )
# 		save_share_index_file(params)
# 		params.analysis['check_dates'] = False			# To prevent this function being run twice
# 		if params.reports['missing_dates']: print_missing_dates(params)

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Share Data File - Loader - local
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
def load_share_data_files( scope ): # DONE
	output_results_to_browser( scope, passed='LOADED Share Data Files > ', failed='MISSING Share Data Files for > ', passed_2='na' )

	scope.share_data_loaded_list = []
	scope.share_data_missing_list = []
	
	for ticker in scope.ticker_list:
		generate_path_for_share_data_file(scope, ticker )
		if os.path.exists( scope.path_share_data_file ):
			load_a_file(scope, ticker )
			scope.share_data_loaded_list.append(ticker)
			output_results_to_browser( scope, ticker, result='passed' )
		else:
			scope.share_data_missing_list.append(ticker)
			output_results_to_browser( scope, ticker, result='failed' )
	output_results_to_browser(scope, 'Finished', final_print=True )

def load_a_file( scope, ticker ): # DONE
	share_data_file = pd.read_csv (  
									scope.path_share_data_file, 
									header      = 0,
									# nrows       = params.row_limitor, 
									usecols     = scope.share_data_usecols,
									# index_col   = 'date', 
									dtype       = scope.share_data_dtypes,
									parse_dates = scope.share_data_dates,
									)
	scope.share_data_files[ticker] = share_data_file

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Share Data File - Saver - local
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
def save_share_data_files( scope ): # DONE
	st.subheader('Saving Share Data Files')
	output_results_to_browser( scope, passed='Files SAVED > ', failed='na', passed_2='na' )
	for ticker in scope.share_data_files:
		generate_path_for_share_data_file(scope, ticker )
		save_share_data_file( scope, scope.share_data_files[ticker] )
		output_results_to_browser( scope, ticker, result='passed' )
	output_results_to_browser(scope, 'Finished', final_print=True )

def save_share_data_file( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_share_data_file, index=False )


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - Source of Share Data
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
# threads: use threads for mass downloading? (True/False/Integer)

def download_from_yahoo_finance( scope ): # DONE
	st.subheader('Downloading Ticker data from Yahoo Finance (as specified by the Ticker List')
	
	period = str(st.download_days) + 'd'

	reset_download_status(scope)
	# print ( 'download_groups_for_y_finance = ', scope.download_groups_for_y_finance )
	for count, y_finance_group in enumerate(scope.download_groups_for_y_finance):
		download_message = ('downloading > ' + y_finance_group + ' ( ' + str(count+1) + ' of ' + str(len(scope.download_groups_for_y_finance)) + ' )' )
		st.write(  download_message)
		print ( download_message)
		ticker_string = yahoo_ticker_string_by_group( scope, y_finance_group)

		if scope.download_schema == 'y_finance_single':
			yf_download = yf.download( ticker_string, period=period , interval='1d', progress=True, show_errors=False )
			yf_download['Ticker'] = ticker_string   								# manually add the ticker column as its missing
			# print (yf_download)
		else:
			yf_download = yf.download( ticker_string, group_by = 'ticker', period=period , interval='1d', progress=True, threads=True, show_errors=False )
			yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
		yf_download = format_columns_in_downloaded_share_data( scope, yf_download )	
		store_yf_download_in_scope( scope, ticker_string, yf_download, yf.shared._ERRORS )
	update_download_status(scope)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def determine_download_groups_for_y_finance(scope): # DONE
	scope.download_groups_for_y_finance = []

	if scope.selected_market != '< select entire market >':
		scope.download_groups_for_y_finance = ( list(scope.share_index_file['industry_group'].unique() ))
	elif len(scope.selected_industry) != 0:
		scope.download_groups_for_y_finance = scope.selected_industry
	elif len(scope.selected_tickers) != 0:
		scope.download_groups_for_y_finance.append('selected_tickers')

def yahoo_ticker_string_by_group( scope, y_finance_group): # DONE
	if y_finance_group == 'selected_tickers':
		# we have selected specific tickers 
		tickers_list = scope.selected_tickers
	else:
		# we have selected a specific market, industry or number of industries
		tickers_in_industry_group_df = scope.share_index_file[scope.share_index_file['industry_group'] == y_finance_group ]
		tickers_list = tickers_in_industry_group_df.index.tolist()
	
	 # store the appropriate type of download for y_finance
	if len(tickers_list) == 1: 
		scope.download_schema = 'y_finance_single'  # we are only downloading a single ticker
	else:
		scope.download_schema = 'y_finance_multi'	# we are downloading multiple tickers

	# Build the Ticker String for Yahoo Finance
	ticker_string = ""
	for ticker in tickers_list:
		if len(ticker_string) != 0:
			ticker_string = ticker_string + " "
		ticker_string =  ticker_string + ticker
	return ticker_string

def format_columns_in_downloaded_share_data( scope, yf_download ): # DONE
	yf_download.reset_index(inplace=True)   # remove any index set during import - we will set the index later

	for col_no in scope.download_schemas[scope.download_schema]:
		provider_column_name    = scope.download_schemas[scope.download_schema][col_no]['col_name']
		if col_no < 50:                 # its a column we are keeping - anything tagged with a key above 50 can be removed
			application_column_name = scope.share_data_schema[col_no]['col_name']
			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
		else:                           # its a column we do not need so lets delete it
			del yf_download[provider_column_name]
	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
	return( yf_download )

def store_yf_download_in_scope( scope, ticker_string, yf_download, download_errors ): # DONE
	# store the downloaded data in a single dictionary
	scope.download_yf_share_data = pd.concat([scope.download_yf_share_data, yf_download], sort=False)
	scope.download_yf_anomolies.update(download_errors)	# store any errors
	output_results_to_browser( scope, passed='Downloaded these Shares > ', passed_2='na', failed='Falied to Download > ' )
	failed_download_list = []
	for ticker, error in download_errors.items():
		failed_download_list.append(ticker)

	ticker_list = ticker_string.split(' ')
	
	for ticker in ticker_list:
		if ticker not in failed_download_list:
			output_results_to_browser( scope, ticker, result='passed' )
		else:
			output_results_to_browser( scope, ticker, result='failed' )
	output_results_to_browser(scope, 'Finished', final_print=True )
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Update Share Index with yahoo download information
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
def reset_download_status( scope ): # DONE
	for ticker in scope.ticker_list:
		scope.share_index_file.at[ticker, 'yahoo_status'] = 'set_for_download'

def update_download_status(scope): # DONE - but needs robust testing on a large group
	for ticker in scope.download_yf_share_data['ticker'].unique():
		scope.share_index_file.at[ticker, 'yahoo_status'] = 'downloaded'
	for ticker, error_message in scope.download_yf_anomolies.items():
		if error_message == 'No data found, symbol may be delisted':
			scope.share_index_file.at[ticker, 'yahoo_status'] = 'delisted'
		else:
			st.write( ticker + ' - download error = ' + str(error_message))
	save_share_index_file(scope)

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Update Share Index with any missing dates
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def reset_missing_dates(params):
# 	for ticker in params.share_data['files']:
# 		params.share_index['file'].at[ticker, 'missing_dates'] = 'checking_dates'

# def store_missing_dates( params, ticker, missing_dates_list ):
# 	if missing_dates_list != None:
# 		missing_dates_list.sort(key = lambda date: datetime.datetime.strptime(date, "%Y-%m-%d" ))
# 		missing_dates_string = ' '.join(missing_dates_list)
# 	else:
# 		missing_dates_string = None

# 	params.share_index['file'].at[ticker, 'missing_dates'] = missing_dates_string
# # -----------------------------------------------------------------------------------------------------------------------------------
# # Update Share Index with any Trading Halt Days
# # -----------------------------------------------------------------------------------------------------------------------------------
# def update_trading_halt_days(params):
# 	if params.share_index['specified_trading_halt_codes'] != None:  # just make sure we have specified some codes
# 		terminal_heading( params, ( 'editing share index to account for trading halt days' + cyan + '   Changed' + '  /  ' + purple + 'Failed' + white ), line_filler='-' )
# 		output_result_to_terminal(params)
# 		for ticker in params.analysis['ticker_list']:
# 			missing_dates_string = str(params.share_index['file'].loc[ticker]['missing_dates'])
# 			trading_halt_dates_string = str(params.share_index['file'].loc[ticker]['trading_halt_dates'])

# 			if missing_dates_string != 'nan' or missing_dates_string != None: # make sure we actually have some missing dates
# 				if trading_halt_dates_string == 'nan' or trading_halt_dates_string == None:
# 					# we have nothing so a simple copy will suffice
# 					params.share_index['file'].at[ticker, 'trading_halt_dates'] = missing_dates_string 
# 				else:
# 					# we had some trading halt days previously so we need to add them together
# 					params.share_index['file'].at[ticker, 'trading_halt_dates'] = trading_halt_dates_string + ' ' + missing_dates_string 
# 			params.share_index['file'].at[ticker, 'missing_dates'] = None  # as they are no longer missing - we have them accounted for in the trading_halt_days
# 			output_result_to_terminal( params, ticker, result='passed' )
# 		print ('')
# 		save_share_index_file(params)
# 	# rerun the date checker to make sure the result is what we wanted
# 	params.analysis['check_dates'] = True
# 	check_share_data_for_missing_dates(params)


# # -----------------------------------------------------------------------------------------------------------------------------------
# # Colours
# # -----------------------------------------------------------------------------------------------------------------------------------

# red         = '\033[91m'
# green       = '\033[92m'
# yellow      = '\033[93m'
# blue        = '\033[94m'
# purple      = '\033[95m'
# cyan        = '\033[96m'
# white 		= '\033[0m'