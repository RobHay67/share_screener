from pages.view.title import render_page_title
from charts.controller import plot_charts




# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_single_ticker_page(scope):
	
	render_page_title(scope, 'Ticker Analysis')

	ticker = scope.pages['single']['selectors']['ticker']

	if ticker != 'select a ticker' :
		
		# Check that we have data available for this ticker
		# before attempting to make any plots

		if ticker in scope.pages['single']['df'].keys():	
			print('Rob - commented out the plot chart for thwe moment') # TODO - undo this
			# plot_charts(scope, ticker)
			


