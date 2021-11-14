
import streamlit as st
import time  
import pandas as pd

# from ticker.schema import share_data_schema
# from config.yfinance import download_share_data_schemas
from config.markets import markets, public_holidays, opening_hours
from scope.folders import scope_folders
from scope.chart import scope_chart
from scope.strategy import scope_strategy


from index.load import load_ticker_index_file

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
		scope.ticker_index_file = {}

	if scope.initial_load:

		# Streamlit Variables
		scope.st_button = None

		# Project Params
		scope.project_description = project_description
		scope.project_start_time = time.time()
				
		# Results - for batch processing of multiple tickers
		scope.results = { 'passed':'', 'passed_2':'', 'failed':'', 'passed_count':0, 'passed_2_count':0, 'failed_count':0 }
		
		scope_folders(scope)
		
		# Primary Application Objects
		load_ticker_index_file(scope)				# adds the scope.ticker_index_file
		scope.share_data_files 			= {}		# TODO rename to ticker_data_files


		# Ticker Selections are stored in these variables
		scope.selected_market 				= 'select entire market'	# for the multi ticker selection screen
		scope.selected_industries 			= None
		scope.selected_tickers 				= None
		scope.ticker_list					= {	
												'multi'			: [],
												'single'		:['select a ticker'],
												'intraday'		:['select a ticker'],
												'volume'		:['select a ticker'],
												'research'		:['select a ticker'],
											}

		# Download Ticker Variables
		scope.download_days 			= 5
		scope.download_industries 		= []
		scope.download_yf_files			= {}
		scope.downloaded_loaded_list 	= []
		scope.downloaded_missing_list 	= []
		scope.downloaded_yf_anomolies 	= {}


		# Analysis Variables
		scope.analysis_limit_share_data = 300
		# scope.analysis_apply_limit = False

		scope_strategy(scope)
		scope_chart(scope)

		# Prevent session_state from re-running during its use
		st.session_state.initial_load = False
		
