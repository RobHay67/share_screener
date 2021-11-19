from scope.project.scope import scope_project
from scope.app.scope import scope_app
from scope.pages.scope import scope_pages
from scope.folders.scope import scope_folders
from scope.download.scope import scope_download
from scope.strategy.scope import scope_strategy
from analysis.charts.scope import scope_chart
# from analysis.measures.scope import scope_measures
from scope.results.scope import scope_results
from scope.user.scope import scope_user
from ticker.scope import scope_ticker_files

from index.scope import scope_index


def set_scope(scope, project_description):
	if 'we_need_to_load_the_ticker_index' not in scope:		# set the initial load state - keep this to a minimum
		scope.we_need_to_load_the_ticker_index = True
		scope_project(scope, project_description)
		scope_app(scope)									# This contains all the application settings
		scope_pages(scope)									# This contains all the page Specific settings
		scope_folders(scope)								# Required before we can attempt to load the data
		scope_download(scope)
		scope_strategy(scope)
		scope_chart(scope)
		# scope_measures(scope)
		scope_results(scope)
		scope_user(scope)
		scope_ticker_files(scope)

	if scope.we_need_to_load_the_ticker_index:
		scope_index(scope)
		scope.we_need_to_load_the_ticker_index = False		# Prevent session_state from re-running during its use


	return scope

