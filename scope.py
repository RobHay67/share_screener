# from types import SimpleNamespace

import pandas as pd
import pathlib
import os 
import time  
from datetime import datetime, timedelta 
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
	if 'initial_load' not in scope:
		scope.initial_load = True
		scope.update_available_dropdowns = True
		
		
		
	if scope.initial_load:
		# st.warning('Updating the session state params')
		# Streamlit Params
		scope.display_page = 'undetermined'

		# Project Params
		scope.project_description = project_description
		scope.project_start_time = time.time()
		# Terminal Params
		scope.terminal_audit = False
		scope.terminal_width = 200
		scope.terminal_print_width = 0
		scope.terminal_count_passed = 0
		scope.terminal_count_passed_2 = 0
		scope.terminal_count_failed = 0
		# Result
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
		scope.path_share_index = pathlib.Path.home().joinpath( scope.folder_share_data, 'share_index.csv' )
		scope.path_website_file = pathlib.Path.home().joinpath( scope.folder_website, 'strategy_results.json' )
		scope.path_share_data_file = 'not yet set',
		# Load the Share Index File
		load_share_index_file(scope)



		# Ticker list - for analysis
		scope.update_ticker_list_required = False
		scope.ticker_list = []

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


		# Download Share Data
		scope.download_days = 1
		scope.download_groups_for_y_finance = []
		scope.download_schema = None
		scope.download_schemas = download_share_data_schemas	
		# scope.download_yf_share_data = None
		scope.download_yf_share_data = pd.DataFrame(columns=scope.share_data_usecols + ['ticker'] )
		scope.download_yf_anomolies =  {}


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
		
def build_ticker_dropdowns(scope):

	# st.error('The Ticker Dropdowns have been rebuilt!! - should this have happened?')

	print ( '\033[91m' + 'Ticker Dropdowns have been rebuil' + '\033[0m' )

	# Available Share Markerts
	list_of_markets = list(markets.keys())
	list_of_markets.insert(0, '< select entire market >')
	scope.available_markets = list_of_markets
	scope.selected_market = None
	scope.share_market = 'ASX'

	# Available Share industries
	list_of_industries = scope.share_index_file['industry_group'].unique().tolist()
	list_of_industries.sort()
	scope.available_industries = list_of_industries
	scope.selected_industry = None
	
	# Available Share Tickers
	list_of_tickers = scope.share_index_file.index.values.tolist()
	scope.available_tickers = list_of_tickers
	scope.selected_tickers = None

	# Dont run this again unless we have downloaded new share data
	scope.update_available_dropdowns = False
	
	
def render_scope_page(scope):
	st.title('Application Parameters')

	param_group = st.selectbox(
									'Show Application Parameters',
									(
										'< select group >',
										'Lists - Ticker(s)',
										'Lists - Industries',
										'File - Share Index File', 
										'File - Share Data Files', 
										'...............................system.parameters',
										'Streamlit',
										'Application',
										'Market', 
										'Download',
										'Folders', 
										'Strategy', 
										'Charting', 
										# 'Terminal',
										)
							)

	if param_group == 'Lists - Ticker(s)':
		st.subheader('Ticker Lists')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Ticker List Needs Updating ?')
		with col2: st.write(st.scope.ticker_list_needs_updating)
		with col3: st.write('< ticker_list_needs_updating >')
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Analysis Ticker List')
		with col2: st.write('< ticker_list >')
		st.write(st.scope.ticker_list)
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Loaded Ticker List')
		with col2: st.write('< share_data_loaded_list >')
		st.write(st.scope.share_data_loaded_list)

		col1,col2 = st.columns([6,2])
		with col1: st.write('Missing Ticker List')
		with col2: st.write('< share_data_missing_list >')
		st.write(st.scope.share_data_missing_list)

	if param_group == 'Lists - Industries':
		st.subheader('Share Index File contains the following Industries')
		industry_group_count = pd.DataFrame(st.scope.share_index_file['industry_group'].value_counts())
		industry_group_count.index.name = 'Industry'
		industry_group_count.columns =['No of Codes']
		st.dataframe(industry_group_count, 2000, 1200)

	if param_group == 'File - Share Index File':
		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Share Index File')
		with col2: st.write('< share_index_file >')
		st.dataframe(scope.share_index_file, 2000, 1200)

	if param_group == 'File - Share Data Files': # DONE 
		col1,col2 = st.columns([6,2])
		with col1: st.subheader('Loaded and Downloaded share data.')
		with col2: st.write('< share_data_files >')

		list_of_loaded_tickers = list(scope.share_data_files.keys())

		for ticker in list_of_loaded_tickers:
			my_expander = st.expander(label=ticker)
			my_expander.dataframe(scope.share_data_files[ticker], 2000, 2000)

	if param_group == 'Streamlit':
		st.subheader('Streamlit Variables')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Initial Run / load')
		with col2: st.write(scope.initial_load)
		with col3: st.write('< initial_load >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Selected Market')
		with col2: st.subheader(scope.selected_market)
		with col3: st.write('< selected_market >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Selected Industry(s)')
		with col2: st.write(scope.selected_industry)
		with col3: st.write('< selected_industry >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Selected Ticker(s)')
		with col2: st.write(scope.selected_tickers)
		with col3: st.write('< selected_tickers >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('List of Available Markets Generated for Steamlit')
		with col2: st.write(scope.available_markets)
		with col3: st.write('< available_markets >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('List of Available Industries Generated for Steamlit')
		with col2: st.write(scope.available_industries)
		with col3: st.write('< available_industries >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('List of Available Tickers Generated for Steamlit')
		with col2: st.write(scope.available_tickers)
		with col3: st.write('< available_tickers >')

	if param_group == 'Application':
		st.subheader('General Application Parameters')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Project Description')
		with col2: st.write(scope.project_description)
		with col3: st.write('< project_description >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Project Start Time')
		with col2: st.write(datetime.fromtimestamp(scope.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'))
		with col3: st.write('< project_start_time >')
		
		st.markdown("""---""")
		st.subheader('Result Parameters')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Result Passed')
		with col2: st.write(scope.result_passed)
		with col3: st.write('< result_passed >')
		with col1: st.write('Result Passed_2')
		with col2: st.write(scope.result_passed_2)
		with col3: st.write('< result_passed_2 >')
		with col1: st.write('Result Failed')
		with col2: st.write(scope.result_failed)
		with col3: st.write('< result_failed >')

		st.markdown("""---""")
		st.subheader('Terminal Parameters')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Audit')
		with col2: st.write(scope.terminal_audit)
		with col3: st.write('< terminal_audit >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Width')
		with col2: st.write(scope.terminal_width)
		with col3: st.write('< terminal_width >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Print Width')
		with col2: st.write(scope.terminal_print_width)
		with col3: st.write('< terminal_print_width')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Count Passed')
		with col2: st.write(scope.terminal_count_passed)
		with col3: st.write('< terminal_count_passed')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Count_2 Passed')
		with col2: st.write(scope.terminal_count_passed_2)
		with col3: st.write('< terminal_count_passed_2')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Terminal Count Failed')
		with col2: st.write(scope.terminal_count_failed)
		with col3: st.write('< terminal_count_failed >')

	if param_group == 'Market':
		st.subheader('Market Parameters')
		
		share_market_message = 'Current Share Market = ' + str(scope.share_market)
		st.success(share_market_message)

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Available Markets')
		with col2: st.write(scope.available_markets)
		with col3: st.write('< available_markets >')
		# st.dataframe(st.scope.available_markets, 2000, 1200)

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Selected Market')
		with col2: st.write(scope.selected_market)
		with col3: st.write('< selected_market >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Market Share Suffix')
		with col2: st.write(scope.market_suffix)
		with col3: st.write('< market_suffix >')
		# st.dataframe(st.scope.market_suffix, 2000, 1200)

		st.markdown("""---""")
		st.subheader('Market Dates - Opening times and Public Holidays')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Public Holidays')
		with col2: st.write(scope.market_public_holidays)
		with col3: st.write('< market_public_holidays >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Opening Hours')
		with col2: st.write(scope.market_opening_hours)
		with col3: st.write('< market_opening_hours >')

	if param_group == 'Download':
		st.subheader('Download Parameters')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Number of Days to Download')
		with col2: st.write(scope.download_days)
		with col3: st.write('< download_days >')

		st.markdown("""---""")
		st.subheader('Most Recent Download Variables and Data')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Appropriate download method')
		with col2: st.write(scope.download_schema)
		with col3: st.write('< download_schema >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Batched Groups of tickers for the download')
		with col2: st.write(scope.download_groups_for_y_finance)
		with col3: st.write('< download_groups_for_y_finance >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Downloaded Data from y_finance')
		with col2: st.write(scope.download_yf_share_data)
		with col3: st.write('< download_yf_share_data >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Error Messages from y_finance')
		with col2: st.write(scope.download_yf_anomolies)
		with col3: st.write('< download_yf_anomolies >')

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

	if param_group == 'Folders':
		st.subheader('Folders and Paths')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Project Folder')
		with col2: st.write(scope.folder_project)
		with col3: st.write('< folder_project >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Share Data Folder')
		with col2: st.write(scope.folder_share_data)
		with col3: st.write('< folder_share_data >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Results Analysis Folder')
		with col2: st.write(scope.folder_results_analysis)
		with col3: st.write('< folder_results_analysis >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Website Output Folder')
		with col2: st.write(scope.folder_website)
		with col3: st.write('< folder_website >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Share Index File')
		with col2: st.write(scope.path_share_index)
		with col3: st.write('< path_share_index >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Website Output File')
		with col2: st.write(scope.path_website_file)
		with col3: st.write('< path_website_file >')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Share Data File')
		with col2: st.write(scope.path_share_data_file)
		with col3: st.write('< path_share_data_file >')

	if param_group == 'Strategy': # TODO
		st.subheader('Strategy Parameters')
		# TODO not sure what the final format of some of these objects should be
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Strategy Name')
		with col2: st.write(scope.strategy_name)
		with col3: st.write('strategy_name')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Print Header')
		with col2: st.write(scope.strategy_print_header)
		with col3: st.write('strategy_print_header')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Price Columns')
		with col2: st.dataframe(scope.strategy_price_columns, 100, 200)
		with col3: st.write('strategy_price_columns')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Print Count')
		with col2: st.write(scope.strategy_print_count)
		with col3: st.write('strategy_print_count')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Build Header')
		with col2: st.write(scope.strategy_build_header)
		with col3: st.write('strategy_build_header')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Header')
		with col2: st.write(scope.strategy_header)
		with col3: st.write('strategy_header')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Print Line')
		with col2: st.write(scope.strategy_print_line)
		with col3: st.write('strategy_print_line')
		
		col1,col2 = st.columns([6,2])
		with col1: st.write('Json Dicitionary')
		with col2: st.write('strategy_json_dict')
		st.write(scope.strategy_json_dict)

		col1,col2 = st.columns([6,2])
		with col1: st.write('Results Dataframe')
		with col2: st.write('strategy_results')
		st.dataframe(scope.strategy_results, 2000, 1200)

	if param_group == 'Charting':
		st.subheader('Charting Parameters')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Chart Line')
		with col2: st.write(scope.chart_lines)
		with col3: st.write('< chart_lines >')
		
		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Chart MACD on Price')
		with col2: st.write(scope.chart_macd_on_price)
		with col3: st.write('< chart_macd_on_price >')

		col1,col2,col3 = st.columns([2,4,2])
		with col1: st.write('Chart MACD on Volume')
		with col2: st.write(scope.chart_macd_on_volume)
		with col3: st.write('< chart_macd_on_volume >')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Params sub groups - for easier maintenance - we need to move any remaining variables into the set initial session state
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


