import time  


from config.streamlit import set_streamlit_page_config

from config.charts.config import scope_charts
from config.results.config import scope_results
from config.tests.config import scope_tests

from files.config import scope_files
from apps.config import scope_pages
from strategies.config import scope_strategy
from users.model.config import scope_user
from data.config import scope_data

from users.model.load import load_user_table
from config.dropdowns import update_dropdowns


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime
	
	# Todo for releases
	scope.autologin = True
	
	if 'initial_load' not in scope:		
		scope.initial_load = True			# set the initial load state (this will not run a second time)
											# prevents this section from runnning again and
											# allows the ticker index to load next
		scope_config(scope)					# This contains all the application settings (see below)
		scope_files(scope)					# Required before we can attempt to load the data
		scope_pages(scope)					# This contains all the page Specific settings
		scope_strategy(scope)
				
		scope_user(scope)					# Load the users table
		scope_data(scope)					# load the share index
		load_user_table(scope)				# Load the users table
	
		scope.initial_load = False			# Prevent session_state from re-running during its use

	# The dropdown menus occasionaly need repopulating
	if scope.config['dropdowns']['update_dropdowns']: 
		update_dropdowns(scope)


	return scope

	
def scope_config(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'Share Screener Application'
	scope.config['project_start_time'] = time.time()


	# System Wide Variables
	scope.config['share_market'] = 'ASX'						# Set Initial Default Share Market - we gotta start somewhere

	# Dropdowns
	scope.config['dropdowns'] = {}
	scope.config['dropdowns']['update_dropdowns'] = False		# Intially set to false, the loading or refreshing of the 
																# share index file has resposibility to modify this, but can
																# only do this after loading the share index file

	scope.config['dropdowns']['markets'] = []
	scope.config['dropdowns']['industries'] = []
	scope.config['dropdowns']['tickers'] = []
	scope.config['dropdowns']['ticker'] = []
	scope.config['dropdowns']['ohlcv_columns'] 	= ['open', 'high', 'low', 'close', 'volume']
	scope.config['dropdowns']['price_columns'] = ['open', 'high', 'low', 'close' 		   ]	


	scope_tests(scope)

	scope_charts(scope)

	scope_results(scope)

	
