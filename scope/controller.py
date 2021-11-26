
# Scope Controller


from config.streamlit import set_streamlit_page_config

from scope.model.project import scope_project
from scope.model.app import scope_app
from pages.model.pages import scope_pages
from scope.model.folders import scope_folders
from ticker.model.download import scope_download
from scope.model.strategy import scope_strategy
from charts.model.charts import scope_chart
from scope.model.results import scope_results
from ticker.model.tickers import scope_tickers
from index.model.index import scope_index
from analysis.model.analysis import scope_analysis

from scope.dropdowns import update_dropdowns

from pages.view.sidebar import view_sidebar
from pages.controller import view_selected_page


def set_scope(scope):
	
	set_streamlit_page_config()								# should only run onetime

	if 'initial_load' not in scope:			
		scope.initial_load = True			# set the initial load state 
											# prevents this section from runnning again and
											# allows the ticker index to load next

		scope_project(scope)
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

	view_sidebar(scope)						# Render the Sidebar
	view_selected_page(scope)				# Render the selected Page

	return scope



	

