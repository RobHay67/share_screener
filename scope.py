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


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope out the Params Object == scope in streamlit
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_initial_scope(scope, project_description):
	if 'initial_load' not in scope:					# set the initial load state - keep this to a minimum
		scope.initial_load = True
		scope.dropdown_update_lists = False	# Intially set to false, the loading or refreshing of the share index file has resposibility to set this
			# TODO - do we need to do this??
		scope.share_market = 'ASX'				# Set Initial Applications Selections
		scope.display_page = 'initial_load'		# The homepage to display - 

	if scope.initial_load:
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

		# Ticker Selections are stored in these variables
		scope.tickers_market 				= 'select entire market'	# for the multi ticker selection screen
		scope.tickers_industries 			= None
		scope.tickers_multi 				= None
		# scope.tickers_for_multi 			= []
		scope.ticker						={
												'research'		:'select a ticker',
												'volume_predict':'select a ticker',
												'intraday'		:'select a ticker',
												'single'		:'select a ticker',
											}

		# Share Data Files
		scope.share_data_files 			= {}
		scope.downloaded_loaded_list 	= []
		scope.downloaded_missing_list 	= []
		scope.share_data_schema 		= share_data_schema
		scope.share_data_usecols 		= ['date', 'open', 'high', 'low', 'close', 'volume']
		scope.share_data_dtypes 		= {'open': 'float64', 'high': 'float64', 'low': 'float64', 'close': 'float64', 'volume': 'int64'}
		scope.share_data_dates 			= ['date']

		# Market Dictionaries
		scope.market_suffix 		 = markets
		scope.market_public_holidays = public_holidays
		scope.market_opening_hours 	 = opening_hours	

		# Object to store the Tickers to be loaded or downloaded
		scope.ticker_list = []

		# Download Ticker Variables
		scope.download_days 			= 1
		scope.download_industries 		= []
		scope.download_schemas 			= download_share_data_schemas	
		scope.downloaded_yf_ticker_data = pd.DataFrame(columns=scope.share_data_usecols + ['ticker'] )
		scope.downloaded_yf_anomolies 	=  {}


		# Analysis Variables
		scope.dropdown_ticker_columns = ['open', 'high', 'low', 'close', 'volume']

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

		# Prevent session_state from re-running during its use
		st.session_state.initial_load = False
		
def dropdown_update_lists(scope):
	print ( '\033[91m' + 'Dropdown Lists have been repopulated' + '\033[0m' )

	list_of_markets = list(scope.market_suffix.keys())
	list_of_markets.insert(0, 'select entire market')
	scope.dropdown_markets = list_of_markets
	
	list_of_industries = scope.ticker_index_file['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.dropdown_industries = list_of_industries
	
	list_of_tickers = scope.ticker_index_file.index.values.tolist()
	scope.dropdown_tickers = list_of_tickers

	alt_ticker_list = scope.ticker_index_file.index.values.tolist()
	alt_ticker_list.insert(0, 'select a ticker')
	scope.dropdown_ticker = alt_ticker_list
	
	# ---------------------------------------------------------------------------------------
	# Prevent executing this function again (until changes have been made to the share index)
	scope.dropdown_update_lists = False
	
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

	col1,col2,col3,col4,col5,col6 = st.columns([2,2,2,2,2,2])

	with col1: st.subheader('Data')
	with col1: show_ticker_index = st.button('Ticker Index File ( ' + str((len(st.session_state.ticker_index_file))) + ' )')
	with col1: show_share_data_files = st.button('Share Data Files ( ' + str(len(st.session_state.share_data_files.keys())) + ' )')
	with col1: show_industries = st.button('Industries')
	
	with col2: st.subheader('Analysis')
	with col2: show_strategy = st.button('Strategy')
	with col2: show_charting = st.button('Charting')

	with col3: st.subheader('Session')
	with col3: show_session = st.button('Session')
	with col3: show_selectors = st.button('Selectors')
	with col3: show_download = st.button('Download')
	with col3: show_results = st.button('Results')


	with col4: st.subheader('System')
	with col4: show_application = st.button('Application')
	with col4: show_folders = st.button('Folders')
	with col4: show_market = st.button('Share Market')

	if show_ticker_index:
		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Ticker Index File')
		with col2: st.write('< ticker_index_file >')
		st.dataframe(scope.ticker_index_file, 2000, 1200)

	if show_share_data_files:
		st.subheader('Loaded Ticker Files')
		render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )

		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Loaded and Downloaded share data.')
		with col2: st.write('< share_data_files >')

		list_of_loaded_tickers = list(scope.share_data_files.keys())

		for ticker in list_of_loaded_tickers:
			my_expander = st.expander(label=ticker)
			my_expander.dataframe(scope.share_data_files[ticker], 2000, 2000)
	
	if show_industries:
		st.subheader('Share Index File contains the following Industries')
		industry_group_count = pd.DataFrame(scope.ticker_index_file['industry_group'].value_counts())
		industry_group_count.index.name = 'Industry'
		industry_group_count.columns =['No of Codes']
		st.dataframe(industry_group_count, 2000, 1200)

	if show_strategy:
		st.subheader('Strategy Parameters')
		# TODO not sure what the final format of some of these objects should be

		render_3_columns( 'Strategy Name', scope.strategy_name, 'strategy_name' )
		render_3_columns( 'Print Header', scope.strategy_print_header, 'strategy_print_header' )

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Price Columns')
		with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
		with col3: st.write('< strategy_price_columns >')
		
		render_3_columns( 'Print Count', scope.strategy_print_count, 'strategy_print_count' )
		render_3_columns( 'Build Header', scope.strategy_build_header, 'strategy_build_header' )
		render_3_columns( 'Header', scope.strategy_header, 'strategy_header' )
		render_3_columns( 'Print Line', scope.strategy_print_line, 'strategy_print_line' )
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Json Dicitionary')
		with col2: st.write('< strategy_json_dict >')
		st.write(scope.strategy_json_dict)

		col1,col2 = st.columns([6,2])
		with col1: st.write('Results Dataframe')
		with col2: st.write('< strategy_results >')
		st.dataframe(scope.strategy_results, 2000, 1200)

	if show_charting:
		st.subheader('Charting Parameters')
		render_3_columns( 'Chart Line', scope.chart_lines, 'chart_lines' )
		render_3_columns( 'Chart MACD on Price', scope.chart_macd_on_price, 'chart_macd_on_price' )
		render_3_columns( 'Chart MACD on Volume', scope.chart_macd_on_volume, 'chart_macd_on_volume' )

	if show_session:
		st.subheader('Session Variables')

		render_3_columns( 'Initial Load Description', scope.initial_load, 'initial_load' )
		render_3_columns( 'Current Page to Display', scope.display_page, 'display_page' )
		render_3_columns( 'Current Share Market', scope.share_market, 'share_market' )


	if show_selectors:
		st.subheader('Ticker Selectors and Selections')

		render_3_columns( 'Initial Run / load', scope.initial_load, 'initial_load' )

		st.markdown("""---""")
		st.subheader('Ticker Selectors')
		col1,col2,col3,col4,col5,col6,col7 = st.columns([1.5,1.5,1,2,2.5,2.5,1])

		with col1:
			st.markdown('##### Selector')
			st.write('Share Market')
			st.write('Company Profile')
			st.write('Volume Prediction')
			st.write('Intra-Day')
			st.write('Single Ticker')
			st.write('Share Market')
			st.write('Industry')
			st.write('Tickers')
			st.write('Ticker Column')

		with col2:
			st.markdown('##### Contains')
			st.write('Target Market')
			st.write('Ticker in Index')
			st.write('Ticker in Index')
			st.write('Ticker in Index')
			st.write('Ticker in Index')
			st.write('Share Markets')
			st.write('Industry in Index')
			st.write('Ticker in Index')
			st.write('Column for Calculation')

		with col3:
			st.markdown('##### Widget')
			st.write('To Be Config')
			st.write('selectbox')
			st.write('selectbox')
			st.write('selectbox')
			st.write('selectbox')
			st.write('selectbox')
			st.write('multiselect')
			st.write('multiselect')
			st.write('multiselect')

		with col4:
			st.markdown('##### Populated from')
			st.write('**Hard Coded')
			st.write('< dropdown_ticker >')
			st.write('< dropdown_ticker >')
			st.write('< dropdown_ticker >')
			st.write('< dropdown_ticker >')
			st.write('< dropdown_markets >')
			st.write('< dropdown_industries >')
			st.write('< dropdown_tickers >')
			st.write('[ hard coded list ]')

		with col5:
			st.markdown('##### Current Selection')
			st.write(scope.share_market)
			st.write(scope.ticker['research'])
			st.write(scope.ticker['volume_predict'])
			st.write(scope.ticker['intraday'])
			st.write(scope.ticker['single'])
			st.write(scope.tickers_market)
			st.write(scope.tickers_industries)
			st.write(scope.tickers_multi)
			st.write(scope.dropdown_ticker_columns)

		with col6:
			st.markdown('##### Selection Stored In')
			st.write('< share_market >')
			st.write("< ticker['research'] >")
			st.write("< ticker['volume_predict'] >")
			st.write("< ticker['intraday'] >")
			st.write("< ticker['single'] >")
			st.write('< tickers_market >')
			st.write('< tickers_industries >')
			st.write('< tickers_multi >')
			st.write('  not stored ')			#TODO - we may need to store this for different indicators 

		
		
		st.markdown("""---""")
		st.subheader('Dropdown Lists (per above)')
		render_3_columns( 'Available Markets    ( selectbox )'  , scope.dropdown_markets	, 'dropdown_markets' )
		render_3_columns( 'Available Industries ( multiselect )', scope.dropdown_industries	, 'dropdown_industries' )
		render_3_columns( 'Available Tickers    ( multiselect )', scope.dropdown_tickers	, 'dropdown_tickers' )
		render_3_columns( 'Available Ticker     ( selectbox )'  , scope.dropdown_ticker		, 'dropdown_ticker' )

	if show_download:
		st.markdown('##### Download Variables')
		render_3_columns( 'Number of Days to Download', scope.download_days, 'download_days' )

		st.markdown("""---""")
		st.markdown('##### Most Recent Download Variables and Data')
		render_3_columns( 'Industry Groups for y_finance to iterate over', scope.download_industries, 'download_industries' )
		render_3_columns( 'Loaded Ticker List', scope.downloaded_loaded_list, 'downloaded_loaded_list' )
		render_3_columns( 'Missing Ticker List', scope.downloaded_missing_list, 'downloaded_missing_list' )
		render_3_columns( 'Downloaded Data from y_finance', scope.downloaded_yf_ticker_data, 'downloaded_yf_ticker_data' )
		render_3_columns( 'Error Messages  from y_finance', scope.downloaded_yf_anomolies  , 'downloaded_yf_anomolies' )

		st.markdown("""---""")
		st.markdown('##### Most Recent Ticker List which would have been utilised by the above variables')
		render_3_columns( 'Current Ticker List', (str(len(scope.ticker_list)) + ' ticker(s)'), 'ticker_list' )
		ticker_list_message = ''
		for count, ticker in enumerate(scope.ticker_list):
			ticker_list_message = ticker_list_message + ticker
			if count < len(scope.ticker_list) - 1:
				ticker_list_message += '  '
		st.info(ticker_list_message)

		st.markdown("""---""")
		st.subheader('Available Schemas for the different downloads from y_finance')
		col1,col2,col3 = st.columns([2,4,2])
		list_of_schemas = list(scope.download_schemas.keys())
		for schema in list_of_schemas:
			with col1: st.write(schema)
			# schema_definition = scope.download_schemas[schema]
			# schema_definition = pd.DataFrame(scope.download_schemas[schema])
			# print( schema_definition)
			with col2: st.write(scope.download_schemas[schema])
			# with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
			# with col2: st.write(schema_definition)
		with col3: st.write('< download_schemas >')
	
	if show_results:
		st.subheader('Results from Most Recent Batch Process')
		st.markdown("""---""")
		st.subheader('Result Parameters')
		render_3_columns( 'Result Passed', scope.result_passed, 'result_passed' )
		render_3_columns( 'Result Passed_2', scope.result_passed_2, 'result_passed_2' )
		render_3_columns( 'Result Failed', scope.result_failed, 'result_failed' )

	if show_application:
		st.subheader('General Application Parameters')
		render_3_columns( 'Project Description', scope.project_description, 'project_description' )
		render_3_columns( 'Project Start Time', datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'), 'project_start_time' )
		render_3_columns( 'Current Share Market', scope.share_market, 'share_market' )
	
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

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Helpers
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
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










