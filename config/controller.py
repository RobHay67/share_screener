import time  

from config.model.streamlit import set_streamlit_page_config

from charts.config import scope_chart
from results.config import scope_results
from screener.config import scope_tests

from files.config import scope_files
# from config.model.data import scope_data
from data.config import scope_data
from pages.config import scope_pages
from strategies.config import scope_strategy

from pages.view.home_page import view_project_welcome
from config.model.dropdowns import update_dropdowns



def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime

	if 'initial_load' not in scope:		
		scope.initial_load = True			# set the initial load state (this will not run a second time)
											# prevents this section from runnning again and
											# allows the ticker index to load next

		scope_config(scope)					# This contains all the application settings
		scope_files(scope)					# Required before we can attempt to load the data
		scope_data(scope)					# load the share index
		scope_pages(scope)					# This contains all the page Specific settings
		scope_strategy(scope)

		view_project_welcome(scope)			# Render the home page

	if scope.config['dropdowns']['update_dropdowns']: 
		update_dropdowns(scope)

	return scope

	







def scope_config(scope):
	# Application Fixex Variables
	scope.config = {}
	scope.config['project_description'] = 'DDT - Data Driven Trading'
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
	scope.config['dropdowns']['price_columns '] = ['open', 'high', 'low', 'close' 		   ]	


	scope.config['tests'] = {}
	scope_tests(scope)


	scope.config['charts'] = {}
	scope_chart(scope)


	scope.config['results'] = {}
	scope_results(scope)
