



# import pandas as pd
# import yfinance as yf					# https://github.com/ranaroussi/yfinance
# import datetime
# import os

# from share_index import save_share_index_file
# from params import generate_path_for_share_data_file
# from reports import report_progress, terminal_heading, output_result_to_terminal, print_missing_dates





# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Primary Controller
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def ensure_share_data_is_available(params):
	if len(params.analysis['ticker_list']) > 0:								# we have some share data to analyse
		load_share_data_files( params )
		download_from_yahoo_finance( params )			
		combine_loaded_and_downloaded_share_data(params)
		check_share_data_for_missing_dates( params )   # ensure that the expected date ranges are actually available for each stock

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Primary Controller
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def combine_loaded_and_downloaded_share_data(params):
# 	if params.download['combining']:   # we only need to run this function if we have recently downloaded some share data
# 		terminal_heading( params, ( 'combine loaded and downloaded share data ' + cyan + ' COMBINED' + '  /  ' + yellow + ' ADDED ' + ' / ' + purple + 'SKIPPED'), line_filler='-' )
# 		output_result_to_terminal(params)
# 		for ticker in params.analysis['ticker_list']:
# 			if ticker in params.download['yf_share_data']['ticker'].unique():
# 				ticker_data = params.download['yf_share_data'][params.download['yf_share_data']['ticker'] == ticker]	# subset to specific ticker
# 				ticker_data = ticker_data[params.share_data['usecols']]													# standardise the columns
# 				ticker_data = ticker_data[ticker_data['volume'] != 0]													# drop rows where volume is zero 
# 				if ticker in params.share_data['loaded_list']:		# we have an exisiting share_data_file so we concatenate the data
# 					params.share_data['files'][ticker] = pd.concat([params.share_data['files'][ticker], ticker_data]).drop_duplicates(subset=['date'], keep='last')
# 					output_result_to_terminal( params, ticker, result='passed' )
# 				else:
# 					params.share_data['files'][ticker] = ticker_data		# its brand new - so we can just add it to the dictionary
# 					output_result_to_terminal( params, ticker, result='passed_2' )
# 				params.share_data['files'][ticker].sort_values(by=['date'], inplace=True)					# sort the share data into date order ascending
# 			else:  
# 				output_result_to_terminal( params, ticker, result='failed' )
# 		output_result_to_terminal(params, ( ' - merged ' + cyan + str(params.terminal['count_passed']) + white + ' added ' + yellow + str(params.terminal['count_passed_2']) + white + ' and skipped ' + purple + str(params.terminal['count_failed']) + white), final_print=True )
# 		save_share_data_files( params )
# 		params.download['combining'] = False  # to prevent this function running a second time

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
# def load_share_data_files( params ):
# 	if len(params.share_data['loaded_list']) == 0:   			# prevent loading files if they have already been loaded
# 		terminal_heading( params, ( 'load share data files ' + cyan + 'LOADED' + '  /  ' + purple + 'MISSING' + white + '     ( download required for inclusion in strategy analysis )'), line_filler='-' )
# 		output_result_to_terminal( params )
# 		for ticker in params.analysis['ticker_list']:
# 			generate_path_for_share_data_file(params, ticker )
# 			if os.path.exists( params.path_share_data_file ):
# 				load_a_file(params, ticker )
# 				params.share_data['loaded_list'].append(ticker)
# 				output_result_to_terminal( params, ticker, result='passed' )
# 			else:
# 				params.share_data['missing_list'].append(ticker)
# 				output_result_to_terminal( params, ticker, result='failed' )
# 		output_result_to_terminal( params, ( ' - loaded ' + cyan + str(params.terminal['count_passed']) + white + ' files' + white ), final_print=True )
# 	return params

# def load_a_file( params, ticker ):
# 	share_data_file = pd.read_csv (  
# 									params.path_share_data_file, 
# 									header      = 0,
# 									# nrows       = params.row_limitor, 
# 									usecols     = params.share_data['usecols'],
# 									# index_col   = 'date', 
# 									dtype       = params.share_data['dtypes'],
# 									parse_dates = params.share_data['dates'],
# 									)
# 	params.share_data['files'][ticker] = share_data_file
# 	return share_data_file

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Share Data File - Saver - local
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def save_share_data_files( params ):
# 	terminal_heading( params, ('Saving this many Share Data Files > ' + str(len(params.share_data['files']))), line_filler='-', colour=cyan )
# 	report_progress(params, 'Saving Share Data files into the local folder ', ( cyan + 'saved' + '  /  ' + purple + 'not saved' + white))
# 	output_result_to_terminal( params )
# 	for ticker in params.share_data['files']:
# 		generate_path_for_share_data_file(params, ticker )
# 		save_share_data_file( params, params.share_data['files'][ticker] )
# 		output_result_to_terminal( params, ticker, result='passed' )
# 	output_result_to_terminal (params, ( ' - saved ' + cyan + str(params.terminal['count_passed']) + white + ' files' + white ), final_print=True )

# def save_share_data_file( params, dataframe ):
# 	saving_df = dataframe.copy()
# 	saving_df.to_csv( params.path_share_data_file, index=False )

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Yahoo Finance - Source of Share Data
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # group_by: group by column or ticker (‘column’/’ticker’, default is ‘column’)
# # threads: use threads for mass downloading? (True/False/Integer)

# def download_from_yahoo_finance( params ):
# 	if params.download['downloading_it']:					# prevent downloading if we have already completed the download
# 		download_date_range = string_of_date_range( params.download['begin'], params.download['end'])
# 		terminal_heading( params, ( 'download share data files from Yahoo Finance ' + download_date_range + cyan + '   LOADED' + '  /  ' + purple + 'UNABLE TO DONWLOAD' + white ), line_filler='-' )
# 		reset_download_status(params)
# 		for count, industry_group in enumerate(params.download['industry_group']):
# 			print ( 'downloading >', industry_group, '(', count+1, 'of', len(params.download['industry_group']), ')')
# 			ticker_string = yahoo_ticker_string_by_industry( params, industry_group)
# 			if params.download['download_schema'] == 'y_finance_single':
# 				yf_download = yf.download( ticker_string, start=params.download['begin'], end=params.download['end'] , progress=True, show_errors=False )
# 				yf_download['Ticker'] = ticker_string   								# manually add the ticker column as its missing
# 				print (yf_download)
# 			else:
# 				yf_download = yf.download( ticker_string, group_by = 'ticker', start=params.download['begin'], end=params.download['end'], progress=True, threads=True, show_errors=False )
# 				yf_download = yf_download.stack(level=0).rename_axis(['Date', 'Ticker']).reset_index(level=1)
# 			yf_download = format_columns_in_downloaded_share_data( params, yf_download )	
# 			store_yf_download_in_params( params, ticker_string, yf_download, yf.shared._ERRORS )
# 		update_download_status(params)
# 	params.download['downloading_it'] = False  # to prevent this running again

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Yahoo Finance - helpers
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------

# def yahoo_ticker_string_by_industry( params, industry_group):
# 	if industry_group == 'specified_share_codes':
# 		tickers_list = params.analysis['ticker_list']
# 	else:
# 		tickers_in_industry_group_df = params.share_index['file'][params.share_index['file']['industry_group'] == industry_group ]
# 		tickers_list = tickers_in_industry_group_df.index.tolist()
	
# 	if len(tickers_list) == 1:  # store the type of download y_finance
# 		params.download['download_schema'] = 'y_finance_single'
# 	else:
# 		params.download['download_schema'] = 'y_finance_multi'

# 	ticker_string = ""
# 	for ticker in tickers_list:
# 		if len(ticker_string) != 0:ticker_string = ticker_string + " "
# 		ticker_string =  ticker_string + ticker
# 	return ticker_string

# def format_columns_in_downloaded_share_data( params, yf_download ):
# 	report_progress ( params, 'rename imported columns and remove redundant columns' )

# 	download_schema = params.download['download_schema']
# 	yf_download.reset_index(inplace=True)   # remove any index set during import - we will set the index later

# 	for col_no in params.download['schemas'][download_schema]:
# 		provider_column_name    = params.download['schemas'][download_schema][col_no]['col_name']
# 		if col_no < 50:                 # its a column we are keeping - anything tagged with a key above 50 can be removed
# 			application_column_name = params.share_data['schema'][col_no]['col_name']
# 			yf_download.rename(columns = { provider_column_name : application_column_name }, inplace = True)
# 		else:                           # its a column we do not need so lets delete it
# 			del yf_download[provider_column_name]
# 	yf_download['volume'] = yf_download['volume'].fillna(0).astype(int)
# 	return( yf_download )

# def store_yf_download_in_params( params, ticker_string, yf_download, download_errors ):
# 	# store the downloaded data in a single dictionary
# 	params.download['yf_share_data'] = pd.concat([params.download['yf_share_data'], yf_download], sort=False)
# 	params.download['yf_anomolies'].update(download_errors)	# store any errors
# 	output_result_to_terminal(params)
# 	failed_download_list = []
# 	for ticker, error in download_errors.items():
# 		failed_download_list.append(ticker)

# 	ticker_list = ticker_string.split(' ')
	
# 	for ticker in ticker_list:
# 		if ticker not in failed_download_list:
# 			output_result_to_terminal( params, ticker, result='passed' )
# 		else:
# 			output_result_to_terminal( params, ticker, result='failed' )
# 	output_result_to_terminal ( params, ('- downloaded = ' + cyan + str(params.terminal['count_passed']) + white + ' failed = ' + purple + str(params.terminal['count_failed']) + white ), final_print=True )

# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# # Update Share Index with yahoo download information
# # --------------------------------------------------------------------------------------------------------------------------------------------------------------
# def reset_download_status( params ):
# 	for ticker in params.analysis['ticker_list']:
# 		params.share_index['file'].at[ticker, 'yahoo_status'] = 'set_for_download'

# def update_download_status(params):
# 	for ticker in params.download['yf_share_data']['ticker'].unique():
# 		params.share_index['file'].at[ticker, 'yahoo_status'] = 'downloaded'
# 	for ticker, error_message in params.download['yf_anomolies'].items():
# 		if error_message == 'No data found, symbol may be delisted':
# 			params.share_index['file'].at[ticker, 'yahoo_status'] = 'delisted'
# 		else:
# 			print ( purple + ticker + white + ' - failed to download - error = ' + str(error_message))
# 	save_share_index_file(params)

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
# # Helpers - a nice date range string for terminal output
# # -----------------------------------------------------------------------------------------------------------------------------------

# def string_of_date_range( date_1, date_2 ): 
# 	date_1 = datetime.datetime.strptime( date_1, "%Y-%m-%d" )
# 	date_2 = datetime.datetime.strptime( date_2, "%Y-%m-%d" )
# 	no_of_days = date_1 - date_2
# 	return ( str(date_1) + ' <--> ' + str(date_2) + ' ' + str(no_of_days.days) + ' days')

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