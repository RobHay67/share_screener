


import streamlit as st
import pandas as pd
import yfinance as yf					# https://github.com/ranaroussi/yfinance
# import datetime
import os

from ticker_index import save_ticker_index_file
from scope import generate_path_for_share_data_file
# from reports import report_progress, terminal_heading, output_result_to_terminal, print_missing_dates
from web_results import render_results

# ==============================================================================================================================================================
# Browser Render Controller : Load and / or  Download share data
# ==============================================================================================================================================================
def render_ticker_data_fetcher(scope, ticker_list):

	if isinstance(ticker_list, str): ticker_list = [ticker_list]

	st.header('Load and/or Download Share Data')
	col1,col2,col3 = st.columns([2,3,7])
	with col1: load_tickers = st.button('Load Share Data File')
	with col2: download_tickers = st.button( ( 'Download Previous ' + str(int(st.download_days)) + ' days') )

	if len(ticker_list) > 0:
		if load_tickers: 
			with col3: st.write( ('Loading ( ' + str(len(ticker_list)) + ' ) Tickers') )
			load_ticker_data_files(scope, ticker_list)
			with col3: st.write('Finished Loading Tickers')
			

		if download_tickers:
			with col3: st.write( ('Downloading ( ' + str(len(ticker_list)) + ' ) Tickers from Yahoo Finance') )

			load_ticker_data_files(scope, ticker_list)

			#TODO - ROB WE ARE up to this point - for some reason it was downloading the entire ASX - need to check this
			determine_download_groups_for_y_finance(scope)

			download_from_yahoo_finance(scope)

			combine_loaded_and_downloaded_ticker_data(scope)

			# check_share_data_for_missing_dates( scope )

			st.write('Finished Downloading Ticker Trading Data')
		
		
	else:
		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')



def download_tickers(scope):
	st.header('Downloading Tickers from Yahoo Finance (as specified by the Ticker List)')

	if len(scope.tickers_for_multi) != 0: 
		st.subheader('Loading Tickers (as specified by the Ticker List)')

		load_ticker_data_files(scope)

		determine_download_groups_for_y_finance(scope)

		download_from_yahoo_finance(scope)

		combine_loaded_and_downloaded_ticker_data(scope)

		# check_share_data_for_missing_dates( scope )

	else:
		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
	
	st.write('Finished Downloading Ticker Trading Data')




def render_ticker_data_page(scope):
	st.title('Load and/or Download Share Data')
	st.info(('Current number of Loaded Files ( ' + str((len(scope.share_data_files))) + ' )'))

	render_ticker_data_fetcher(scope, ['test'])


	# col1,col2 = st.columns([4,4])

	# with col1: st.subheader('Load Share Data Files')
	# with col1: st.subheader('(per ticker list)')
	# with col1: st.write(('number of Files to Load = ( ' + str((len(scope.tickers_for_multi))) + ' )'))
	# with col1: load_tickers = st.button('Load OHLCV Data')

	# with col2: st.subheader('Download Latest Share Data')
	# with col2: st.subheader('(per ticker list)')
	# with col2: st.download_days = st.number_input('change ( - / + )  number of days to download', min_value=1, max_value=1000, value=1, key='0')    
	# with col2: download_tickers = st.button('Download OHLCV Data')

	
	# st.markdown("""---""")

	# if load_tickers:
	# 	st.header('Loading Tickers (as specified by the Ticker List)')

	# 	if len(scope.tickers_for_multi) != 0: 
	# 		load_ticker_data_files(scope)
	# 	else:
	# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
		
	# 	st.write('Finished Loading Tickers')

	# if download_tickers:
	# 	st.header('Downloading Tickers from Yahoo Finance (as specified by the Ticker List)')

	# 	if len(scope.tickers_for_multi) != 0: 
	# 		st.subheader('Loading Tickers (as specified by the Ticker List)')

	# 		load_ticker_data_files(scope)

	# 		determine_download_groups_for_y_finance(scope)

	# 		download_from_yahoo_finance(scope)

	# 		combine_loaded_and_downloaded_ticker_data(scope)

	# 		# check_share_data_for_missing_dates( scope )

	# 	else:
	# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
		
	# 	st.write('Finished Downloading Ticker Trading Data')

def render_ticker_data_file(scope):
	st.header('Loaded and Downloaded share data.')
	list_of_loaded_tickers = list(scope.share_data_files.keys())

	for ticker in list_of_loaded_tickers:
		my_expander = st.expander(label=ticker)
		my_expander.dataframe(scope.share_data_files[ticker], 2000, 2000)	



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Primary Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def ensure_share_data_is_available(params):
# 	if len(params.analysis['tickers_for_multi']) > 0:								# we have some share data to analyse
# 		# load_ticker_data_files( params )
# 		download_from_yahoo_finance( params )			
# 		combine_loaded_and_downloaded_ticker_data(params)
# 		check_share_data_for_missing_dates( params )   # ensure that the expected date ranges are actually available for each stock




# ==============================================================================================================================================================
# Combiner - concatenates any downloaded data with any loaded data resulting in a complete (hopefully) temporal history of existing share data
# ==============================================================================================================================================================
def combine_loaded_and_downloaded_ticker_data(scope): # WIP - change to check for loaded ticker
	st.subheader('Combining the Loaded and Downloaded Share Data Files')
	render_results( scope, passed='COMBINED > ', passed_2='CREATED new files > ', failed='na' )

	for ticker in scope.ticker_list:																		# iterate through the target tickers
		if ticker in scope.download_yf_share_data['ticker'].unique():										# if we have downloaded data (we may have nothing)
			ticker_data = scope.download_yf_share_data[scope.download_yf_share_data['ticker'] == ticker]	# subset to a specific ticker in the downloaded data
			ticker_data = ticker_data[scope.share_data_usecols]												# standardise the columns
			ticker_data = ticker_data[ticker_data['volume'] != 0]											# drop rows where volume is zero 
			if ticker in scope.share_data_loaded_list:														# we have an exisiting share_data_file so we concatenate the data
				scope.share_data_files[ticker] = pd.concat([scope.share_data_files[ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
				render_results( scope, ticker, result='passed' )
			else:
				scope.share_data_files[ticker] = ticker_data												# its brand new - so we can just add it to the dictionary
				render_results( scope, ticker, result='passed_2' )
			scope.share_data_files[ticker].sort_values(by=['date'], inplace=True)							# sort the share data into date order ascending
	render_results(scope, 'Finished', final_print=True )
	save_ticker_data_files( scope )


# ==============================================================================================================================================================
# Ticker Data : loaders and savers
# ==============================================================================================================================================================
def load_and_download_ticker_data( scope ):
	st.header('Downloading Tickers from Yahoo Finance')


	# 	if len(scope.tickers_for_multi) != 0: 
	# 		st.subheader('Loading Tickers (as specified by the Ticker List)')

	# load_ticker_data_files(scope, ticker_list)

	# determine_download_groups_for_y_finance(scope)   # DONT NEED THIS STEP ANYMORE

	download_from_yahoo_finance(scope )


	combine_loaded_and_downloaded_ticker_data(scope)

	# 		# check_share_data_for_missing_dates( scope )

	# scope.download_by_group = False
	scope.download_groups_for_y_finance = [] # Reset for next download

	# 	else:
	# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')



def load_ticker_data_files( scope ):
	render_results( scope, passed='LOADED Share Data Files > ', failed='MISSING Share Data Files for > ', passed_2='na' )

	# scope.share_data_loaded_list = []
	# scope.share_data_missing_list = []
	
	for ticker in scope.ticker_list:
	# for ticker in scope.tickers_for_multi:
		generate_path_for_share_data_file(scope, ticker )
		if os.path.exists( scope.path_share_data_file ):
			load_a_file(scope, ticker )
			scope.share_data_loaded_list.append(ticker)
			render_results( scope, ticker, result='passed' )
		else:
			scope.share_data_missing_list.append(ticker)
			render_results( scope, ticker, result='failed' )
	render_results(scope, 'Finished', final_print=True )

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

def save_ticker_data_files( scope ): # DONE
	st.subheader('Saving Share Data Files')
	render_results( scope, passed='Files SAVED > ', failed='na', passed_2='na' )
	for ticker in scope.share_data_files:
		generate_path_for_share_data_file(scope, ticker )
		save_ticker_data_file( scope, scope.share_data_files[ticker] )
		render_results( scope, ticker, result='passed' )
	render_results(scope, 'Finished', final_print=True )

def save_ticker_data_file( scope, dataframe ): # DONE
	saving_df = dataframe.copy()
	saving_df.to_csv( scope.path_share_data_file, index=False )


# ==============================================================================================================================================================
# Yahoo Finance - current source of OHLCV Share Data
# ==============================================================================================================================================================

def download_from_yahoo_finance( scope ): # WIP
	# group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
	# threads: use threads for mass downloading? (True/False/Integer)
	st.subheader('Downloading Ticker data from Yahoo Finance (as specified by the Ticker List')
	
	period = str(st.download_days) + 'd'

	reset_download_status(scope)
	# print ( 'download_groups_for_y_finance = ', scope.download_groups_for_y_finance )
	for count, y_finance_group in enumerate(scope.download_groups_for_y_finance):
		download_message = ('downloading > ' + y_finance_group + ' ( ' + str(count+1) + ' of ' + str(len(scope.download_groups_for_y_finance)) + ' )' )
		st.write(  download_message)
		print ( download_message)
		ticker_string = yahoo_ticker_string_for_each_group( scope, y_finance_group)

		print ( scope.download_schema)

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
# def determine_download_groups_for_y_finance(scope, ticker_list ): # TODO : this is complicated and needs refactoring
# 	# If appropriate, group the download by the industry 
# 	# groups as this simplifies the download process

# 	scope.download_groups_for_y_finance = []

# 	# group_method = ''
# 	if download_by_group == False:

# 	# if we are multi download, we do what we normally do, otherwise we do the selected tickers method (for singles)
# 	if scope.download_group_method == 'tickers_selected':
# 		scope.download_groups_for_y_finance.append('tickers_selected')
# 	elif scope.download_group_method == 'tickers_multi':
# 		if scope.tickers_market != 'select entire market':
# 			scope.download_groups_for_y_finance = ( list(scope.ticker_index_file['industry_group'].unique() ))
# 		elif len(scope.tickers_industries) != 0:
# 			scope.download_groups_for_y_finance = scope.selected_industry
# 		elif len(scope.tickers_selected) != 0:
# 			scope.download_groups_for_y_finance.append('tickers_selected')
# 	else:
# 		st.error( ('The scope.download_group_method value > ' + scope.download_group_method + ' < which has not been configured') )

def yahoo_ticker_string_for_each_group( scope, y_finance_group): # TODO - refactor this as well - that last function can be a single line
	# TODO - we need to know which ticker list to work with
	if y_finance_group == 'random_tickers':
		# we have selected specific tickers 
		tickers_list = scope.ticker_list
	else:
		# we have selected a specific market, industry or number of industries
		tickers_in_industry_group_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == y_finance_group ]
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
	render_results( scope, passed='Downloaded these Shares > ', passed_2='na', failed='Falied to Download > ' )
	failed_download_list = []
	for ticker, error in download_errors.items():
		failed_download_list.append(ticker)

	ticker_list = ticker_string.split(' ')
	
	for ticker in ticker_list:
		if ticker not in failed_download_list:
			render_results( scope, ticker, result='passed' )
		else:
			render_results( scope, ticker, result='failed' )
	render_results(scope, 'Finished', final_print=True )


# ==============================================================================================================================================================
# Update Share Index with download status information
# ==============================================================================================================================================================
def reset_download_status( scope ): # TODO - test output
	for ticker in scope.ticker_list:
		scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'set_for_download'

def update_download_status(scope ): # TODO DONE - but needs robust testing on a large group
	for ticker in scope.download_yf_share_data['ticker'].unique():
		scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'downloaded'
	for ticker, error_message in scope.download_yf_anomolies.items():
		if error_message == 'No data found, symbol may be delisted':
			scope.ticker_index_file.at[ticker, 'yahoo_status'] = 'delisted'
		else:
			st.write( ticker + ' - download error = ' + str(error_message))
	save_ticker_index_file(scope)


# ==============================================================================================================================================================
# Ticker List for Multi Ticker Analysis : Construct and Quick Show
# ==============================================================================================================================================================
def construct_list_of_ticker_codes(scope):
	st.header('Adding or Remove tickers from the Ticker List')
	ticker_list = []
	
	render_results( scope, passed='Added these selections ticker list > ', passed_2='na', failed='na' )

	# ##############################
	# Most detailed takes precedence
	# ##############################


	# Selected a ticker or tickers
	if len(scope.tickers_selected) != 0:
		for ticker in scope.tickers_selected:
			render_results( scope, ticker, result='passed' )
			ticker_list += [ticker]	
		pass

	# Selected an Industry
	elif len(scope.tickers_industries) != 0:
		for industry in scope.tickers_industries:
			render_results( scope, industry.upper(), result='passed' )
			tickers_in_industry_group_df = scope.ticker_index_file[scope.ticker_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	
	# Selected an entire share market
	elif scope.tickers_market != 'select entire market':
		render_results( scope, scope.tickers_market.upper(), result='passed' )
		available_tickers_for_this_market = scope.ticker_index_file.index.values.tolist()
		ticker_list =  available_tickers_for_this_market
	else:
		st.error('All Tickers removed from Ticker List')

	render_results(scope, 'Finished', final_print=True )

	scope.tickers_for_multi = ticker_list
	scope.tickers_update_list = False

	st.markdown("""---""")

	st.subheader('Ticker List - after adding dropdown selections')
	ticker_list_message = ''
	for ticker in scope.tickers_for_multi:
		ticker_list_message = ticker_list_message + ticker + ' - '
	st.success(ticker_list_message)

	st.write(('Number of tickers in Ticker List =  ( ' + str((len(scope.tickers_for_multi))) + ' ) tickers'))

def render_ticker_list(scope):
	st.header('Ticker List')
	st.subheader('target tickers for analysis')
	st.write('use sidebar to add tickers to this list)')
	ticker_list_message = ''
	for count, ticker in enumerate(scope.tickers_for_multi):
		ticker_list_message = ticker_list_message + ticker
		if count < len(scope.tickers_for_multi) - 1:
			ticker_list_message += '  '

	st.success(ticker_list_message)




# ==============================================================================================================================================================
# Share Data File - missing dates # TODO - Rob determine if we are still doing this?
# ==============================================================================================================================================================

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
# 				listing_date = (params.ticker_index['file'].loc[ticker]['listing_date'])
# 				if (listing_date > params.analysis['start'] and listing_date < params.analysis['end']) or (listing_date < params.analysis['start']) or (listing_date > params.analysis['end']):
# 					pre_listing_dates = list(pd.date_range(params.analysis['start'], listing_date, freq='B').strftime('%Y-%m-%d'))
# 					missing_dates_list = list(set(missing_dates_list) - set(pre_listing_dates))

# 			if len(missing_dates_list) > 0:
# 				# at the moment we need to manually tag the trading halt dates (after confirmation with the ASX that this is the case) terminal > pipenv run python app.py -th boq
# 				if pd.notna(params.ticker_index['file'].loc[ticker]['trading_halt_dates']):
# 					trading_halt_dates_list = [ date for date in params.ticker_index['file'].loc[ticker]['trading_halt_dates'].split()]
# 					missing_dates_list = list(set(missing_dates_list) - set(trading_halt_dates_list))

# 			if len(missing_dates_list) > 0 :
# 				store_missing_dates( params, ticker, missing_dates_list )
# 				output_result_to_terminal( params, ticker, result='failed' )
# 			else:
# 				store_missing_dates( params, ticker, None )
# 				output_result_to_terminal( params, ticker, result='passed' )
# 		output_result_to_terminal(params, (' - dates good for ' + cyan + str(params.terminal['count_passed']) + white + ' and gaps with ' + purple + str(params.terminal['count_failed']) + white), final_print=True )
# 		save_ticker_index_file(params)
# 		params.analysis['check_dates'] = False			# To prevent this function being run twice
# 		if params.reports['missing_dates']: print_missing_dates(params)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Update Share Index with any missing dates
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def reset_missing_dates(params):
# 	for ticker in params.share_data['files']:
# 		params.ticker_index['file'].at[ticker, 'missing_dates'] = 'checking_dates'

# def store_missing_dates( params, ticker, missing_dates_list ):
# 	if missing_dates_list != None:
# 		missing_dates_list.sort(key = lambda date: datetime.datetime.strptime(date, "%Y-%m-%d" ))
# 		missing_dates_string = ' '.join(missing_dates_list)
# 	else:
# 		missing_dates_string = None

# 	params.ticker_index['file'].at[ticker, 'missing_dates'] = missing_dates_string

# -----------------------------------------------------------------------------------------------------------------------------------
# Update Share Index with any Trading Halt Days
# -----------------------------------------------------------------------------------------------------------------------------------
# def update_trading_halt_days(params):
# 	if params.ticker_index['specified_trading_halt_codes'] != None:  # just make sure we have specified some codes
# 		terminal_heading( params, ( 'editing share index to account for trading halt days' + cyan + '   Changed' + '  /  ' + purple + 'Failed' + white ), line_filler='-' )
# 		output_result_to_terminal(params)
# 		for ticker in params.analysis['tickers_for_multi']:
# 			missing_dates_string = str(params.ticker_index['file'].loc[ticker]['missing_dates'])
# 			trading_halt_dates_string = str(params.ticker_index['file'].loc[ticker]['trading_halt_dates'])

# 			if missing_dates_string != 'nan' or missing_dates_string != None: # make sure we actually have some missing dates
# 				if trading_halt_dates_string == 'nan' or trading_halt_dates_string == None:
# 					# we have nothing so a simple copy will suffice
# 					params.ticker_index['file'].at[ticker, 'trading_halt_dates'] = missing_dates_string 
# 				else:
# 					# we had some trading halt days previously so we need to add them together
# 					params.ticker_index['file'].at[ticker, 'trading_halt_dates'] = trading_halt_dates_string + ' ' + missing_dates_string 
# 			params.ticker_index['file'].at[ticker, 'missing_dates'] = None  # as they are no longer missing - we have them accounted for in the trading_halt_days
# 			output_result_to_terminal( params, ticker, result='passed' )
# 		print ('')
# 		save_ticker_index_file(params)
# 	# rerun the date checker to make sure the result is what we wanted
# 	params.analysis['check_dates'] = True
# 	check_share_data_for_missing_dates(params)




# ==============================================================================================================================================================
#
#
# Redundant Code - delete once happy with the application codebase
#
# 
# ==============================================================================================================================================================



# -----------------------------------------------------------------------------------------------------------------------------------
# Replaced these functions with non specfic ticker lists
# -----------------------------------------------------------------------------------------------------------------------------------
# def load_ticker_data_files( scope ): # DONE
# 	render_results( scope, passed='LOADED Share Data Files > ', failed='MISSING Share Data Files for > ', passed_2='na' )

# 	scope.share_data_loaded_list = []
# 	scope.share_data_missing_list = []
	
# 	for ticker in scope.tickers_for_multi:
# 		generate_path_for_share_data_file(scope, ticker )
# 		if os.path.exists( scope.path_share_data_file ):
# 			load_a_file(scope, ticker )
# 			scope.share_data_loaded_list.append(ticker)
# 			render_results( scope, ticker, result='passed' )
# 		else:
# 			scope.share_data_missing_list.append(ticker)
# 			render_results( scope, ticker, result='failed' )
# 	render_results(scope, 'Finished', final_print=True )







# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Browser Render Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def load_tickers(scope, ticker_list ):
# 	st.header('Loading Tickers (as specified by the Ticker List)')

# 	if len(scope.tickers_for_multi) != 0: 
# 		load_ticker_data_files(scope)
# 	else:
# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
	
# 	st.write('Finished Loading Tickers')