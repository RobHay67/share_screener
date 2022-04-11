from pages.view.title import render_page_title
from charts.controller import plot_charts




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_single_ticker_page(scope):
	# render_page_title(scope, 'Ticker Analysis', 'single')
	render_page_title(scope, 'Ticker Analysis')
	
	ticker = scope.pages['single']['ticker_list'][0]
	
	if ticker in scope.pages['single']['df'].keys():	
		plot_charts(scope, ticker)
		


