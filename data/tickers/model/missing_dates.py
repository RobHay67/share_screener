import streamlit as st
import pandas as pd
import yfinance as yf					# https://github.com/ranaroussi/yfinance
# import datetime
import os


# TODO - this is older code that we may need to reimplement - keep for now rob 16/11/21









# from data.ticker_index import save_ticker_index_file
# from data.tickers.index.file import save_index
# # from scope import path_for_ticker_file



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





# -----------------------------------------------------------------------------------------------------------------------------------
# Missing Dates Reports TODO : Rob, work out if we still need this - should it even be in this module
# -----------------------------------------------------------------------------------------------------------------------------------


# def print_missing_dates(params):
# 	terminal_heading( params, 'Missing Dates for each ticker just assessed', line_filler='-', colour=yellow )
# 	print ( yellow, end='' )
# 	for ticker in params.share_data['files']:
# 		missing_dates_string = str(params.ticker_index['file'].at[ticker, 'missing_dates'])
# 		if missing_dates_string != 'None':
# 			qty = str(missing_dates_string.count(' ')+1)
# 			leader = ticker + white + ' (' + qty + ') ' + yellow
# 			if len(missing_dates_string) <= params.terminal['width'] - 20:
# 				print ( leader + missing_dates_string )
# 			else:
# 				for chunk in chunkstring(missing_dates_string, (11*16)):
# 					print ( leader + chunk )
# 	print ( yellow + '-'*params.terminal['width'] + white)

# def chunkstring(string, length):
# 	return (string[0+i:length+i] for i in range(0, len(string), length))





