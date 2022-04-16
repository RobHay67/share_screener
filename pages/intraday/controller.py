from pages.view.header import render_page_title
from pages.picker.controller import render_ticker_picker


# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_intraday_page(scope):
	# render_page_title(scope, 'Intra Day Analysis', 'intraday')
	render_page_title(scope, 'Intra Day Analysis')

	render_ticker_picker(scope)

	ticker = scope.pages['single']['selectors']['ticker']

	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.data['ticker_files'].keys()):

			print('TODO render_intraday_page')

		


