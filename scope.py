import streamlit as st
import time  

from partials.dropdowns.config import scope_dropdown_menus
from files.config import scope_folders_and_paths
from users.config import scope_user
from progress.config import scope_progress
from apps.config import scope_apps
from trials.config import scope_trials
from charts.config import scope_charts
from ticker_index.config import scope_index_file
from partials.ticker_search.config import scope_ticker_search
from tickers.config import scope_ticker_files, scope_download_variables
from strategies.config import scope_strategy


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime
	
	# TODO for releases purposes only - delete later
	scope.autologin = True
	
	if 'initial_load' not in scope:		
		
		scope_application_variables(scope)	# This contains all the application settings (see below)
		
		scope_dropdown_menus(scope)			# The data for the various selectors
		
		scope_folders_and_paths(scope)		# Required before we can attempt to load the data
		
		scope_user(scope)					# Set Default Values ready for a user to login
		
		scope_progress(scope)				# Used to report on Function Progress

		scope_apps(scope)					# This contains all the app Specific settings

		scope_trials(scope)					# add the trials configuration
		
		scope_charts(scope)					# add the chart configuration

		scope_index_file(scope)				# load the share index
		
		scope_ticker_search(scope)			# variable to facilite searching for ticker by name
		
		scope_ticker_files(scope)			# variables for storing the ticker files
		
		scope_download_variables(scope)		# variable used during download of ticker data

		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case
	
		scope.initial_load = False			# Prevent session_state/scope from reloading with the default values

	return scope

	
def scope_application_variables(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Screener Application'
	scope.config['project_start_time'] = time.time()

	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere



def set_streamlit_page_config():
	
	# Set the Browser Tab Name for the App
	st.set_page_config( 
			page_title='DDT - Data Driven Trading', 
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
	st.markdown("""
        <style>
            #    .css-18e3th9 {
            #         padding-top: 0rem;
            #         padding-bottom: 10rem;
            #         padding-left: 5rem;
            #         padding-right: 5rem;
            #     }
            #    .css-1d391kg {
            #         padding-top: 1rem;
            #         padding-right: 1rem;
            #         padding-bottom: 3.5rem;
            #         padding-left: 1rem;
            #     }
        </style>
        """, unsafe_allow_html=True)

