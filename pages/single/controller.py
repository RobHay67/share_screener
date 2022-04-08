from pages.view.analysis_title import analysis_titles
from charts.controller import plot_charts




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_single_ticker_page(scope):
	# analysis_titles(scope, 'Ticker Analysis', 'single')
	analysis_titles(scope, 'Ticker Analysis')
	
	ticker = scope.pages['single']['ticker_list'][0]
	
	if ticker in scope.pages['single']['chart_df'].keys():	
		plot_charts(scope, ticker)
		


