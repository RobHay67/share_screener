import os
import pathlib
import streamlit as st
import time  
import pandas as pd

from config.ticker_file import share_data_schema
from config.yfinance import download_share_data_schemas
from config.markets import markets, public_holidays, opening_hours




from index.file import load_index

# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Scope out the Params Object == scope in streamlit
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def set_scope(scope, project_description):
	if 'initial_load' not in scope:					# set the initial load state - keep this to a minimum
		scope.initial_load = True
		scope.dropdown_lists_need_updating = False	# Intially set to false, the loading or refreshing of the 
													# share index file has resposibility to set this, but can
													# only do this after loading the share index file
		scope.share_market = 'ASX'					# Set Initial Default Share Market - we gotta start somewhere
		scope.display_page = 'initial_load'			# The homepage to display on first load

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
		scope.folder_project = pathlib.Path(__file__).parent.parent.resolve()

		print( '='*1000)
		print(scope.folder_project)


		scope.folder_share_data = pathlib.Path.home().joinpath( scope.folder_project, 'files' )
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
		load_index(scope)

		# Ticker Selections are stored in these variables
		scope.tickers_market 				= 'select entire market'	# for the multi ticker selection screen
		scope.tickers_industries 			= None
		scope.tickers_multi 				= None
		# scope.tickers_for_multi 			= []
		scope.ticker						={
												'research'		:'select a ticker',
												'volume'		:'select a ticker',
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
		scope.analysis_limit_share_data = 300
		# scope.analysis_apply_limit = False


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
		
