import time  


from config.streamlit import set_streamlit_page_config

from charts.config import scope_charts
from config.progress.config import scope_progress
from config.tests.config import scope_tests

from files.config import scope_files
from apps.config import scope_apps
from strategies.config import scope_strategy
from users.load import load_user_table
from users.config import scope_user



from data.index.config import scope_index_file, scope_ticker_search
from data.tickers.config import scope_ticker_files, scope_download_variables


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime
	
	# TODO for releases purposes only - delete later
	scope.autologin = True
	
	if 'initial_load' not in scope:		
		
		scope_application_variables(scope)	# This contains all the application settings (see below)
		scope_dropdown_menus(scope)			# The data for the various selectors

		scope_progress(scope)				# Used to report on Function Progress

		scope_files(scope)					# Required before we can attempt to load the data

		scope_tests(scope)
		scope_charts(scope)

		scope_apps(scope)					# This contains all the app Specific settings
		
		scope.strategy = {}
		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case

		scope.users = {}
		load_user_table(scope)				# Load the users table
		scope_user(scope)					# Set Default Values ready for a user to login
		
		scope.data = {}
		scope_index_file(scope)				# load the share index
		scope_ticker_search(scope)			# variable to facilite searching for ticker by name
		scope_ticker_files(scope)			# variables for storing the ticker files
		scope_download_variables(scope)		# variable used during download of ticker data
		
	
		scope.initial_load = False			# Prevent session_state/scope from reloading with the default values

	return scope

	
def scope_application_variables(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Screener Application'
	scope.config['project_start_time'] = time.time()

	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere


def scope_dropdown_menus(scope):
	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] 	= ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	




	
