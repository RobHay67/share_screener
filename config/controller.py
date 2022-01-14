from config.params.screener import scope_screener
from config.params.app import scope_app
# from config.params.charts import scope_chart
from charts.config import scope_chart
from config.params.download import scope_download
# from config.params.folders import scope_folders
from files.config import scope_folders
# from config.params.index import scope_index
from index.config import scope_index
from config.params.pages import scope_pages
from config.params.results import scope_results
from config.params.strategy import scope_strategy
from config.params.streamlit import set_streamlit_page_config
# from config.params.ticker_files import scope_tickers
from tickers.config import scope_tickers

from config.model.dropdowns import update_dropdowns

# TODO - need to eliminate as many of these as we can - have the code refer directly to the config module 
# instead of storing it in the scope - ie folders

from pages.view.home_page import view_project_welcome


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime

	if 'initial_load' not in scope:					
		scope.initial_load = True			# set the initial load state 
											# prevents this section from runnning again and
											# allows the ticker index to load next

		scope_app(scope)					# This contains all the application settings
		scope_pages(scope)					# This contains all the page Specific settings
		scope_folders(scope)				# Required before we can attempt to load the data
		scope_download(scope)
		scope_strategy(scope)
		scope_chart(scope)
		scope_results(scope)
		scope_screener(scope)
		scope_tickers(scope)

		view_project_welcome(scope)			# Render the home page

	if scope.initial_load:					# This will only run one time after the initial load has occured
		scope_index(scope)
		scope.initial_load = False			# Prevent session_state from re-running during its use

	if scope.dropdown_lists_need_updating: 
		update_dropdowns(scope)



	return scope


# For Testing Purposes Only
def print_scope_to_terminal(scope):
	print( 'List of all keys in the st.session_state')
	if 'initial_load' in scope:
		for key in sorted(scope):
			print ( key)
	print ( '-'*100)
	

