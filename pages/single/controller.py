from pages.view.header import render_page_title
from charts.controller import plot_charts
from pages.picker.controller import render_ticker_picker



# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Single Ticker Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
def render_single_ticker_page(scope):
	
	render_page_title(scope, 'Ticker Analysis (single ticker)')

	render_ticker_picker(scope)


	ticker = scope.pages['single']['selectors']['ticker']

	if ticker != 'select a ticker' :
		
		# Check that we have data available for this ticker
		# before attempting to make any plots

		if ticker in scope.pages['single']['df'].keys():	
			plot_charts(scope)
			


