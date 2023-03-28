
from apps.reports.dfs import render_available_dataframes



def render_dataframes(scope):
	
	app = scope.apps['display_app']
	if scope.apps[app]['render']['ticker_file'] != 'Show/Hide Data':
		render_available_dataframes(scope)