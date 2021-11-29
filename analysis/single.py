from analysis.view.titles import analysis_titles
from charts.controller import plot_charts




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def analysis_ticker_page(scope):
	analysis_titles(scope, 'Ticker Analysis', 'single')
	
	ticker = scope.pages['single']['ticker_list'][0]
	
	if ticker in scope.pages['single']['chart_df'].keys():	
		plot_charts(scope, ticker)
		


