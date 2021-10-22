from types import SimpleNamespace
import time  
from datetime import datetime, timedelta 
import pandas as pd
import pathlib
import os 
import streamlit as st

from share_index import load_share_index_file
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Config - Market Information
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
markets = {
					'ASX' : { 'ticker_suffix':'.AX' },
					'USA' : { 'ticker_suffix':'.US' },
				}

public_holidays = {
						'ASX':[ '2021-12-28', '2021-12-27', '2021-06-14', '2021-04-25', '2021-04-05', '2021-04-02', '2021-01-26', '2021-01-01', 
								'2020-12-28', '2020-12-25', '2020-06-08', '2020-04-13', '2020-04-10',               '2020-01-27', '2020-01-01', ],
						'USA':['2021-12-27'],
						}

opening_hours = { 
						'ASX':{
							'group_1':{'letter_range':['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time':'10:00:00','minutes_per_day':360   },
							'group_2':{'letter_range':['C', 'D', 'E', 'F'],                          'opening_time':'10:02:00','minutes_per_day':357.75},
							'group_3':{'letter_range':['G', 'H', 'I', 'J', 'K', 'L', 'M'],           'opening_time':'10:05:00','minutes_per_day':355.5 },
							'group_4':{'letter_range':['N', 'O', 'P', 'Q', 'R'],                     'opening_time':'10:07:00','minutes_per_day':353.25},
							'group_5':{'letter_range':['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],      'opening_time':'10:09:00','minutes_per_day':351   },
						},
						'USA':{	'group_1':{'letter_range':['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time':'10:00:00','minutes_per_day':360   },
							},
				}

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Share Data file Schema
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

share_data_schema =  {
					1 : { 'col_name' : 'date'   , 'index_col' : True  , 'data_type' : 'datetime64[ns]'  },
					2 : { 'col_name' : 'open'   , 'index_col' : False , 'data_type' : 'float64'         },
					3 : { 'col_name' : 'high'   , 'index_col' : False , 'data_type' : 'float64'         },
					4 : { 'col_name' : 'low'    , 'index_col' : False , 'data_type' : 'float64'         },
					5 : { 'col_name' : 'close'  , 'index_col' : False , 'data_type' : 'float64'         },
					6 : { 'col_name' : 'volume' , 'index_col' : False , 'data_type' : 'int64'           }, 
					0 : { 'col_name' : 'ticker' , 'index_col' : False , 'data_type' : None              },   # will not be added to the column dictionary
					# 0 : { 'col_name' : 'unused' , 'index_col' : False , 'data_type' : None              },
					}

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Download Share Data - various schemas
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# the key provides a unique identifier and also the column order - 0's are removed from the final dataframe
# list the downloaded column names from the download ( in order they come down in )
# map each column to the share_data_schema by utilising the same key 
# ie col 3 (High) maps to col 3 in the applocation_cols dictionary ( high )
# column keys > 50 will be ignored
download_share_data_schemas =    {
							'y_finance_single' :   {
													1 : { 'col_name' : 'Date'       , 'index_col' : True  },
													2 : { 'col_name' : 'Open'       , 'index_col' : False },
													3 : { 'col_name' : 'High'       , 'index_col' : False },
													4 : { 'col_name' : 'Low'        , 'index_col' : False },
													5 : { 'col_name' : 'Close'      , 'index_col' : False },
													50: { 'col_name' : 'Adj Close'  , 'index_col' : False },
													6 : { 'col_name' : 'Volume'     , 'index_col' : False },
													0 : { 'col_name' : 'Ticker'     , 'index_col' : False },   # manually added by the imported for consistency
													},
							'y_finance_multi' :     {
													1 : { 'col_name' : 'Date'       , 'index_col' : True  },
													0 : { 'col_name' : 'Ticker'     , 'index_col' : False },
													98: { 'col_name' : 'Adj Close'  , 'index_col' : False },
													5 : { 'col_name' : 'Close'      , 'index_col' : False },
													3 : { 'col_name' : 'High'       , 'index_col' : False },
													4 : { 'col_name' : 'Low'        , 'index_col' : False },
													2 : { 'col_name' : 'Open'       , 'index_col' : False },
													6 : { 'col_name' : 'Volume'     , 'index_col' : False },
													}
							}

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope out the Params Object == session_state in streamlit
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_session_variables(session_state, project_description):
	if 'initial_run' not in session_state:
		session_state.initial_run = True
	else:
		session_state.initial_run = False

	# print ( 'INITL STATE = ', session_state.initial_run )

	if session_state.initial_run:
		# Project Params
		session_state.project_description = project_description
		session_state.project_start_time = time.time()
		# Terminal Params
		session_state.terminal_audit = False
		session_state.terminal_width = 200
		session_state.terminal_print_width = 0
		session_state.terminal_count_passed = 0
		session_state.terminal_count_passed_2 = 0
		session_state.terminal_count_failed = 0
		# Folders
		session_state.folder_project = pathlib.Path(__file__).parent.resolve()
		session_state.folder_share_data = pathlib.Path.home().joinpath( session_state.folder_project, 'share_data' )
		session_state.folder_results_analysis = pathlib.Path.home().joinpath( session_state.folder_project, 'results_analysis' )
		session_state.folder_website = pathlib.Path.home().joinpath( session_state.folder_project, 'website' )
		if not os.path.isdir( session_state.folder_project ) : os.makedirs( session_state.folder_project )
		if not os.path.isdir( session_state.folder_share_data ) : os.makedirs( session_state.folder_share_data )
		if not os.path.isdir( session_state.folder_results_analysis ) : os.makedirs( session_state.folder_results_analysis )
		if not os.path.isdir( session_state.folder_website ) : os.makedirs( session_state.folder_website )
		# File Paths
		session_state.path_share_index = pathlib.Path.home().joinpath( session_state.folder_project, 'share_index.csv' )
		session_state.path_website_file = pathlib.Path.home().joinpath( session_state.folder_website, 'strategy_results.json' )
		session_state.path_share_data_file = 'not yet set',
		# Available Share Markerts
		session_state.available_markets = list(markets.keys())
		session_state.selected_market = 'ASX'
		# Share Index - Default Load = Australia
		load_share_index_file(session_state)
		# Available Share industries
		industries = session_state.share_index_file['industry_group'].unique().tolist()
		industries.sort()
		session_state.available_industries = industries
		# Available Share Tickers
		session_state.available_tickers = session_state.share_index_file.index.values.tolist()
		# Ticker list - for analysis
		session_state.update_ticker_list = True
		# Share Data Files
		session_state.share_data_files = {}
		session_state.share_data_loaded_list = []
		session_state.share_data_missing_list = []
		# session_state.share_data_schema = share_data_schema
		# session_state.share_data_usecols = ['date', 'open', 'high', 'low', 'close', 'volume']
		# session_state.share_data_dtypes = {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
		# session_state.share_data_dates = ['date']



		# Market Dictionaries
		session_state.market_suffix = markets
		session_state.market_public_holidays = public_holidays
		session_state.market_opening_hours = opening_hours	
		

		# Strategy Params
		session_state.strategy_name = 'None yet Selected', 
		session_state.strategy_print_header = True
		session_state.strategy_price_columns = ['open', 'high', 'low', 'close' ]
		session_state.strategy_print_count = 0
		session_state.strategy_build_header = True
		session_state.strategy_header = {1:'', 2:'', 3:'', 4:''}
		session_state.strategy_print_line = ''
		session_state.strategy_json_dict = { "shares":{}, "columnNames":[] }
		session_state.strategy_results = {}


		# Chart Variables
		session_state.chart_lines = []
		session_state.chart_macd_on_price = {}
		session_state.chart_macd_on_volume = {}


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Params sub groups - for easier maintenance
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# def share_index_params(params):
	# trading halt params
	# TODO - come back to this one if needed
	# params.share_index['specified_trading_halt_codes'] = args.record_trading_halt_dates
	# if params.share_index['specified_trading_halt_codes'] == None:
	# 	params.share_index['edit_index'] = False
	# else:
	# 	params.share_index['edit_index'] = True

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
	# construct_list_of_share_codes(params)

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

	
# def download_params(params):
	# params.download['no_of_days'] = args.download_no_of_days
	# if params.download['no_of_days'] >= 1: 
	# 	params.download['downloading_it'] = True
	# 	params.download['combining'] = True
	# else:
	# 	params.download['downloading_it'] = False
	# 	params.download['combining'] = False
	# params.download['schemas'] = download_share_data_schemas	
	# params.download['yf_share_data'] = pd.DataFrame(columns=params.share_data['usecols'] + ['ticker'] )
	# params.download['yf_anomolies'] =  {} 
	# # Dates for the download - Y-finance seems to want tomorrows date for the end period - so end date is exlusive
	# download_end   = params.analysis['end'] + timedelta(days=1)
	# download_begin = download_end - timedelta(days=params.download['no_of_days'])
	# params.download['begin'] = (download_begin).strftime('%Y-%m-%d') 
	# params.download['end']   = (download_end  ).strftime('%Y-%m-%d') 
	# # Industry Groups for the downloader
	# params.download['industry_group'] = ''
	# if params.analysis['entire_market'] == True: 
	# 	params.download['industry_group'] = ( list(params.share_index['file']['industry_group'].unique() ))
	# if params.analysis['industry_group'] != None and params.analysis['entire_market'] == False:	
	# 	params.download['industry_group'] = [ params.analysis['industry_group'] ]
	# if params.analysis['specified_share_codes'] != None and params.analysis['industry_group'] == None: 
	# 	params.download['industry_group'] = ['specified_share_codes']



# -----------------------------------------------------------------------------------------------------------------------------------
# share file path generator
# -----------------------------------------------------------------------------------------------------------------------------------

def generate_path_for_share_data_file( params, ticker ):
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'
	file_path = pathlib.Path.home().joinpath( params.folder_share_data, file_name )
	params.path_share_data_file = file_path

# ===================================================================================================================================
# 
# Construct Ticker Lists for Analysis and Downloading validated share codes
#
# ===================================================================================================================================
def construct_list_of_share_codes(params):
	st.info('Updating list of ticker codes')
	ticker_list = []
	
	# Most detailed takes precedece
	if len(params.selected_tickers) != 0:
		for ticker in params.selected_tickers:
			st.warning('adding this ticker to the Ticker List = ' + ticker )
			ticker_list += [ticker]	
		pass
	elif len(params.selected_industry) != 0:
		for industry in params.selected_industry:
			st.warning('adding ' + industry.upper() + ' to the ticker list' )
			tickers_in_industry_group_df = params.share_index_file[params.share_index_file['industry_group'] == industry ]
			tickers_in_industry = tickers_in_industry_group_df.index.tolist()
			ticker_list += tickers_in_industry 
		pass
	elif params.selected_industry != 'Select an Industry':
		available_market_codes = params.share_index_file.index.values.tolist()
		ticker_list =  available_market_codes
	else:
		st.warning('Could not build a ticker list for analyis')

	params.ticker_list = ticker_list
	params.update_ticker_list = False




#
# -----------------------------------------------------------------------------------------------------------------------------------
# Colours
# -----------------------------------------------------------------------------------------------------------------------------------
red         = '\033[91m'
green       = '\033[92m'
yellow      = '\033[93m'
blue        = '\033[94m'
purple      = '\033[95m'
cyan        = '\033[96m'
white 		= '\033[0m'