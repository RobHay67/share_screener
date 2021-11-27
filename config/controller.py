from config.helpers.analysis import scope_analysis
from config.helpers.app import scope_app
from config.helpers.charts import scope_chart
from config.helpers.download import scope_download
from config.helpers.folders import scope_folders
from config.helpers.index import scope_index
from config.helpers.pages import scope_pages
from config.helpers.results import scope_results
from config.helpers.strategy import scope_strategy
from config.helpers.streamlit import set_streamlit_page_config
from config.helpers.ticker import scope_tickers

from config.model.dropdowns import update_dropdowns

# TODO - need to eliminate as many of these as we can - have the code refer directly to the config module 
# instead of storing it in the scope - ie folders


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
		scope_analysis(scope)
		scope_tickers(scope)

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
	

