import streamlit as st
import time  

from files.config import scope_folders_and_paths
from users.config import scope_users
from apps.config.app import scope_apps
from trials.config import scope_trials
from charts.config import scope_charts
from ticker_index.config import scope_index_file
from apps.config.ticker_search import scope_ticker_search
from apps.config.dropdowns import scope_dropdown_menus
from tickers.config import scope_ticker_files
from apps.config.missing_tickers import scope_missing_tickers
from tickers.download.config import scope_download_variables
from strategies.config import scope_strategy




def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime
	
	# TODO for releases purposes only - delete later
	scope.autologin = True
	
	if 'initial_load' not in scope:		
		
		scope_application_variables(scope)	# This contains all the application settings (see below)
		
		scope_dropdown_menus(scope)			# The data for the various selectors
		
		scope_folders_and_paths(scope)		# Required before we can attempt to load the data
		
		scope_users(scope)					# Set Default Values ready for a user to login
		
		scope_apps(scope)					# This contains all the app Specific settings

		scope_trials(scope)					# add the trials configuration
		
		scope_charts(scope)					# add the chart configuration

		scope_index_file(scope)				# load the share index
		
		scope_ticker_search(scope)			# variable to facilite searching for ticker by name
		
		scope_ticker_files(scope)			# variables for storing the ticker files

		scope_missing_tickers(scope)		# lists of tickers that failed to upload or download
		
		scope_download_variables(scope)		# variable used during download of ticker data

		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case
	
		scope.initial_load = False			# Prevent session_state/scope from reloading with the default values

	return scope

	
def scope_application_variables(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Picker'
	scope.config['project_start_time'] = time.time()

	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere



def set_streamlit_page_config():
	
	# Set the Browser Tab Name for the App
	st.set_page_config( 
			page_title='Share Picker', 
			page_icon='📊',
			layout="wide",								# Allow wide Screen to be taken advantage of
			)
	
	# Padding Between Controls
	padding = 1.0
	st.markdown(f""" <style>
		.reportview-container .main .block-container{{
			padding-top: {padding}rem;
			padding-right: {padding}rem;
			padding-left: {padding}rem;
			padding-bottom: {padding}rem;
		}} </style> """, unsafe_allow_html=True)

	# Remove whitespace from the top of the app and sidebar
	st.write('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True) # this is heaps better

	# st.markdown("""
	# 				<style>
	# 					.css-o18uir.e16nr0p33 {
	# 					margin-top: -75px;
	# 					}
	# 				</style>
	# 				""", unsafe_allow_html=True)

	# st.markdown(
    #         f'''
    #         <style>
    #             .reportview-container .sidebar-content {{
    #                 padding-top: {1}rem;
    #             }}
    #             .reportview-container .main .block-container {{
    #                 padding-top: {1}rem;
    #             }}
    #         </style>
    #         ''',unsafe_allow_html=True)


	# st.markdown("""
    #     <style>
    #         #    .css-18e3th9 {
    #         #         padding-top: 0rem;
    #         #         padding-bottom: 10rem;
    #         #         padding-left: 5rem;
    #         #         padding-right: 5rem;
    #         #     }
    #         #    .css-1d391kg {
    #         #         padding-top: 1rem;
    #         #         padding-right: 1rem;
    #         #         padding-bottom: 3.5rem;
    #         #         padding-left: 1rem;
    #         #     }
    #     </style>
    #     """, unsafe_allow_html=True)

