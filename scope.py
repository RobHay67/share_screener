# from types import SimpleNamespace

import pandas as pd
import pathlib
import os 
import time  
from datetime import datetime, timedelta 
import streamlit as st

from ticker_index import load_ticker_index_file

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
							'timezone':'Australia/Sydney',
							# https://www.marketindex.com.au/trading-hours
							'group_1':{'letter_range':['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time':'10:00:00','minutes_per_day':360   },
							'group_2':{'letter_range':['C', 'D', 'E', 'F'],                          'opening_time':'10:02:15','minutes_per_day':357.75},
							'group_3':{'letter_range':['G', 'H', 'I', 'J', 'K', 'L', 'M'],           'opening_time':'10:04:30','minutes_per_day':355.5 },
							'group_4':{'letter_range':['N', 'O', 'P', 'Q', 'R'],                     'opening_time':'10:06:45','minutes_per_day':353.25},
							'group_5':{'letter_range':['S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],      'opening_time':'10:09:00','minutes_per_day':351   },
						},
						'USA':{	
							'timezone':'US/Central',
							'group_1':{'letter_range':['1', '2', '3', '4', '5', '8', '9', 'A', 'B'], 'opening_time':'10:00:00','minutes_per_day':360   },
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









# ================================================================================================================================================================
#        							Multi Share Code Analysis		Volume Predictor						Company Profile							Daily Analysis
# ----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Appropriate Code List				tickers_for_multi				ticker_for_vol_predict					ticker_for_company_profile
# how do we select tickers to add	dropdown_markets				dropdown_ticker_for_volume_analysis		dropdown_ticker_for_company_profile
#									dropdown_industries
#									dropdown_tickers
# Files are stored					share_data_multi_files			share_data_volume_file					share_data_profile_file					share_data_analysis_file



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope out the Params Object == scope in streamlit
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_initial_scope(scope, project_description):
	if 'initial_load' not in scope:
		# set the initial state for the application - keep this to a minimum
		scope.initial_load = True
		scope.update_dropdown_lists = True
		# Set Initial Applications Selections
		scope.share_market = 'ASX'
		scope.chosen_market = None
		scope.chosen_industries = None
		scope.chosen_tickers = None
		scope.ticker_for_vol_predict = 'select a ticker'
		scope.ticker_for_company_profile = 'select a ticker'


	if scope.initial_load:
		# st.warning('Updating the session state params')
		# Streamlit Params
		scope.display_page = 'undetermined'

		# Project Params
		scope.project_description = project_description
		scope.project_start_time = time.time()
				
		# Results - for batch processing of multiple tickers
		scope.result_passed = ''
		scope.result_passed_2 = ''
		scope.result_failed = ''
		scope.result_passed_count = 0
		scope.result_passed_2_count = 0
		scope.result_failed_count = 0
		
		# Folders
		scope.folder_project = pathlib.Path(__file__).parent.resolve()
		scope.folder_share_data = pathlib.Path.home().joinpath( scope.folder_project, 'share_data' )
		scope.folder_results_analysis = pathlib.Path.home().joinpath( scope.folder_project, scope.folder_share_data, 'results_analysis' )
		scope.folder_website = pathlib.Path.home().joinpath( scope.folder_project, scope.folder_share_data, 'website' )
		if not os.path.isdir( scope.folder_project ) : os.makedirs( scope.folder_project )
		if not os.path.isdir( scope.folder_share_data ) : os.makedirs( scope.folder_share_data )
		if not os.path.isdir( scope.folder_results_analysis ) : os.makedirs( scope.folder_results_analysis )
		if not os.path.isdir( scope.folder_website ) : os.makedirs( scope.folder_website )
		
		# File Paths
		scope.path_ticker_index = pathlib.Path.home().joinpath( scope.folder_share_data, 'ticker_index.csv' )
		scope.path_website_file = pathlib.Path.home().joinpath( scope.folder_website, 'strategy_results.json' )
		scope.path_share_data_file = 'not yet set',
		# Load the Ticker Index File
		load_ticker_index_file(scope)

		# Ticker list - for analysis
		scope.update_ticker_list_required = False
		scope.tickers_for_multi = []

		# Share Data Files
		scope.share_data_files = {}
		scope.share_data_loaded_list = []
		scope.share_data_missing_list = []
		scope.share_data_schema = share_data_schema
		scope.share_data_usecols = ['date', 'open', 'high', 'low', 'close', 'volume']
		scope.share_data_dtypes = {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
		scope.share_data_dates = ['date']

		# Market Dictionaries
		scope.market_suffix = markets
		scope.market_public_holidays = public_holidays
		scope.market_opening_hours = opening_hours	

		# Download Ticker Variables
		scope.download_days = 1
		scope.download_groups_for_y_finance = []
		scope.download_schema = None
		scope.download_schemas = download_share_data_schemas	
		scope.download_yf_share_data = pd.DataFrame(columns=scope.share_data_usecols + ['ticker'] )
		scope.download_yf_anomolies =  {}
		
		# Analysis Variables
		scope.dropdown_colums = ['open', 'high', 'low', 'close', 'volume']



		# Strategy Params
		scope.strategy_name = 'None yet Selected', 
		scope.strategy_print_header = True
		scope.strategy_price_columns = ['open', 'high', 'low', 'close' ]
		scope.strategy_print_count = 0
		scope.strategy_build_header = True
		scope.strategy_header = {1:'', 2:'', 3:'', 4:''}
		scope.strategy_print_line = ''
		scope.strategy_json_dict = { "shares":{}, "columnNames":[] }
		scope.strategy_results = {}

		# Chart Variables
		scope.chart_lines = []
		scope.chart_macd_on_price = {}
		scope.chart_macd_on_volume = {}

		st.session_state.initial_load = False
		
def refresh_ticker_dropdown_lists(scope):
	print ( '\033[91m' + 'Dropdown Lists have been repopulated' + '\033[0m' )

	# ---------------------------------------------------------------------------------------
	# Single Share Market Selector
	list_of_markets = list(scope.market_suffix.keys())
	list_of_markets.insert(0, '< select entire market >')
	scope.dropdown_markets = list_of_markets
	# scope.dropdown_markets_re_render = True
	
	# ---------------------------------------------------------------------------------------
	# Multi Share Industry Selector
	list_of_industries = scope.ticker_index_file['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.dropdown_industries = list_of_industries
	# scope.dropdown_industries_re_render = True
	
	# ---------------------------------------------------------------------------------------
	# Multi Share Ticker Selector
	list_of_tickers = scope.ticker_index_file.index.values.tolist()
	scope.dropdown_tickers = list_of_tickers
	scope.dropdown_tickers_re_render = True
	# scope.dropdown_ticker_volume_re_render = True

	# ---------------------------------------------------------------------------------------
	# Single Ticker Selector for Volume Analysis
	tickers_for_volume_prediction = scope.ticker_index_file.index.values.tolist()
	tickers_for_volume_prediction.insert(0, 'select a ticker')
	scope.dropdown_ticker_for_volume_analysis = tickers_for_volume_prediction

	# ---------------------------------------------------------------------------------------
	# Single Ticker Selector for Company Profile
	tickers_for_company_profile = scope.ticker_index_file.index.values.tolist()
	tickers_for_company_profile.insert(0, 'select a ticker')
	scope.dropdown_ticker_for_company_profile = tickers_for_company_profile
	
	# ---------------------------------------------------------------------------------------
	# Dont run this again unless we have downloaded new share data
	# scope.update_dropdown_lists = False
	
# -----------------------------------------------------------------------------------------------------------------------------------
# share file path generator
# -----------------------------------------------------------------------------------------------------------------------------------

def generate_path_for_share_data_file( scope, ticker ): # DONE
	file_name = ( ticker.replace( '.', '_' ) ) + '.csv'
	file_path = pathlib.Path.home().joinpath( scope.folder_share_data, file_name )
	scope.path_share_data_file = file_path

# ==============================================================================================================================================================
# Render all Scope Variables
# ==============================================================================================================================================================

def render_scope_page(scope):
	st.title('Application Parameters')

	col1,col2,col3,col4 = st.columns([2,2,2,2])

	with col1: st.subheader('Lists')
	with col1: show_tickers = st.button('Ticker Lists ( ' + str((len(scope.tickers_for_multi))) + ' )')
	with col1: show_industries = st.button('Industries')

	with col2: st.subheader('Data')
	with col2: show_ticker_index = st.button('Ticker Index File ( ' + str((len(st.session_state.ticker_index_file))) + ' )')
	with col2: show_share_data_files = st.button('Share Data Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )')
	with col2: show_download = st.button('Download Settings')

	with col3: st.subheader('Analysis')
	with col3: show_strategy = st.button('Strategy')
	with col3: show_charting = st.button('Charting')

	with col4: st.subheader('Parameters')
	with col4: show_application_variables = st.button('Application Variables')
	with col4: show_folders = st.button('Folder Locations')
	with col4: show_market = st.button('Share Market Information')

	if show_tickers:
		st.subheader('Ticker Lists')

		render_3_columns( 'Ticker Dropdown Lists need updating', scope.update_dropdown_lists, 'update_dropdown_lists' )
				
		st.markdown("""---""")
		st.subheader('Ticker List for Multi Share Code Analysis')
		render_3_columns( 'Ticker List - Multi', scope.tickers_for_multi, 'tickers_for_multi' )
		render_3_columns( 'Loaded Ticker List', scope.share_data_loaded_list, 'share_data_loaded_list' )
		render_3_columns( 'Missing Ticker List', scope.share_data_missing_list, 'share_data_missing_list' )

		st.markdown("""---""")
		st.subheader('Ticker List for Single Share Code Analysis')
		render_3_columns( 'Ticker List - for Volume Prediction', scope.ticker_for_vol_predict, 'ticker_for_vol_predict' )
		render_3_columns( 'Ticker List - for Company Profile', scope.ticker_for_company_profile, 'ticker_for_company_profile' )
		# render_3_columns( 'Ticker List - for Volume Prediction', scope.ticker_for_vol_predict, 'ticker_for_vol_predict' )




	if show_industries:
		st.subheader('Share Index File contains the following Industries')
		industry_group_count = pd.DataFrame(scope.ticker_index_file['industry_group'].value_counts())
		industry_group_count.index.name = 'Industry'
		industry_group_count.columns =['No of Codes']
		st.dataframe(industry_group_count, 2000, 1200)

	if show_ticker_index:
		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Ticker Index File')
		with col2: st.write('< ticker_index_file >')
		st.dataframe(scope.ticker_index_file, 2000, 1200)

	if show_share_data_files:

		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Loaded and Downloaded share data.')
		with col2: st.write('< share_data_files >')

		list_of_loaded_tickers = list(scope.share_data_files.keys())

		for ticker in list_of_loaded_tickers:
			my_expander = st.expander(label=ticker)
			my_expander.dataframe(scope.share_data_files[ticker], 2000, 2000)

	if show_download:
		st.subheader('Download Parameters')

		render_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

		st.markdown("""---""")
		st.subheader('Most Recent Download Variables and Data')

		render_3_columns( 'Appropriate download method', scope.download_schema, 'download_schema' )
		render_3_columns( 'Batched Groups of tickers for the download', scope.download_groups_for_y_finance, 'download_groups_for_y_finance' )
		render_3_columns( 'Downloaded Data from y_finance', scope.chart_lines, 'chart_lines' )
		render_3_columns( 'Error Messages from y_finance', scope.download_yf_anomolies, 'download_yf_anomolies' )

		st.markdown("""---""")
		st.subheader('Available Schemas for the different downloads from y_finance')
			
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Download Schemas - Available')

		list_of_schemas = list(scope.download_schemas.keys())
		for schema in list_of_schemas:
			with col2: st.write(schema)
			schema_definition = scope.download_schemas[schema]
			with col2: st.write(scope.download_schemas[schema])
		with col3: st.write('< download_schemas >')

	if show_strategy:
		st.subheader('Strategy Parameters')
		# TODO not sure what the final format of some of these objects should be

		render_3_columns( 'Strategy Name', scope.strategy_name, 'strategy_name' )
		render_3_columns( 'Print Header', scope.strategy_print_header, 'strategy_print_header' )

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Price Columns')
		with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
		with col3: st.write('strategy_price_columns')
		
		render_3_columns( 'Print Count', scope.strategy_print_count, 'strategy_print_count' )
		render_3_columns( 'Build Header', scope.strategy_build_header, 'strategy_build_header' )
		render_3_columns( 'Header', scope.strategy_header, 'strategy_header' )
		render_3_columns( 'Print Line', scope.strategy_print_line, 'strategy_print_line' )
		# render_3_columns( 'JSON Dicitionary', scope.strategy_json_dict, 'strategy_json_dict' )
		render_3_columns( 'Chart', scope.chart_lines, 'chart_lines' )
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Json Dicitionary')
		with col2: st.write('strategy_json_dict')
		st.write(scope.strategy_json_dict)

		col1,col2 = st.columns([6,2])
		with col1: st.write('Results Dataframe')
		with col2: st.write('strategy_results')
		st.dataframe(scope.strategy_results, 2000, 1200)

	if show_charting:
		st.subheader('Charting Parameters')
		render_3_columns( 'Chart Line', scope.chart_lines, 'chart_lines' )
		render_3_columns( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
		render_3_columns( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )

	if show_application_variables:
		st.subheader('General Application Parameters')
		
		render_3_columns( 'Project Description', scope.project_description, 'project_description' )
		render_3_columns( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )
		render_3_columns( 'Initial Run / load', scope.initial_load, 'initial_load' )

		st.markdown("""---""")
		st.subheader('Dropdown Selections - Multiple Ticker Analysis < tickers_for_multi>')

		render_3_columns( 'Selected Market', scope.chosen_market, 'chosen_market' )
		render_3_columns( 'Selected Industry(s)', scope.chosen_industries, 'chosen_industries' )
		render_3_columns( 'Selected Ticker(s)', scope.chosen_tickers, 'chosen_tickers' )

		st.markdown("""---""")
		st.subheader('Dropdown Menu - Single Purpose Ticker Selections')

		render_3_columns( 'Ticker for Volume Analysis', scope.ticker_for_vol_predict, 'ticker_for_vol_predict' )
		render_3_columns( 'Ticker for Volume Analysis', scope.ticker_for_company_profile, 'ticker_for_company_profile' )

		st.markdown("""---""")
		st.subheader('Dropdown List Contents - available to select')
		
		render_3_columns( 'Available Markets for SINGLE selection', scope.chosen_market, 'chosen_market' )
		render_3_columns( 'Available Industries for MULTI selection', scope.dropdown_industries, 'dropdown_industries' )
		render_3_columns( 'Available Tickers for MULTI selection', scope.dropdown_tickers, 'dropdown_tickers' )
		render_3_columns( 'Available Tickers for SINGLE volume analysis', scope.dropdown_ticker_for_volume_analysis, 'dropdown_ticker_for_volume_analysis' )


		st.markdown("""---""")
		st.subheader('Result Parameters')

		render_3_columns( 'Result Passed', scope.result_passed, 'result_passed' )
		render_3_columns( 'Result Passed_2', scope.result_passed_2, 'result_passed_2' )
		render_3_columns( 'Result Failed', scope.result_failed, 'result_failed' )

	if show_folders:
		st.subheader('Folders and Paths')

		diff_col_size = [2,6,2]

		render_3_columns( 'Project Folder', scope.folder_project, 'folder_project', diff_col_size )
		render_3_columns( 'Share Data Folder', scope.folder_share_data, 'folder_share_data', diff_col_size )
		render_3_columns( 'Results Analysis Folder', scope.folder_results_analysis, 'folder_results_analysis', diff_col_size )
		render_3_columns( 'Website Output Folder', scope.folder_website, 'folder_website', diff_col_size )
		render_3_columns( 'Path for Share Index File', scope.path_ticker_index, 'path_ticker_index', diff_col_size )
		render_3_columns( 'Path for Website Output File', scope.path_website_file, 'path_website_file', diff_col_size )
		render_3_columns( 'Path for Share Data File', scope.path_share_data_file, 'path_share_data_file', diff_col_size )

	if show_market:
		st.subheader('Market Parameters')
		st.info( ('Current Share Market = ' + str(scope.share_market)) )

		render_3_columns( 'Share Market Suffix', scope.market_suffix, 'market_suffix' )
		
		st.markdown("""---""")
		st.subheader('Market Dates - Opening times and Public Holidays')

		render_3_columns( 'Public Holidays', scope.market_public_holidays, 'market_public_holidays' )
		render_3_columns( 'Opening Hours', scope.market_opening_hours, 'market_opening_hours' )


def render_3_columns( description, variable, variable_name, diff_col_size=None ):
	if diff_col_size == None:
		col1,col2,col3 = st.columns([2,4,2])
	else:
		col1,col2,col3 = st.columns(diff_col_size)
	
	with col1: st.write(description)
	with col2: st.write(variable)
	with col3: st.write( ('< ' + variable_name + ' >') )






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








# -----------------------------------------------------------------------------------------------------------------------------------
# Share Index Reports
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







