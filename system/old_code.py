# from types import SimpleNamespace

import pandas as pd
import pathlib
import os 
import time  
from datetime import datetime, timedelta 
import streamlit as st

# from ticker_index import load_ticker_index_file



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Params sub groups - for easier maintenance - we need to move any remaining variables into the set initial session state
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# def share_index_params(params):
	# trading halt params
	# TODO - come back to this one if needed
	# params.ticker_index['specified_trading_halt_codes'] = args.record_trading_halt_dates
	# if params.ticker_index['specified_trading_halt_codes'] == None:
	# 	params.ticker_index['edit_index'] = False
	# else:
	# 	params.ticker_index['edit_index'] = True

def analysis_params(params):
	# set function controlling params
	params.analysis['check_dates'] = True

	# Market Variables
	# params.analysis['market'] = args.share_market
	# params.analysis['entire_market'] = args.analyse_entire_market
	# params.analysis['industry_group'] = args.analyse_industry_group
	# params.analysis['specified_share_codes'] = args.analyse_specified_share_codes
	
	# TICKER LIST - primary iterator
	# TODO
	# construct_list_of_ticker_codes(params)

	# set trading variables
	# params.analysis['trade_value'] = args.analysis_trade_value
	# params.analysis['trade_cost'] = args.analysis_trade_cost

	# set date variables
	# params.analysis['no_of_days'] = args.analysis_no_of_days
	# at the moment, these are the same as the expected dates
	
	# will usually be yesterday unless we are running after 5PM today in which case it can be today
	# TODO - need to workout how to calculate this 
	# params.analysis['end_adjust'] =  1 if datetime.today().hour < 17 else 0  	
	# params.analysis['start'] = ( datetime.today() - timedelta(days=params.analysis['no_of_days']) )
	# params.analysis['end']   = ( datetime.today() - timedelta(days=params.analysis['end_adjust']) )

	# # Expected Dates to be available for any analysus
	# dates_excluding_weekends = list(pd.date_range(params.analysis['start'], params.analysis['end'], freq='B').strftime('%Y-%m-%d'))
	# dates_excluding_market_close_days = list( set(dates_excluding_weekends) - set(public_holidays[params.analysis['market']]))
	# params.analysis['date_list'] = dates_excluding_market_close_days

def report_params(params ):
	#TODO - work out what to do with this
	params.reports['missing_dates'] = False








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










