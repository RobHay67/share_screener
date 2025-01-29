from app.helpers.system import print_system_info_to_terminal
from app.scope.model.streamlit import set_streamlit_page_config
from app.scope.model.scope_config import scope_config
from app.scope.model.scope_display import scope_display
from app.scope.model.scope_page import scope_page
from files.scope.model.scope_files import scope_files
from users.scope.model.scope_users import scope_users
from screener.scope.model.scope_trials import scope_trials
from charts.scope.model.scope_charts import scope_charts
from tickers.scope.model.scope_tickers import scope_tickers
from ticker_index.scope.model.scope_ticker_index import scope_ticker_index
from tickers.scope.model.scope_ticker_schema import scope_tickers_schema
from app.scope.model.scope_config import scope_seach_for_ticker
from tickers.scope.model.scope_yf import scope_yf
from screener.scope.model.scope_strategy import scope_strategy


def set_scope(scope):

	print_system_info_to_terminal()
	set_streamlit_page_config()								# should only run onetime
	
	if 'config' not in scope:	
		scope.allow_auto_login = True		# TODO for releases purposes only - delete later
		
		scope_config(scope)					# This contains all the General page settings
		scope_display(scope)				# Value for the scope/config page to display
		scope_page(scope)					# Page specific config
		scope_files(scope)					# Folders & Paths - required before we can attempt to load the data
		scope_users(scope)					# Set Default Values ready for a user to login
		scope_trials(scope)					# add the trials configuration
		scope_charts(scope)					# add the chart configuration
		scope_tickers(scope)				# variables for storing the ticker files
		scope_ticker_index(scope)			# load the share index
		scope_tickers_schema(scope)			# download info for the tickers
		scope_seach_for_ticker(scope)		# variable to facilite searching for ticker by name
		scope_yf(scope)						# variable used during download of ticker data
		scope_strategy(scope)				# TODO - this may not even be required - keeping just in case

	return scope







	


	
