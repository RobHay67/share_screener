import time

from app.helpers.system import print_system_info_to_terminal
from app.views.streamlit_config import set_streamlit_page_config
from app.scope_pages import scope_pages, scope_ticker_search
from files.config import scope_folders_and_paths
from users.config import scope_users
from screener.config.scope import scope_trials
from charts.config.scope import scope_charts
from ticker_index.config import scope_index_file
from tickers.scope import scope_tickers
from tickers.missing_tickers.config import scope_tickers_missing
from y_finance.config import scope_download_variables
from strategies.config import scope_strategy


def set_scope(scope):

	print_system_info_to_terminal()
	set_streamlit_page_config()								# should only run onetime
	
	if 'pages' not in scope:	
		scope.allow_auto_login = True			# TODO for releases purposes only - delete later
		scope.config = {}
		scope.config['project_description'] = 'Share Picker'
		scope.config['project_start_time'] 	= time.time()
		
		scope_pages(scope)					# This contains all the page Specific settings
		scope_folders_and_paths(scope)		# Required before we can attempt to load the data
		scope_users(scope)					# Set Default Values ready for a user to login
		scope_trials(scope)					# add the trials configuration
		scope_charts(scope)					# add the chart configuration
		scope_tickers(scope)				# variables for storing the ticker files
		scope_index_file(scope)				# load the share index
		scope_tickers_missing(scope)		# track missing tickers and associated errors
		scope_ticker_search(scope)			# variable to facilite searching for ticker by name
		scope_download_variables(scope)		# variable used during download of ticker data
		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case

	return scope







	


	
