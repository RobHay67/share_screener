
from pages.reports.dfs import render_available_dataframes



def render_dataframes(scope):
	
	page = scope.display_page
	if scope.pages[page]['render']['ticker_file'] != 'Show/Hide Data':
		render_available_dataframes(scope)