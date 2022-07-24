from apps.ticker_loader.header import render_page_title
from apps.ticker_loader.controller import render_ticker_loader

from apps.ticker_loader.search_results import render_search_results
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_intraday_page(scope):

	render_page_title(scope, 'Intra Day Analysis')

	render_ticker_loader(scope)

	ticker = scope.pages['intraday']['selectors']['ticker']

	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.data['ticker_files'].keys()):

			print('TODO render_intraday_page')

		
	else:
		render_search_results(scope)


