
from ticker_index.views.dataframes.dataframes import render_page_dataframes



def show_dataframes(scope):
	
	page = scope.pages['display']
	if scope.pages[page]['render']['ticker_file'] != 'Show/Hide Data':
		render_page_dataframes(scope)