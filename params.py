# from types import SimpleNamespace

import pandas as pd
import pathlib
import os 
import time  
from datetime import datetime, timedelta 
import streamlit as st

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
def set_initial_session_state(session_state, project_description):
	if 'first_render_of_streamlit' not in session_state:
		session_state.first_render_of_streamlit = True


	print( 'first render = ', session_state.first_render_of_streamlit)
	if session_state.first_render_of_streamlit:
		# st.warning('Updating the session state params')
		# Streamlit Params
		session_state.display_page = 'undetermined'

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
		
def render_sidebar_drop_down_lists(session_state):
	if session_state.first_render_of_streamlit:
                                             
		# Available Share Markerts
		list_of_markets = list(markets.keys())
		list_of_markets.insert(0, '< select entire market >')
		session_state.available_markets = list_of_markets
		session_state.selected_market = None

		# Available Share industries
		list_of_industries = session_state.share_index_file['industry_group'].unique().tolist()
		list_of_industries.sort()
		session_state.available_industries = list_of_industries
		session_state.selected_industry = None
		
		# Available Share Tickers
		list_of_tickers = session_state.share_index_file.index.values.tolist()
		session_state.available_tickers = list_of_tickers
		session_state.selected_tickers = None
		
		# Ticker list - for analysis
		session_state.ticker_list_needs_updating = False
		session_state.ticker_list = []

def render_app_params_selector(session_state):
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
										'Folders', 
										'Strategy', 
										'Charting', 
										# 'Terminal',
										)
							)

	if param_group == 'Lists - Ticker(s)':
		st.subheader('Ticker Lists')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Ticker List Needs Updating ?')
		with col2: st.write(st.session_state.ticker_list_needs_updating)
		with col3: st.code('< ticker_list_needs_updating >')
		
		col1,col2 = st.columns([4,4])
		with col1: st.write('Analysis Ticker List')
		with col2: st.code('< ticker_list >')
		st.write(st.session_state.ticker_list)
		
		col1,col2 = st.columns([4,4])
		with col1: st.write('Loaded Ticker List')
		with col2: st.code('< share_data_loaded_list >')
		st.write(st.session_state.share_data_loaded_list)

		col1,col2 = st.columns([4,4])
		with col1: st.write('Missing Ticker List')
		with col2: st.code('< share_data_missing_list >')
		st.write(st.session_state.share_data_missing_list)

	if param_group == 'Lists - Industries':
		st.subheader('Share Index File contains the following Industries')
		industry_group_count = pd.DataFrame(st.session_state.share_index_file['industry_group'].value_counts())
		industry_group_count.index.name = 'Industry'
		industry_group_count.columns =['No of Codes']
		st.dataframe(industry_group_count, 2000, 1200)

	if param_group == 'File - Share Index File':
		col1,col2 = st.columns([4,4])
		with col1: st.subheader('Share Index File')
		with col2: st.code('< share_index_file >')
		st.dataframe(st.session_state.share_index_file, 2000, 1200)

	if param_group == 'File - Share Data Files': # TODO 
		col1,col2 = st.columns([4,4])
		with col1: st.subheader('Share Data Files (loaded)')
		with col2: st.code('< share_data_files >')
		#TODO - does this need to be a table - we need to load some data before checking
		st.write(st.session_state.share_data_files)

	if param_group == 'Streamlit':
		st.subheader('Streamlit Variables')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Initial Run / load')
		with col2: st.write(st.session_state.first_render_of_streamlit)
		with col3: st.code('< first_render_of_streamlit >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Selected Market')
		with col2: st.subheader(st.session_state.selected_market)
		with col3: st.code('< selected_market >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Selected Industry(s)')
		with col2: st.write(st.session_state.selected_industry)
		with col3: st.code('< selected_industry >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Selected Ticker(s)')
		with col2: st.write(st.session_state.selected_tickers)
		with col3: st.code('< selected_tickers >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('List of Available Markets Generated for Steamlit')
		with col2: st.write(st.session_state.available_markets)
		with col3: st.code('< available_markets >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('List of Available Industries Generated for Steamlit')
		with col2: st.write(st.session_state.available_industries)
		with col3: st.code('< available_industries >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('List of Available Tickers Generated for Steamlit')
		with col2: st.write(st.session_state.available_tickers)
		with col3: st.code('< available_tickers >')

	if param_group == 'Application':
		st.subheader('General Application Parameters')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Project Description')
		with col2: st.write(st.session_state.project_description)
		with col3: st.code('< project_description >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Project Start Time')
		with col2: st.write(datetime.fromtimestamp(st.session_state.project_start_time).strftime('%Y-%m-%d %H:%M:%S %p'))
		with col3: st.code('< project_start_time >')
		
		st.markdown("""---""")
		st.subheader('Terminal Parameters')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Audit')
		with col2: st.write(st.session_state.terminal_audit)
		with col3: st.code('< terminal_audit >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Width')
		with col2: st.write(st.session_state.terminal_width)
		with col3: st.code('< terminal_width >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Print Width')
		with col2: st.write(st.session_state.terminal_print_width)
		with col3: st.code('< terminal_print_width')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Count Passed')
		with col2: st.write(st.session_state.terminal_count_passed)
		with col3: st.code('< terminal_count_passed')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Count_2 Passed')
		with col2: st.write(st.session_state.terminal_count_passed_2)
		with col3: st.code('< terminal_count_passed_2')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Terminal Count Failed')
		with col2: st.write(st.session_state.terminal_count_failed)
		with col3: st.code('< terminal_count_failed >')

	if param_group == 'Market':
		st.subheader('Market Parameters')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Available Markets')
		with col2: st.write(st.session_state.available_markets)
		with col3: st.code('< available_markets >')
		# st.dataframe(st.session_state.available_markets, 2000, 1200)

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Selected Market')
		with col2: st.write(st.session_state.selected_market)
		with col3: st.code('< selected_market >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Market Share Suffix')
		with col2: st.write(st.session_state.market_suffix)
		with col3: st.code('< market_suffix >')
		# st.dataframe(st.session_state.market_suffix, 2000, 1200)

		st.markdown("""---""")
		st.subheader('Market Dates - Opening times and Public Holidays')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Public Holidays')
		with col2: st.write(st.session_state.market_public_holidays)
		with col3: st.code('< market_public_holidays >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Opening Hours')
		with col2: st.write(st.session_state.market_opening_hours)
		with col3: st.code('< market_opening_hours >')
		
	if param_group == 'Folders':
		st.subheader('Folders and Paths')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Project Folder')
		with col2: st.write(st.session_state.folder_project)
		with col3: st.code('folder_project')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Share Data Folder')
		with col2: st.write(st.session_state.folder_share_data)
		with col3: st.code('folder_share_data')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Results Analysis Folder')
		with col2: st.write(st.session_state.folder_results_analysis)
		with col3: st.code('folder_results_analysis')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Website Output Folder')
		with col2: st.write(st.session_state.folder_website)
		with col3: st.code('folder_website')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Share Index File')
		with col2: st.write(st.session_state.path_share_index)
		with col3: st.code('path_share_index')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Website Output File')
		with col2: st.write(st.session_state.path_website_file)
		with col3: st.code('path_website_file')

		col1,col2,col3 = st.columns([2,6,2])
		with col1: st.write('Path for Share Data File')
		with col2: st.write(st.session_state.path_share_data_file)
		with col3: st.code('path_share_data_file')

	if param_group == 'Strategy': # TODO
		st.subheader('Strategy Parameters')
		# TODO not sure what the final format of some of these objects should be
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Strategy Name')
		with col2: st.write(st.session_state.strategy_name)
		with col3: st.code('strategy_name')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Print Header')
		with col2: st.write(st.session_state.strategy_print_header)
		with col3: st.code('strategy_print_header')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Price Columns')
		with col2: st.dataframe(st.session_state.strategy_price_columns, 2000, 1200)
		with col3: st.code('strategy_price_columns')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Print Count')
		with col2: st.write(st.session_state.strategy_print_count)
		with col3: st.code('strategy_print_count')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Build Header')
		with col2: st.write(st.session_state.strategy_build_header)
		with col3: st.code('strategy_build_header')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Header')
		with col2: st.write(st.session_state.strategy_header)
		with col3: st.code('strategy_header')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Print Line')
		with col2: st.write(st.session_state.strategy_print_line)
		with col3: st.code('strategy_print_line')
		
		col1,col2 = st.columns([4,4])
		with col1: st.write('Json Dicitionary')
		with col2: st.code('strategy_json_dict')
		st.write(st.session_state.strategy_json_dict)

		col1,col2 = st.columns([4,4])
		with col1: st.write('Results Dataframe')
		with col2: st.code('strategy_results')
		st.dataframe(st.session_state.strategy_results, 2000, 1200)

	if param_group == 'Charting':
		st.subheader('Charting Parameters')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Chart Line')
		with col2: st.write(st.session_state.chart_lines)
		with col3: st.code('< chart_lines >')
		
		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Chart MACD on Price')
		with col2: st.write(st.session_state.chart_macd_on_price)
		with col3: st.code('< chart_macd_on_price >')

		col1,col2,col3 = st.columns([2,2,4])
		with col1: st.write('Chart MACD on Volume')
		with col2: st.write(st.session_state.chart_macd_on_volume)
		with col3: st.code('< chart_macd_on_volume >')

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


