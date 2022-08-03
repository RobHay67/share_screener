from apps_parts.ticker_loader.header import render_page_title
from apps_parts.ticker_loader.controller import render_ticker_loader

from apps_parts.ticker_search.search_results import render_search_results
# --------------------------------------------------------------------------------------------------------------------------------------------------------------
# Intra Day Analysis
# --------------------------------------------------------------------------------------------------------------------------------------------------------------

def render_intraday_page(scope):

	render_page_title(scope, 'Intra Day Analysis')

	render_ticker_loader(scope)

	ticker = scope.apps['intraday']['selectors']['ticker']

	if ticker != 'select a ticker' :		
		
		if ticker in list(scope.data['ticker_files'].keys()):

			print('TODO render_intraday_page')

		
	else:
		render_search_results(scope)


