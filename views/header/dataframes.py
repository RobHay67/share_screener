
from views.ticker_index.dataframes.report import render_page_dataframes



def render_dataframes(scope):
	
	page = scope.pages['display']
	if scope.pages[page]['render']['ticker_file'] != 'Show/Hide Data':
		render_page_dataframes(scope)