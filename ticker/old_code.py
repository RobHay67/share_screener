import streamlit as st
import pandas as pd
import yfinance as yf					# https://github.com/ranaroussi/yfinance
# import datetime
import os
import pathlib

# from ticker_index import save_ticker_index_file
from ticker.index.file import save_index
# from scope import generate_path_for_share_data_file
from web.results import view_results

# ==============================================================================================================================================================
# Browser Render Controllers : 
# ==============================================================================================================================================================













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
# 		save_index(params)
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
# 		for ticker in params.analysis['ticker_list']:
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
# 		save_index(params)
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


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Primary Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def ensure_share_data_is_available(params):
# 	if len(params.analysis['ticker_list']) > 0:								# we have some share data to analyse
# 		# load_ticker_data_files( params )
# 		download_from_yahoo_finance( params )			
# 		combine_downloaded_with_any_loaded_ticker_data(params)
# 		check_share_data_for_missing_dates( params )   # ensure that the expected date ranges are actually available for each stock




# ==============================================================================================================================================================
# Browser Render Controller : Load and / or  Download share data
# ==============================================================================================================================================================
# def view_ticker_data_fetcher(scope, ticker_list):

# 	if isinstance(ticker_list, str): ticker_list = [ticker_list]

# 	st.header('Load and/or Download Share Data')
# 	col1,col2,col3 = st.columns([2,3,7])
# 	with col1: load_tickers = st.button('Load Share Data File')
# 	with col2: download_tickers = st.button( ( 'Download Previous ' + str(int(st.download_days)) + ' days') )

# 	if len(ticker_list) > 0:
# 		if load_tickers: 
# 			with col3: st.write( ('Loading ( ' + str(len(ticker_list)) + ' ) Tickers') )
# 			load_ticker_data_files(scope, ticker_list)
# 			with col3: st.write('Finished Loading Tickers')
			

# 		if download_tickers:
# 			with col3: st.write( ('Downloading ( ' + str(len(ticker_list)) + ' ) Tickers from Yahoo Finance') )

# 			load_ticker_data_files(scope, ticker_list)

# 			#TODO - ROB WE ARE up to this point - for some reason it was downloading the entire ASX - need to check this
# 			determine_download_groups_for_y_finance(scope)

# 			download_from_yahoo_finance(scope)

# 			combine_downloaded_with_any_loaded_ticker_data(scope)

# 			# check_share_data_for_missing_dates( scope )

# 			st.write('Finished Downloading Ticker Trading Data')
		
		
# 	else:
# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')



# def download_tickers(scope):
# 	st.header('Downloading Tickers from Yahoo Finance (as specified by the Ticker List)')

# 	if len(scope.ticker_list) != 0: 
# 		st.subheader('Loading Tickers (as specified by the Ticker List)')

# 		load_ticker_data_files(scope)

# 		determine_download_groups_for_y_finance(scope)

# 		download_from_yahoo_finance(scope)

# 		combine_downloaded_with_any_loaded_ticker_data(scope)

# 		# check_share_data_for_missing_dates( scope )

# 	else:
# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
	
# 	st.write('Finished Downloading Ticker Trading Data')




# def view_ticker_data_page(scope):
# 	st.title('Load and/or Download Share Data')
# 	st.info(('Current number of Loaded Files ( ' + str((len(scope.ticker_data_files))) + ' )'))

# 	view_ticker_data_fetcher(scope, ['test'])


	# col1,col2 = st.columns([4,4])

	# with col1: st.subheader('Load Share Data Files')
	# with col1: st.subheader('(per ticker list)')
	# with col1: st.write(('number of Files to Load = ( ' + str((len(scope.ticker_list))) + ' )'))
	# with col1: load_tickers = st.button('Load OHLCV Data')

	# with col2: st.subheader('Download Latest Share Data')
	# with col2: st.subheader('(per ticker list)')
	# with col2: st.download_days = st.number_input('change ( - / + )  number of days to download', min_value=1, max_value=1000, value=1, key='0')    
	# with col2: download_tickers = st.button('Download OHLCV Data')

	
	# st.markdown("""---""")

	# if load_tickers:
	# 	st.header('Loading Tickers (as specified by the Ticker List)')

	# 	if len(scope.ticker_list) != 0: 
	# 		load_ticker_data_files(scope)
	# 	else:
	# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
		
	# 	st.write('Finished Loading Tickers')

	# if download_tickers:
	# 	st.header('Downloading Tickers from Yahoo Finance (as specified by the Ticker List)')

	# 	if len(scope.ticker_list) != 0: 
	# 		st.subheader('Loading Tickers (as specified by the Ticker List)')

	# 		load_ticker_data_files(scope)

	# 		determine_download_groups_for_y_finance(scope)

	# 		download_from_yahoo_finance(scope)

	# 		combine_downloaded_with_any_loaded_ticker_data(scope)

	# 		# check_share_data_for_missing_dates( scope )

	# 	else:
	# 		st.error('Ticker List does not contain any tickers - add tickers using the sidebar')
		
	# 	st.write('Finished Downloading Ticker Trading Data')





	# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Yahoo Finance - helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def determine_download_groups_for_y_finance(scope, ticker_list ): # TODO : this is complicated and needs refactoring - actually lets just put the bruden back
# onto the caller to know what they need to download
# 	# If appropriate, group the download by the industry 
# 	# groups as this simplifies the download process

# 	scope.download_groups_for_y_finance = []

# 	# group_method = ''
# 	if download_by_group == False:

# 	# if we are multi download, we do what we normally do, otherwise we do the selected tickers method (for singles)
# 	if scope.download_group_method == 'tickers_multi':
# 		scope.download_groups_for_y_finance.append('tickers_multi')
# 	elif scope.download_group_method == 'tickers_multi':
# 		if scope.selected_market != 'select entire market':
# 			scope.download_groups_for_y_finance = ( list(scope.ticker_index['industry_group'].unique() ))
# 		elif len(scope.selected_industries) != 0:
# 			scope.download_groups_for_y_finance = scope.selected_industry
# 		elif len(scope.selected_tickers) != 0:
# 			scope.download_groups_for_y_finance.append('tickers_multi')
# 	else:
# 		st.error( ('The scope.download_group_method value > ' + scope.download_group_method + ' < which has not been configured') )

# def yahoo_ticker_string_for_each_group( scope, y_finance_group): # TODO - refactor this as well - that last function can be a single line
# 	# TODO - we need to know which ticker list to work with
# 	# TODO - this code should be done by the caller
# 	if y_finance_group == 'random_tickers':
# 		# we have selected specific tickers 
# 		tickers_list = scope.ticker_list
# 	else:
# 		# we have selected a specific market, industry or multiple industries
# 		tickers_in_industry_group_df = scope.ticker_index[scope.ticker_index['industry_group'] == y_finance_group ]
# 		tickers_list = tickers_in_industry_group_df.index.tolist()
	
# 	 # store the appropriate type of download for y_finance
# 	 # TODO - this could be done by the downloader rather than having another variable!!!!
# 	if len(tickers_list) == 1: 
# 		scope.download_schema = 'y_finance_single'  # we are only downloading a single ticker
# 	else:
# 		scope.download_schema = 'y_finance_multi'	# we are downloading multiple tickers

# 	# Build the Ticker String for Yahoo Finance
# 	ticker_string = ""
# 	for ticker in tickers_list:
# 		if len(ticker_string) != 0:
# 			ticker_string = ticker_string + " "
# 		ticker_string =  ticker_string + ticker
# 	return ticker_string